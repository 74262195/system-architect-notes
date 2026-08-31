import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const ignoredDirs = new Set(['.git', '.obsidian', '.trash', '.opencode', '.claudian', '.makemd', '.space']);
const walk = (dir) => fs.readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
  if (e.isDirectory() && ignoredDirs.has(e.name)) return [];
  const p = path.join(dir, e.name);
  return e.isDirectory() ? walk(p) : [p];
});
const allFiles = walk(root);
const files = allFiles.filter((p) => p.endsWith('.md'));
const names = new Set(allFiles.map((p) => path.basename(p).replace(/\.(md|excalidraw|pdf|docx|png|jpg|jpeg|svg)$/i, '')));
const errors = [];
const warnings = [];
const aliases = new Map();

for (const file of files) {
  const text = fs.readFileSync(file, 'utf8');
  const rel = path.relative(root, file);
  if (/^(00_索引|01_综合知识|02_案例分析|03_论文素材|04_真题错题|05_画图素材)\//.test(rel) &&
      (!text.startsWith('---\n') ||
       !/^type:/m.test(text.slice(0, text.indexOf('\n---', 4))) ||
       !/^subject:/m.test(text.slice(0, text.indexOf('\n---', 4))))) {
    warnings.push(`${rel}: frontmatter 缺少 type 或 subject`);
  }

  if (!rel.startsWith('prompts/')) {
    for (const match of text.matchAll(/\[\[([^\]]+)\]\]/g)) {
      const target = match[1].split('|')[0].split('#')[0].trim();
      if (target && !names.has(path.basename(target).replace(/\.(md|excalidraw|pdf|docx|png|jpg|jpeg|svg)$/i, ''))) {
        warnings.push(`${rel}: 失效链接 ${target}`);
      }
    }
  }

  const fm = text.startsWith('---\n') ? text.slice(4, text.indexOf('\n---', 4)) : '';
  const line = fm.match(/^aliases:\s*\[([^\]]*)\]/m);
  if (line) for (const alias of line[1].split(',').map((x) => x.trim()).filter(Boolean)) {
    const owners = aliases.get(alias) ?? [];
    owners.push(rel);
    aliases.set(alias, owners);
  }

  if (/wechat-sync-auth|BEGIN (RSA|OPENSSH|PRIVATE) KEY|gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}/i.test(text)) {
    errors.push(`${rel}: 疑似认证信息`);
  }
}

for (const [alias, owners] of aliases) {
  if (owners.length > 1) warnings.push(`重复 aliases ${alias}: ${owners.join(' | ')}`);
}

if (errors.length) {
  console.error(errors.join('\n'));
  process.exit(1);
}

console.log(`OK: ${files.length} 个 Markdown 文件通过检查`);
if (warnings.length) {
  console.warn(`WARN: ${warnings.length} 个历史资料问题未阻断提交`);
  console.warn(warnings.join("\n"));
}
