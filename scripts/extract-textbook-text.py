#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "02、最新教材-新大纲(第二版)"
AI_ROOT = SOURCE_ROOT / "AI教材库"
OUTPUT_ROOT = AI_ROOT / "原始文本"
REPORT_PATH = AI_ROOT / "抽取报告.md"
INDEX_PATH = AI_ROOT / "教材索引.md"

LFS_SIGNATURE = b"version https://git-lfs.github.com/spec/v1"
DEFAULT_CHUNK_PAGES = 12
DEFAULT_OCR_WORKERS = 2
DEFAULT_OCR_DPI = 180
MIN_SOURCE_AVG_CHARS = 120
MIN_PAGE_CHARS = 30

SOURCE_PROFILES = {
    "系统架构第二版 大纲.pdf": {
        "source_kind": "考试大纲",
        "priority": 110,
        "role": "用于判定考试范围、能力要求与章节边界；不替代教材正文解释。",
    },
    "系统架构设计师教程第二版可搜索.pdf": {
        "source_kind": "主教材",
        "priority": 100,
        "role": "用于概念、机制、公式、章节知识覆盖的主干校验。",
    },
    "【带搜索】系统架构设计师第二版.pdf": {
        "source_kind": "教材交叉核验",
        "priority": 90,
        "role": "用于与主教材交叉核验文字层、页码和可能缺失内容。",
    },
    "2_系统架构师32小时.pdf": {
        "source_kind": "应试辅导",
        "priority": 70,
        "role": "用于应试视角、重点归纳和辅助解释，不单独作为范围裁决依据。",
    },
    "彩色 考试32小时通关-第2版（2023）.pdf": {
        "source_kind": "应试辅导",
        "priority": 65,
        "role": "用于应试视角、例题和记忆辅助，不单独作为范围裁决依据。",
    },
    "软件体系结构原理、方法与实践_第2版.pdf": {
        "source_kind": "扩展参考",
        "priority": 60,
        "role": "用于软件体系结构相关主题的扩展理解；与考试口径冲突时不覆盖大纲/主教材。",
    },
}


def yaml_value(value):
    if value is None:
        return '""'
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)


def profile_for(path):
    return SOURCE_PROFILES.get(
        path.name,
        {
            "source_kind": "教材资料（待分类）",
            "priority": 50,
            "role": "作为补充资料使用；来源角色需要人工确认。",
        },
    )


def is_lfs_pointer(path):
    try:
        return LFS_SIGNATURE in path.read_bytes()[:256]
    except OSError:
        return False


def require_tool(name, install_hint):
    if shutil.which(name) is None:
        raise RuntimeError(f"未找到 {name}。{install_hint}")


