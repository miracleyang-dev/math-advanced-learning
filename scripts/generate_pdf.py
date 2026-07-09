#!/usr/bin/env python3
"""
将 HTML 讲义（含 MathJax 公式）渲染为 PDF。

依赖：
    pip install playwright
    python -m playwright install chromium

用法：
    python scripts/generate_pdf.py functional-analysis/src/lecture-01.html
    python scripts/generate_pdf.py functional-analysis/src/lecture-01.html -o output.pdf
"""

import argparse
import asyncio
import sys
from pathlib import Path
from typing import Optional


async def html_to_pdf(html_path: str, output_path: Optional[str] = None):
    try:
        from playwright.async_api import Error as PlaywrightError
        from playwright.async_api import async_playwright
    except ImportError:
        print(
            "Error: Playwright is not installed.\n"
            "Run in Windows cmd:\n"
            "  py -m pip install playwright\n"
            "  py -m playwright install chromium",
            file=sys.stderr,
        )
        sys.exit(1)

    input_path = Path(html_path).resolve()
    if not input_path.exists():
        print(f"Error: {input_path} not found", file=sys.stderr)
        sys.exit(1)

    if output_path is None:
        pdf_path = input_path.with_suffix(".pdf")
    else:
        pdf_path = Path(output_path).resolve()

    print(f"Input:  {input_path}")
    print(f"Output: {pdf_path}")

    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch()
        except PlaywrightError:
            print(
                "Error: Playwright Chromium is not installed or cannot be launched.\n"
                "Run in Windows cmd:\n"
                "  py -m playwright install chromium",
                file=sys.stderr,
            )
            sys.exit(1)
        page = await browser.new_page()

        await page.goto(input_path.as_uri(), wait_until="networkidle")
        await page.wait_for_timeout(5000)

        # Wait for MathJax rendering
        try:
            await page.wait_for_function(
                "typeof MathJax !== 'undefined' && MathJax.startup && MathJax.startup.promise",
                timeout=15000,
            )
            await page.evaluate("MathJax.startup.promise")
        except Exception:
            print("Warning: MathJax wait timed out, proceeding anyway", file=sys.stderr)

        await page.wait_for_timeout(2000)

        await page.pdf(
            path=str(pdf_path),
            format="A4",
            margin={"top": "20mm", "bottom": "22mm", "left": "22mm", "right": "22mm"},
            print_background=True,
        )

        await browser.close()
        print(f"Done. ({pdf_path.stat().st_size / 1024:.0f} KB)")


def main():
    parser = argparse.ArgumentParser(description="Render HTML lecture notes to PDF")
    parser.add_argument("input", help="Path to HTML file")
    parser.add_argument("-o", "--output", help="Output PDF path (default: same name .pdf)")
    args = parser.parse_args()

    asyncio.run(html_to_pdf(args.input, args.output))


if __name__ == "__main__":
    main()
