#!/usr/bin/env python3
"""Minimal static repository validator.

This intentionally uses only the Python standard library and validates source
hygiene, narrow Markdown links, Skill package shape, and public artifact
boundaries. It does not test ChatGPT runtime behavior or production readiness.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

TEXT_SUFFIXES = {
    ".md", ".py", ".yml", ".yaml", ".txt", ".json", ".toml", ".gitignore"
}
TEXT_NAMES = {".gitignore", "LICENSE", "AGENTS.md"}
IGNORED_DIRS = {".git", "__pycache__", ".idea", ".vscode"}
ARCHIVE_SUFFIXES = {".zip", ".skill"}
BINARY_DOCUMENT_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tif", ".tiff", ".pdf"
}
BINARY_DOCUMENT_ALLOWLIST: set[str] = set()
GENERATED_PACKAGE_PATHS = {"agents/openai.yaml", "assets/icon.svg"}
GENERATED_PACKAGE_ALLOWLIST: set[str] = set()
CREDENTIAL_FILENAMES = {
    ".env", "id_rsa", "id_ed25519", "credentials.json", "service-account.json"
}
CREDENTIAL_SUFFIXES = {".pem", ".key", ".p12"}
CONFLICT_RE = re.compile(r"^(<<<<<<<|=======|>>>>>>>)")
INLINE_LINK_RE = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
CODE_SPAN_RE = re.compile(r"`([^`\n]+)`")
URL_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
AI_URL_PATTERNS = [
    ("ChatGPT conversation/share URL", re.compile(r"https://chatgpt\.com/(?:c|share)/[^\s)\]>\"']+")),
    ("ChatGPT Codex task URL", re.compile(r"https://chatgpt\.com/(?:codex|tasks?)/[^\s)\]>\"']+")),
    ("OpenAI session-sharing URL", re.compile(r"https://(?:chat\.openai\.com|chatgpt\.com)/share/[^\s)\]>\"']+")),
    ("Claude conversation/share URL", re.compile(r"https://claude\.ai/(?:chat|share)/[^\s)\]>\"']+")),
]


def rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix() or "."
    except ValueError:
        return path.as_posix()


def iter_files(root: Path):
    for path in sorted(root.rglob("*"), key=lambda p: rel(p, root)):
        parts = set(path.relative_to(root).parts)
        if parts & IGNORED_DIRS:
            continue
        if path.is_file():
            yield path


def is_text_file(path: Path) -> bool:
    return path.name in TEXT_NAMES or path.suffix.lower() in TEXT_SUFFIXES


def read_text(path: Path, root: Path, errors: list[str]) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        errors.append(f"ERROR {rel(path, root)}: not readable as UTF-8 ({exc.reason})")
    except OSError as exc:
        errors.append(f"ERROR {rel(path, root)}: cannot read file ({exc})")
    return None


def check_text_hygiene(path: Path, root: Path, text: str, errors: list[str]) -> None:
    for line_no, line in enumerate(text.splitlines(), start=1):
        body = line[:-1] if line.endswith("\r") else line
        if body.endswith((" ", "\t")):
            errors.append(f"ERROR {rel(path, root)}: trailing whitespace on line {line_no}")
        if CONFLICT_RE.match(body):
            errors.append(f"ERROR {rel(path, root)}: unresolved merge-conflict marker on line {line_no}")


def without_fenced_code(text: str) -> str:
    out: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append("")
        elif in_fence:
            out.append("")
        else:
            out.append(line)
    return "\n".join(out)


def check_markdown_links(path: Path, root: Path, text: str, errors: list[str]) -> int:
    count = 0
    for match in INLINE_LINK_RE.finditer(without_fenced_code(text)):
        target = match.group(1).strip()
        split = urlsplit(target)
        if split.scheme in {"http", "https", "mailto"} or target.startswith("#"):
            continue
        if split.scheme and split.scheme not in {""}:
            continue
        cleaned = unquote(split.path)
        if not cleaned:
            continue
        resolved = (path.parent / cleaned).resolve()
        count += 1
        if not resolved.exists():
            errors.append(f"ERROR {rel(path, root)}: Markdown link target does not exist: {target}")
    return count


def discover_packages(root: Path) -> tuple[list[Path], list[Path]]:
    exp_root = root / "experiments"
    experimental = sorted([p for p in exp_root.glob("**/package") if p.is_dir()]) if exp_root.exists() else []
    skills_root = root / "skills"
    production = []
    if skills_root.exists():
        production = sorted([p for p in skills_root.iterdir() if p.is_dir() and not p.name.startswith(".")])
    return experimental, production


def read_frontmatter(skill: Path, root: Path, text: str, errors: list[str]) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        errors.append(f"ERROR {rel(skill, root)}: missing opening frontmatter delimiter")
        return {}
    closing = None
    for index, line in enumerate(lines[1:], start=1):
        if line == "---":
            closing = index
            break
    if closing is None:
        errors.append(f"ERROR {rel(skill, root)}: missing closing frontmatter delimiter")
        return {}
    data: dict[str, str] = {}
    for line in lines[1:closing]:
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"\'')
    return data


def is_package_ref(span: str) -> bool:
    if any(ch.isspace() for ch in span) or URL_RE.match(span):
        return False
    if span.startswith(("/", "#", "<", "{", "$")) or span in {"...", "???"}:
        return False
    path = Path(span)
    return not path.is_absolute() and path.suffix != "" and any(part == ".." or part for part in path.parts)


def check_package(package: Path, root: Path, errors: list[str]) -> int:
    skill = package / "SKILL.md"
    if not skill.exists():
        errors.append(f"ERROR {rel(package, root)}: missing SKILL.md")
        return 0
    text = read_text(skill, root, errors)
    if text is None:
        return 0
    fm = read_frontmatter(skill, root, text, errors)
    for key in ("name", "description"):
        if not fm.get(key):
            errors.append(f"ERROR {rel(skill, root)}: missing or empty frontmatter key: {key}")
    refs = 0
    for match in CODE_SPAN_RE.finditer(text):
        span = match.group(1)
        if not is_package_ref(span):
            continue
        refs += 1
        target = (package / span).resolve()
        try:
            target.relative_to(package.resolve())
        except ValueError:
            errors.append(f"ERROR {rel(skill, root)}: package-relative reference escapes package: {span}")
            continue
        if not target.exists():
            errors.append(f"ERROR {rel(skill, root)}: package-relative reference does not exist: {span}")
    for subdir in package.rglob("observations"):
        if subdir.is_dir():
            errors.append(f"ERROR {rel(subdir, root)}: observations directory must remain outside package directories")
    return refs


def check_artifacts(path: Path, root: Path, errors: list[str]) -> None:
    r = rel(path, root)
    suffix = path.suffix.lower()
    name = path.name
    if suffix in ARCHIVE_SUFFIXES:
        errors.append(f"ERROR {r}: prohibited archive artifact")
    if suffix in BINARY_DOCUMENT_SUFFIXES and r not in BINARY_DOCUMENT_ALLOWLIST:
        errors.append(f"ERROR {r}: prohibited binary document or screenshot artifact")
    if name in CREDENTIAL_FILENAMES or name.startswith(".env.") or suffix in CREDENTIAL_SUFFIXES:
        errors.append(f"ERROR {r}: prohibited credential-bearing filename")


def check_generated_package_files(packages: list[Path], root: Path, errors: list[str]) -> None:
    for package in packages:
        for relative in GENERATED_PACKAGE_PATHS:
            candidate = package / relative
            if candidate.exists() and rel(candidate, root) not in GENERATED_PACKAGE_ALLOWLIST:
                errors.append(f"ERROR {rel(candidate, root)}: generated platform file is not allowed in source package")


def check_ai_urls(path: Path, root: Path, text: str, errors: list[str]) -> None:
    for category, pattern in AI_URL_PATTERNS:
        if pattern.search(text):
            errors.append(f"ERROR {rel(path, root)}: prohibited {category}")


def validate(root: Path) -> tuple[list[str], dict[str, int]]:
    root = root.resolve()
    errors: list[str] = []
    counts = {"text_files": 0, "markdown_links": 0, "experimental_packages": 0, "production_packages": 0, "package_refs": 0}
    files = list(iter_files(root))
    for path in files:
        check_artifacts(path, root, errors)
        if is_text_file(path):
            counts["text_files"] += 1
            text = read_text(path, root, errors)
            if text is None:
                continue
            check_text_hygiene(path, root, text, errors)
            check_ai_urls(path, root, text, errors)
            if path.suffix.lower() == ".md":
                counts["markdown_links"] += check_markdown_links(path, root, text, errors)
    experimental, production = discover_packages(root)
    counts["experimental_packages"] = len(experimental)
    counts["production_packages"] = len(production)
    for package in experimental + production:
        counts["package_refs"] += check_package(package, root, errors)
    check_generated_package_files(experimental + production, root, errors)
    return sorted(errors), counts


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate static repository hygiene and Skill package boundaries.")
    parser.add_argument("--root", type=Path, help="temporary repository root to validate")
    args = parser.parse_args(argv)
    root = args.root.resolve() if args.root else Path(__file__).resolve().parents[1]
    errors, counts = validate(root)
    if errors:
        for error in errors:
            print(error)
        print(f"\nRepository validation failed with {len(errors)} error(s).")
        return 1
    print(
        "Repository validation passed: "
        f"{counts['text_files']} text files, "
        f"{counts['markdown_links']} Markdown links, "
        f"{counts['experimental_packages']} experimental Skill packages, "
        f"{counts['production_packages']} production Skill packages, "
        f"{counts['package_refs']} package file references."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
