#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "历年真题"
AI_ROOT = SOURCE_ROOT / "AI题库"
OUTPUT_ROOT = AI_ROOT / "原始文本"
REPORT_PATH = AI_ROOT / "抽取报告.md"

LFS_SIGNATURE = b"version https://git-lfs.github.com/spec/v1"
SUPPORTED_SUFFIXES = {".pdf", ".docx"}
MIN_USEFUL_TEXT = 500


def yaml_value(value: object) -> str:
    if value is None:
        return '""'
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)


def is_lfs_pointer(path: Path) -> bool:
    try:
        return LFS_SIGNATURE in path.read_bytes()[:256]
    except OSError:
        return False


def extract_pdf(path: Path) -> str:
    if shutil.which("pdftotext") is None:
        raise RuntimeError(
            "未找到 pdftotext。macOS 可执行 `brew install poppler`；"
            "GitHub Actions 会自动安装 poppler-utils。"
        )
    proc = subprocess.run(
        ["pdftotext", "-layout", "-enc", "UTF-8", str(path), "-"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        err = proc.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(err or f"pdftotext 退出码 {proc.returncode}")
    return proc.stdout.decode("utf-8", errors="replace")


def extract_docx(path: Path) -> str:
    with zipfile.ZipFile(path) as zf:
        try:
            xml = zf.read("word/document.xml")
        except KeyError as exc:
            raise RuntimeError("DOCX 中缺少 word/document.xml") from exc

    root = ET.fromstring(xml)
    w = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    lines: list[str] = []
    for paragraph in root.iter(f"{w}p"):
        parts = [node.text or "" for node in paragraph.iter(f"{w}t")]
        text = "".join(parts).strip()
        if text:
            lines.append(text)
    return "\n".join(lines)


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\f", "\n\n<!-- PDF_PAGE_BREAK -->\n\n")
    lines = [line.rstrip() for line in text.splitlines()]
    out: list[str] = []
    blank = 0
    for line in lines:
        if line.strip():
            blank = 0
            out.append(line)
        else:
            blank += 1
            if blank <= 2:
                out.append("")
    return "\n".join(out).strip()


def infer_metadata(rel: Path) -> dict[str, object]:
    text = rel.as_posix()
    year_match = re.search(r"(20\d{2})", text)
    year = int(year_match.group(1)) if year_match else ""

    if "上半年" in text or re.search(r"(^|[^0-9])5月", text):
        session = "上半年"
    elif "下半年" in text or re.search(r"(^|[^0-9])11月", text):
        session = "下半年"
    else:
        session = "未标明"

    filename = rel.name
    if "综合知识" in filename or "科目一" in filename:
        paper = "综合知识"
    elif "案例分析" in filename or "科目二" in filename:
        paper = "案例分析"
    elif "论文" in filename or "科目三" in filename:
        paper = "论文"
    elif "答案" in filename or "解析" in filename:
        paper = "答案/解析"
    else:
        paper = "综合资料"

    if "回忆" in text:
        source_kind = "回忆版"
    elif "网友" in text:
        source_kind = "网友版"
    elif "整理" in text or "分享" in text:
        source_kind = "整理版"
    elif re.search(r"真题及解析|答案详解", text):
        source_kind = "真题解析资料（来源待核验）"
    else:
        source_kind = "资料版（来源待核验）"

    return {
        "year": year,
        "session": session,
        "paper": paper,
        "source_kind": source_kind,
    }


def output_path_for(source: Path) -> Path:
    rel = source.relative_to(SOURCE_ROOT)
    return OUTPUT_ROOT / rel.parent / f"{source.stem}.md"


def render_markdown(source: Path, extracted: str, status: str, error: str = "") -> str:
    rel = source.relative_to(ROOT)
    meta = infer_metadata(source.relative_to(SOURCE_ROOT))
    title = source.stem

    fields = {
        "type": "exam-source",
        "subject": "系统架构设计师",
        "year": meta["year"],
        "session": meta["session"],
        "paper": meta["paper"],
        "source_kind": meta["source_kind"],
        "extract_status": status,
        "source_file": rel.as_posix(),
        "generated_by": "scripts/extract-exam-text.py",
    }

    frontmatter = ["---"]
    frontmatter.extend(f"{key}: {yaml_value(value)}" for key, value in fields.items())
    frontmatter.append("---")

    notice = (
        "> [!info] AI 原始抽取层\n"
        "> 本文件由脚本从原始真题自动抽取，**不是标准答案或最终题库**。"
        "回忆版、网友版、整理版内容必须保留来源属性；后续解析时不得杜撰官方出处。"
    )

    body = [
        *frontmatter,
        "",
        f"# {title}",
        "",
        notice,
        "",
    ]

    if error:
        body += [
            "> [!warning] 抽取失败",
            f"> {error}",
            "",
        ]

    if status == "需OCR":
        body += [
            "> [!warning] 可能是扫描版 PDF",
            "> 当前可提取文字过少。请先做 OCR，再重新运行抽取脚本；不要把空白抽取结果当成题目缺失。",
            "",
        ]

    body += ["## 抽取文本", "", extracted or "_暂无可用文本。_", ""]
    return "\n".join(body)


def scan_sources() -> list[Path]:
    if not SOURCE_ROOT.exists():
        return []
    files: list[Path] = []
    for path in SOURCE_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if AI_ROOT in path.parents:
            continue
        if path.suffix.lower() in SUPPORTED_SUFFIXES:
            files.append(path)
    return sorted(files, key=lambda p: p.as_posix())


def prune_stale(expected: set[Path]) -> list[Path]:
    removed: list[Path] = []
    if not OUTPUT_ROOT.exists():
        return removed
    for path in OUTPUT_ROOT.rglob("*.md"):
        if path in expected:
            continue
        try:
            head = path.read_text(encoding="utf-8", errors="ignore")[:1000]
        except OSError:
            continue
        if 'generated_by: "scripts/extract-exam-text.py"' in head:
            path.unlink()
            removed.append(path)
    return removed


def write_report(rows: list[dict[str, str]], removed: list[Path]) -> None:
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1

    lines = [
        "---",
        "type: exam-extraction-report",
        "subject: 系统架构设计师",
        "status: generated",
        "source: scripts/extract-exam-text.py",
        "tags: [软考, 系统架构设计师, 历年真题, AI题库]",
        "---",
        "",
        "# 历年真题抽取报告",
        "",
        "> [!info] 自动生成",
        "> 此文件由 `scripts/extract-exam-text.py` 生成。原始 PDF/DOCX 仍是证据源；本报告只记录 AI 可读文本层的抽取状态。",
        "",
        "## 汇总",
        "",
        f"- 原始资料：**{len(rows)}** 个",
        f"- 成功可解析：**{counts.get('可解析', 0)}** 个",
        f"- 可能需要 OCR：**{counts.get('需OCR', 0)}** 个",
        f"- LFS 原件未拉取：**{counts.get('LFS未拉取', 0)}** 个",
        f"- 抽取失败：**{counts.get('失败', 0)}** 个",
        f"- 本次清理过期生成文件：**{len(removed)}** 个",
        "",
        "## 明细",
        "",
        "| 原始文件 | 状态 | AI 文本 | 备注 |",
        "| --- | --- | --- | --- |",
    ]

    for row in rows:
        source = row["source"].replace("|", "\\|")
        output = row["output"].replace("|", "\\|")
        note = row["note"].replace("|", "\\|").replace("\n", " ")
        lines.append(f"| `{source}` | {row['status']} | `{output}` | {note} |")

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="把历年真题 PDF/DOCX 抽取为 AI 可读 Markdown。")
    parser.add_argument(
        "--no-prune",
        action="store_true",
        help="不清理已不存在来源所对应的自动生成 Markdown。",
    )
    args = parser.parse_args()

    sources = scan_sources()
    if not sources:
        print("未找到历年真题 PDF/DOCX。", file=sys.stderr)
        return 1

    rows: list[dict[str, str]] = []
    expected: set[Path] = set()

    for source in sources:
        out = output_path_for(source)
        expected.add(out)
        out.parent.mkdir(parents=True, exist_ok=True)
        rel_source = source.relative_to(ROOT).as_posix()
        rel_out = out.relative_to(ROOT).as_posix()

        if is_lfs_pointer(source):
            status = "LFS未拉取"
            note = "请执行 git lfs pull；GitHub Actions 会自动拉取 LFS。"
            markdown = render_markdown(source, "", status, note)
        else:
            try:
                if source.suffix.lower() == ".pdf":
                    raw = extract_pdf(source)
                else:
                    raw = extract_docx(source)
                text = normalize_text(raw)
                if len(re.sub(r"\s+", "", text)) < MIN_USEFUL_TEXT:
                    status = "需OCR"
                    note = "可提取文字过少，疑似扫描版或文字层异常。"
                else:
                    status = "可解析"
                    note = ""
                markdown = render_markdown(source, text, status)
            except Exception as exc:
                status = "失败"
                note = str(exc)
                markdown = render_markdown(source, "", status, note)

        out.write_text(markdown, encoding="utf-8")
        rows.append(
            {
                "source": rel_source,
                "status": status,
                "output": rel_out,
                "note": note,
            }
        )
        print(f"[{status}] {rel_source}")

    removed = [] if args.no_prune else prune_stale(expected)
    write_report(rows, removed)

    hard_failures = sum(1 for row in rows if row["status"] in {"失败", "LFS未拉取"})
    if hard_failures:
        print(
            f"完成，但有 {hard_failures} 个文件未成功抽取。详情见 {REPORT_PATH.relative_to(ROOT)}。",
            file=sys.stderr,
        )
    else:
        print(f"完成。详情见 {REPORT_PATH.relative_to(ROOT)}。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
