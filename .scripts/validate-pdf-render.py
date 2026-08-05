#!/usr/bin/env python3
"""Fail when important pages in the 2025 PDF cannot be rendered."""

import subprocess
import tempfile
from pathlib import Path


PDF = Path("assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf")
PAGES = range(39, 46)
MIN_DARK_PIXEL_RATIO = 0.05


def dark_pixel_ratio(ppm_path: Path) -> float:
    data = ppm_path.read_bytes()
    try:
        _, pixels = data.split(b"\n255\n", 1)
    except ValueError as error:
        raise RuntimeError(f"{ppm_path} is not a supported binary PPM") from error

    pixel_count = len(pixels) // 3
    dark_pixels = sum(
        min(pixels[offset : offset + 3]) < 235
        for offset in range(0, len(pixels), 3)
    )
    return dark_pixels / pixel_count


def main() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        output_dir = Path(temp_dir)
        failures = []

        for page in PAGES:
            output_prefix = output_dir / f"page-{page}"
            result = subprocess.run(
                [
                    "pdftoppm",
                    "-f",
                    str(page),
                    "-l",
                    str(page),
                    "-r",
                    "36",
                    "-singlefile",
                    str(PDF),
                    str(output_prefix),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            ratio = dark_pixel_ratio(output_prefix.with_suffix(".ppm"))

            if result.returncode or result.stderr.strip():
                failures.append(
                    f"page {page} produced renderer errors: {result.stderr.strip()}"
                )
            if ratio < MIN_DARK_PIXEL_RATIO:
                failures.append(
                    f"page {page} appears blank ({ratio:.2%} dark pixels)"
                )

        if failures:
            raise SystemExit("\n".join(failures))

        print(f"Validated pages {PAGES.start}-{PAGES.stop - 1} in {PDF}")


if __name__ == "__main__":
    main()
