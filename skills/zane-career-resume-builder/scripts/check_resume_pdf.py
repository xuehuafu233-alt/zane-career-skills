#!/usr/bin/env python3
"""Run structural checks on a resume PDF; never replace visual QA."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:  # Optional; a Poppler fallback is available below.
    PdfReader = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--pages", type=int, default=None,
                        help="Expected page count. Omit when the project contract does not fix it.")
    parser.add_argument("--require", action="append", default=[])
    parser.add_argument("--forbid", action="append", default=[])
    parser.add_argument("--require-link", action="store_true")
    parser.add_argument("--a4-tolerance", type=float, default=3.0,
                        help="Allowed page-size difference in PDF points.")
    return parser.parse_args()


def annotation_subtype(annotation) -> str:
    try:
        return str(annotation.get_object().get("/Subtype", ""))
    except Exception:
        return ""


def run_pdfinfo(pdf: Path, *options: str) -> str:
    result = subprocess.run(
        ["pdfinfo", *options, str(pdf)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "pdfinfo failed")
    return result.stdout


def fallback_with_pdfinfo(args: argparse.Namespace) -> int:
    """Run a transparent, narrower check when pypdf is unavailable."""
    if shutil.which("pdfinfo") is None:
        print(
            "BLOCKED: install pypdf or provide Poppler pdfinfo; no PDF parser is available",
            file=sys.stderr,
        )
        return 2

    errors: list[str] = []
    limitations: list[str] = []
    try:
        info = run_pdfinfo(args.pdf, "-box")
        struct_text = run_pdfinfo(args.pdf, "-struct-text")
        urls = run_pdfinfo(args.pdf, "-url")
    except Exception as exc:
        print(f"FAIL: pdfinfo fallback cannot inspect PDF: {exc}", file=sys.stderr)
        return 2

    page_match = re.search(r"^Pages:\s+(\d+)", info, re.MULTILINE)
    if not page_match:
        errors.append("cannot determine page count with pdfinfo")
        page_count = 0
    else:
        page_count = int(page_match.group(1))
        if args.pages is not None and page_count != args.pages:
            errors.append(f"expected {args.pages} pages, found {page_count}")

    size_matches = re.findall(
        r"^(?:Page(?:\s+\d+)? size):\s+([\d.]+) x ([\d.]+) pts",
        info,
        re.MULTILINE,
    )
    if not size_matches:
        errors.append("cannot determine page size with pdfinfo")
    else:
        a4_width, a4_height = 595.276, 841.890
        for index, (width_raw, height_raw) in enumerate(size_matches, start=1):
            width, height = float(width_raw), float(height_raw)
            if not (abs(width - a4_width) <= args.a4_tolerance and
                    abs(height - a4_height) <= args.a4_tolerance):
                errors.append(
                    f"page {index} is not portrait A4: {width:.1f} x {height:.1f} pt"
                )

    if not struct_text.strip():
        errors.append("PDF has no tagged extractable text in pdfinfo fallback")
    for phrase in args.require:
        if phrase not in struct_text:
            errors.append(f"required text missing in tagged-text fallback: {phrase!r}")
    for phrase in args.forbid:
        if phrase in struct_text:
            errors.append(f"forbidden text present: {phrase!r}")

    url_lines = [line for line in urls.splitlines() if re.search(r"https?://|mailto:|tel:", line)]
    if args.require_link and not url_lines:
        errors.append("no URL found by pdfinfo -url")
    limitations.append("fallback uses tagged structure text; character extraction may differ from pypdf")

    if errors:
        print("FAIL (pdfinfo fallback)")
        for error in errors:
            print(f"- {error}")
        for limitation in limitations:
            print(f"- limitation: {limitation}")
        return 1

    print(f"PASS WITH LIMITATIONS: {args.pdf}")
    print(f"- pages: {page_count} portrait A4")
    print(f"- URL objects: {len(url_lines)}")
    for limitation in limitations:
        print(f"- limitation: {limitation}")
    print("- structural checks only; render and review every page as continuous reading bands")
    return 0


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    if not args.pdf.is_file():
        print(f"FAIL: file not found: {args.pdf}", file=sys.stderr)
        return 2


    if PdfReader is None:
        return fallback_with_pdfinfo(args)

    try:
        reader = PdfReader(str(args.pdf))
    except Exception as exc:
        print(f"FAIL: cannot open PDF: {exc}", file=sys.stderr)
        return 2

    if args.pages is not None and len(reader.pages) != args.pages:
        errors.append(f"expected {args.pages} pages, found {len(reader.pages)}")

    texts: list[str] = []
    link_count = 0
    a4_width, a4_height = 595.276, 841.890
    for index, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        is_a4 = (abs(width - a4_width) <= args.a4_tolerance and
                 abs(height - a4_height) <= args.a4_tolerance)
        if not is_a4:
            errors.append(f"page {index} is not portrait A4: {width:.1f} x {height:.1f} pt")
        text = page.extract_text() or ""
        texts.append(text)
        if not text.strip():
            errors.append(f"page {index} has no extractable text")
        for annotation in page.get("/Annots", []):
            if annotation_subtype(annotation) == "/Link":
                link_count += 1

    full_text = "\n".join(texts)
    for phrase in args.require:
        if phrase not in full_text:
            errors.append(f"required text missing: {phrase!r}")
    for phrase in args.forbid:
        if phrase in full_text:
            errors.append(f"forbidden text present: {phrase!r}")
    if args.require_link and link_count == 0:
        errors.append("no PDF link annotation found")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: {args.pdf}")
    print(f"- pages: {len(reader.pages)} portrait A4")
    print(f"- extractable characters: {len(full_text.strip())}")
    print(f"- link annotations: {link_count}")
    print("- structural checks only; render and review every page as continuous reading bands")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