def pdf_page_count(path):
    require_tool(
        "pdfinfo",
        "macOS 可执行 brew install poppler；GitHub Actions 会自动安装 poppler-utils。",
    )
    proc = subprocess.run(
        ["pdfinfo", str(path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        err = proc.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(err or f"pdfinfo 退出码 {proc.returncode}")
    text = proc.stdout.decode("utf-8", errors="replace")
    match = re.search(r"^Pages:\s+(\d+)\s*$", text, re.MULTILINE)
    if not match:
        raise RuntimeError("pdfinfo 未返回可识别的 Pages 字段。")
    return int(match.group(1))


def extract_pdf_pages(path):
    require_tool(
        "pdftotext",
        "macOS 可执行 brew install poppler；GitHub Actions 会自动安装 poppler-utils。",
    )
    page_count = pdf_page_count(path)
    proc = subprocess.run(
        ["pdftotext", "-layout", "-enc", "UTF-8", str(path), "-"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        err = proc.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(err or f"pdftotext 退出码 {proc.returncode}")

    raw = proc.stdout.decode("utf-8", errors="replace")
    pages = raw.split("\f")
    while pages and not pages[-1].strip():
        pages.pop()
    pages = [normalize_page(page) for page in pages]

    if len(pages) < page_count:
        pages.extend([""] * (page_count - len(pages)))
    elif len(pages) > page_count:
        pages = pages[:page_count]
    return pages


def normalize_page(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.splitlines()]
    out = []
    blank_count = 0
    for line in lines:
        if line.strip():
            blank_count = 0
            out.append(line)
        else:
            blank_count += 1
            if blank_count <= 2:
                out.append("")
    return "\n".join(out).strip()


def useful_chars(text):
    return len(re.sub(r"\s+", "", text))


def classify_extract_status(pages):
    if not pages:
        return "失败", "未识别到 PDF 页面。"
    char_counts = [useful_chars(page) for page in pages]
    avg_chars = sum(char_counts) / len(char_counts)
    weak_pages = sum(1 for count in char_counts if count < MIN_PAGE_CHARS)
    weak_ratio = weak_pages / len(char_counts)
    if avg_chars < MIN_SOURCE_AVG_CHARS:
        return "需OCR", f"平均每页仅约 {avg_chars:.0f} 个非空白字符，疑似扫描版或文字层异常。"
    if weak_ratio >= 0.30:
        return "部分可解析", f"约 {weak_ratio:.0%} 页面文字很少，图片/扫描页可能缺失。"
    return "可解析", ""


def ocr_pdf_page(path, page_no, dpi):
    require_tool(
        "pdftoppm",
        "macOS 可执行 brew install poppler；GitHub Actions 会自动安装 poppler-utils。",
    )
    require_tool(
        "tesseract",
        "macOS 可执行 brew install tesseract tesseract-lang；GitHub Actions 会安装中英文 OCR 语言包。",
    )
    with tempfile.TemporaryDirectory(prefix="textbook-ocr-") as tmpdir:
        prefix = Path(tmpdir) / "page"
        render = subprocess.run(
            [
                "pdftoppm",
                "-f",
                str(page_no),
                "-l",
                str(page_no),
                "-singlefile",
                "-r",
                str(dpi),
                "-png",
                str(path),
                str(prefix),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if render.returncode != 0:
            err = render.stderr.decode("utf-8", errors="replace").strip()
            raise RuntimeError(err or f"pdftoppm 第 {page_no} 页退出码 {render.returncode}")

        image_path = prefix.with_suffix(".png")
        if not image_path.exists():
            raise RuntimeError(f"第 {page_no} 页 OCR 渲染图片未生成。")

        ocr = subprocess.run(
            [
                "tesseract",
                str(image_path),
                "stdout",
                "-l",
                "chi_sim+eng",
                "--psm",
                "6",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if ocr.returncode != 0:
            err = ocr.stderr.decode("utf-8", errors="replace").strip()
            raise RuntimeError(err or f"tesseract 第 {page_no} 页退出码 {ocr.returncode}")
        return normalize_page(ocr.stdout.decode("utf-8", errors="replace"))


def apply_ocr_fallback(path, pages, status, workers, dpi):
    if status == "需OCR":
        targets = list(range(len(pages)))
    elif status == "部分可解析":
        targets = [i for i, page in enumerate(pages) if useful_chars(page) < MIN_PAGE_CHARS]
    else:
        return pages, set(), 0, []

    if not targets:
        return pages, set(), 0, []

    updated = list(pages)
    replaced_pages = set()
    errors = []

    def task(index):
        page_no = index + 1
        try:
            text = ocr_pdf_page(path, page_no, dpi)
            return index, text, ""
        except Exception as exc:
            return index, "", str(exc)

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(task, index) for index in targets]
        for future in as_completed(futures):
            index, text, error = future.result()
            if error:
                errors.append(f"第 {index + 1} 页：{error}")
                continue
            if useful_chars(text) > useful_chars(updated[index]):
                updated[index] = text
                replaced_pages.add(index + 1)

    return updated, replaced_pages, len(targets), errors


def scan_sources():
    if not SOURCE_ROOT.exists():
        return []
    files = [
        path
        for path in SOURCE_ROOT.glob("*.pdf")
        if path.is_file() and AI_ROOT not in path.parents
    ]
    return sorted(files, key=lambda p: (-int(profile_for(p)["priority"]), p.name))


def render_chunk(source, pages, start_page, end_page, status, ocr_pages):
    profile = profile_for(source)
    rel_source = source.relative_to(ROOT).as_posix()
    digest = hashlib.sha256(
        ("\n\f\n".join(pages)).encode("utf-8", errors="replace")
    ).hexdigest()[:16]
    chunk_has_ocr = any(start_page <= page_no <= end_page for page_no in ocr_pages)
    fields = {
        "type": "textbook-source-chunk",
        "subject": "系统架构设计师",
        "source_kind": profile["source_kind"],
        "source_priority": profile["priority"],
        "extract_status": status,
        "ocr_fallback_used": chunk_has_ocr,
        "source_file": rel_source,
        "pdf_page_start": start_page,
        "pdf_page_end": end_page,
        "chunk_hash": digest,
        "generated_by": "scripts/extract-textbook-text.py",
    }
    frontmatter = ["---"]
    frontmatter.extend(f"{key}: {yaml_value(value)}" for key, value in fields.items())
    frontmatter.append("---")
    body = [
        *frontmatter,
        "",
        f"# {source.stem} · PDF 第 {start_page}–{end_page} 页",
        "",
        "> [!info] AI 教材原始文本层",
        "> 本文件由脚本从 PDF 文字层自动抽取并按页切分；文字层不足时可使用中文 OCR 回退。它用于检索和校验，不替代 PDF 原件；版式、图片、公式位置和表格结构可能丢失。",
        "",
        f"- **资料角色：** {profile['source_kind']}",
        f"- **使用说明：** {profile['role']}",
        f"- **原始文件：** {rel_source}",
        f"- **PDF 页码：** {start_page}–{end_page}",
        f"- **本块包含 OCR 补全：** {'是' if chunk_has_ocr else '否'}",
        "",
    ]
    for offset, page_text in enumerate(pages):
        page_no = start_page + offset
        suffix = "（OCR 补全）" if page_no in ocr_pages else ""
        body += [f"## PDF 第 {page_no} 页{suffix}", ""]
        if page_text:
            body += [page_text, ""]
        else:
            body += [
                "_本页未抽取到可用文字；可能主要是图片、扫描内容或空白页。_",
                "",
            ]
    return "\n".join(body).rstrip() + "\n"


def reset_generated_output():
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)


def write_report(rows, chunk_pages):
    counts = {}
    for row in rows:
        status = str(row["status"])
        counts[status] = counts.get(status, 0) + 1
    lines = [
        "---",
        "type: textbook-extraction-report",
        "subject: 系统架构设计师",
        "status: generated",
        "source: scripts/extract-textbook-text.py",
        "tags: [软考, 系统架构设计师, 教材, AI教材库]",
        "---",
        "",
        "# 教材抽取报告",
        "",
        "> [!info] 自动生成",
        "> 原始 PDF 仍是证据源；这里记录 AI 可读 Markdown 的抽取状态。文字抽取和 OCR 都不包含图片本身，因此遇到结构图、表格或公式异常时必须回看原 PDF。",
        "",
        "## 汇总",
        "",
        f"- 原始 PDF：**{len(rows)}** 个",
        f"- 成功可解析：**{counts.get('可解析', 0)}** 个",
        f"- 部分可解析：**{counts.get('部分可解析', 0)}** 个",
        f"- 仍需 OCR/人工处理：**{counts.get('需OCR', 0)}** 个",
        f"- LFS 原件未拉取：**{counts.get('LFS未拉取', 0)}** 个",
        f"- 抽取失败：**{counts.get('失败', 0)}** 个",
        f"- 分块大小：**{chunk_pages} 页/块**",
        "",
        "## 明细",
        "",
        "| 原始文件 | 角色 | 优先级 | 状态 | 页数 | OCR补全页 | 分块数 | 备注 |",
        "| --- | --- | ---: | --- | ---: | ---: | ---: | --- |",
    ]
    for row in rows:
        source = str(row["source"]).replace("|", "\\|")
        kind = str(row["source_kind"]).replace("|", "\\|")
        note = str(row["note"]).replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {source} | {kind} | {row['priority']} | {row['status']} | "
            f"{row['pages']} | {row['ocr_pages']} | {row['chunks']} | {note} |"
        )
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_index(rows):
    lines = [
        "---",
        "type: textbook-index",
        "subject: 系统架构设计师",
        "status: generated",
        "source: scripts/extract-textbook-text.py",
        "tags: [软考, 系统架构设计师, 教材, AI教材库]",
        "---",
        "",
        "# AI 教材索引",
        "",
        "这个索引按**用途优先级**组织 6 份资料。优先级用于 AI 发生冲突时决定先核验哪一份，不等同于对出版社、作者或官方身份的认证。",
        "",
        "## 使用顺序",
        "",
        "1. **考试范围与能力要求**：先看《系统架构第二版 大纲》。",
        "2. **概念、机制、公式与章节主干**：优先看《系统架构设计师教程第二版可搜索》。",
        "3. **文字层或页码疑点**：用《【带搜索】系统架构设计师第二版》交叉核验。",
        "4. **应试重点、记忆辅助和补充例题**：再看两本“32 小时”资料。",
        "5. **软件体系结构深挖**：最后参考《软件体系结构原理、方法与实践_第2版》。",
        "",
        "> [!warning] 冲突处理",
        "> 大纲用于裁定“考不考/要求到什么层级”；教材用于解释“是什么/怎么工作”；辅导书和扩展参考不能静默覆盖前两者。若不同资料明显冲突，必须保留差异并标记待核验。",
        "",
        "## 资料状态",
        "",
        "| 资料 | 角色 | 优先级 | 状态 | AI 文本位置 |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for row in sorted(rows, key=lambda r: -int(r["priority"])):
        source_path = Path(str(row["source"]))
        stem = source_path.stem
        ai_path = f"02、最新教材-新大纲(第二版)/AI教材库/原始文本/{stem}/"
        lines.append(
            f"| {source_path.name} | {row['source_kind']} | "
            f"{row['priority']} | {row['status']} | {ai_path} |"
        )
    lines += [
        "",
        "## 给 AI 的引用方式",
        "",
        "教材结论尽量记录到“原始文件 + PDF 页码范围”。不要把自动生成 Markdown 的行号当作原书页码；稳定定位依据是 source_file 与 pdf_page_start/pdf_page_end。",
        "",
        "ocr_fallback_used 为 true 时，说明该文本块至少有一页来自 OCR。OCR 文字仍可能存在错字，关键定义、公式和表格必须回看原 PDF。",
        "",
        "需要用教材检查或补全现有笔记时，显式读取 prompts/65-教材证据与笔记校验.md。",
    ]
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(
        description="把系统架构设计师教材 PDF 抽取为按 PDF 页码分块的 AI 可读 Markdown。"
    )
    parser.add_argument(
        "--chunk-pages",
        type=int,
        default=DEFAULT_CHUNK_PAGES,
        help=f"每个 Markdown 分块包含的 PDF 页数，默认 {DEFAULT_CHUNK_PAGES}。",
    )
    parser.add_argument(
        "--ocr-fallback",
        action="store_true",
        help="文字层不足时，对扫描页自动使用简体中文+英文 OCR。",
    )
    parser.add_argument(
        "--ocr-workers",
        type=int,
        default=DEFAULT_OCR_WORKERS,
        help=f"OCR 并发页数，默认 {DEFAULT_OCR_WORKERS}。",
    )
    parser.add_argument(
        "--ocr-dpi",
        type=int,
        default=DEFAULT_OCR_DPI,
        help=f"OCR 渲染分辨率，默认 {DEFAULT_OCR_DPI} DPI。",
    )
    args = parser.parse_args()

    if args.chunk_pages < 1 or args.chunk_pages > 50:
        print("--chunk-pages 必须在 1 到 50 之间。", file=sys.stderr)
        return 2
    if args.ocr_workers < 1 or args.ocr_workers > 4:
        print("--ocr-workers 必须在 1 到 4 之间。", file=sys.stderr)
        return 2
    if args.ocr_dpi < 120 or args.ocr_dpi > 300:
        print("--ocr-dpi 必须在 120 到 300 之间。", file=sys.stderr)
        return 2

    sources = scan_sources()
    if not sources:
        print(f"未在 {SOURCE_ROOT.relative_to(ROOT)} 找到 PDF。", file=sys.stderr)
        return 1

    reset_generated_output()
    rows = []

    for source in sources:
        profile = profile_for(source)
        rel_source = source.relative_to(ROOT).as_posix()
        row = {
            "source": rel_source,
            "source_kind": profile["source_kind"],
            "priority": profile["priority"],
            "status": "",
            "pages": 0,
            "ocr_pages": 0,
            "chunks": 0,
            "note": "",
        }

        if is_lfs_pointer(source):
            row["status"] = "LFS未拉取"
            row["note"] = "请先执行 git lfs pull；GitHub Actions 会只拉取教材目录中的 LFS PDF。"
            rows.append(row)
            print(f"[LFS未拉取] {rel_source}")
            continue

        try:
            pages = extract_pdf_pages(source)
            initial_status, initial_note = classify_extract_status(pages)
            ocr_pages = set()
            attempted = 0
            ocr_errors = []

            if args.ocr_fallback and initial_status in {"需OCR", "部分可解析"}:
                pages, ocr_pages, attempted, ocr_errors = apply_ocr_fallback(
                    source,
                    pages,
                    initial_status,
                    args.ocr_workers,
                    args.ocr_dpi,
                )

            status, final_note = classify_extract_status(pages)
            notes = []
            if ocr_pages or attempted:
                notes.append(f"OCR 尝试 {attempted} 页，采用 {len(ocr_pages)} 页结果")
            if final_note:
                notes.append(final_note)
            elif not ocr_pages and initial_note:
                notes.append(initial_note)
            if ocr_errors:
                notes.append(f"OCR 失败 {len(ocr_errors)} 页；示例：{ocr_errors[0]}")

            row["status"] = status
            row["pages"] = len(pages)
            row["ocr_pages"] = len(ocr_pages)
            row["note"] = "；".join(notes)

            out_dir = OUTPUT_ROOT / source.stem
            out_dir.mkdir(parents=True, exist_ok=True)
            chunk_count = 0
            for start_index in range(0, len(pages), args.chunk_pages):
                chunk = pages[start_index : start_index + args.chunk_pages]
                start_page = start_index + 1
                end_page = start_index + len(chunk)
                out = out_dir / f"p{start_page:04d}-p{end_page:04d}.md"
                out.write_text(
                    render_chunk(
                        source,
                        chunk,
                        start_page,
                        end_page,
                        status,
                        ocr_pages,
                    ),
                    encoding="utf-8",
                )
                chunk_count += 1

            row["chunks"] = chunk_count
            rows.append(row)
            print(
                f"[{status}] {rel_source}: {len(pages)} 页，"
                f"OCR {len(ocr_pages)} 页，{chunk_count} 块"
            )
        except Exception as exc:
            row["status"] = "失败"
            row["note"] = str(exc)
            rows.append(row)
            print(f"[失败] {rel_source}: {exc}", file=sys.stderr)

    write_report(rows, args.chunk_pages)
    write_index(rows)

    hard_failures = sum(
        1 for row in rows if row["status"] in {"失败", "LFS未拉取"}
    )
    if hard_failures:
        print(
            f"完成，但有 {hard_failures} 个文件未成功抽取。详情见 {REPORT_PATH.relative_to(ROOT)}。",
            file=sys.stderr,
        )
        return 1

    print(f"完成。详情见 {REPORT_PATH.relative_to(ROOT)}。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
