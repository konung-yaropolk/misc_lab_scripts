#!/usr/bin/env python3
"""
png_diff.py — pixel-level diff between two folders of PNGs.

For each matching filename:
  - Image A → grayscale → magenta channel  (R=gray, G=0,   B=gray)
  - Image B → grayscale → green channel   (R=0,    G=gray, B=0)
  - Composite = A_magenta + B_green (clamped to 255)

Result:
  - Perfect overlap  → neutral gray  (equal R, G, B)
  - Only in A        → magenta tint
  - Only in B        → green tint
  - Partial overlap  → color shift proportional to the diff

With --include-unmatched, files present in only one folder are also written
to the output, rendered entirely in their respective color (magenta for A,
green for B), as if the other image were pure black.

Usage:
    python png_diff.py <folder_a> <folder_b> <output_folder>
    python png_diff.py <folder_a> <folder_b> <output_folder> --include-unmatched
"""

import sys
import argparse
from pathlib import Path

import numpy as np
from PIL import Image


def to_magenta(gray: np.ndarray) -> np.ndarray:
    """Convert HxW uint8 grayscale array to HxWx3 magenta image."""
    out = np.zeros((*gray.shape, 3), dtype=np.uint8)
    out[:, :, 0] = gray  # R
    out[:, :, 1] = 0     # G
    out[:, :, 2] = gray  # B
    return out


def to_green(gray: np.ndarray) -> np.ndarray:
    """Convert HxW uint8 grayscale array to HxWx3 green image."""
    out = np.zeros((*gray.shape, 3), dtype=np.uint8)
    out[:, :, 0] = 0     # R
    out[:, :, 1] = gray  # G
    out[:, :, 2] = 0     # B
    return out


def flatten(img: Image.Image) -> Image.Image:
    """Flatten alpha onto a white background, return RGB image."""
    bg = Image.new("RGB", img.size, (255, 255, 255))
    bg.paste(img, mask=img.split()[3])
    return bg


def load_gray(path: Path) -> np.ndarray:
    """Load a PNG as a HxW uint8 grayscale array."""
    return np.array(flatten(Image.open(path).convert("RGBA")).convert("L"))


def diff_pair(
    path_a: Path | None,
    path_b: Path | None,
    path_out: Path,
) -> None:
    """
    Composite path_a (magenta) and path_b (green).
    Either path may be None, in which case that channel is treated as black
    and the result is the solo image rendered in its own color.
    """
    assert path_a is not None or path_b is not None

    if path_a is not None and path_b is not None:
        gray_a = load_gray(path_a)
        gray_b = load_gray(path_b)

        # Resize B to match A if sizes differ
        if gray_a.shape != gray_b.shape:
            h, w = gray_a.shape
            print(f"  [warn] size mismatch — resizing B to match A ({w}×{h})")
            gray_b = np.array(
                Image.fromarray(gray_b).resize((w, h), Image.LANCZOS)
            )

    elif path_a is not None:
        gray_a = load_gray(path_a)
        gray_b = np.zeros_like(gray_a)
    else:
        gray_b = load_gray(path_b)
        gray_a = np.zeros_like(gray_b)

    magenta = to_magenta(gray_a).astype(np.uint16)
    green   = to_green(gray_b).astype(np.uint16)

    composite = np.clip(magenta + green, 0, 255).astype(np.uint8)
    Image.fromarray(composite, "RGB").save(path_out)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Per-pixel diff of two PNG folders via magenta/green compositing."
    )
    parser.add_argument("folder_a", type=Path, help="First input folder")
    parser.add_argument("folder_b", type=Path, help="Second input folder")
    parser.add_argument("output",   type=Path, help="Output folder")
    parser.add_argument(
        "--missing", choices=["skip", "warn", "error"], default="warn",
        help="How to handle unmatched files when --include-unmatched is NOT set (default: warn)"
    )
    parser.add_argument(
        "--include-unmatched", action="store_true",
        help=(
            "Also output files present in only one folder, rendered entirely "
            "in their color (magenta for A-only, green for B-only)"
        ),
    )
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)

    files_a = {p.name for p in args.folder_a.glob("*.png")}
    files_b = {p.name for p in args.folder_b.glob("*.png")}

    common = sorted(files_a & files_b)
    only_a = sorted(files_a - files_b)
    only_b = sorted(files_b - files_a)

    # ── Report / handle unmatched ──────────────────────────────────────────
    if (only_a or only_b) and not args.include_unmatched:
        msg = f"Unmatched files — only in A: {only_a}, only in B: {only_b}"
        if args.missing == "error":
            sys.exit(f"[error] {msg}")
        elif args.missing == "warn":
            print(f"[warn]  {msg}")

    if not common and not args.include_unmatched:
        sys.exit("[error] No matching PNG filenames found between the two folders.")

    # ── Build work list ────────────────────────────────────────────────────
    # Each entry: (name, path_a_or_None, path_b_or_None, label)
    work: list[tuple[str, Path | None, Path | None, str]] = []

    for name in common:
        work.append((name, args.folder_a / name, args.folder_b / name, "diff"))

    if args.include_unmatched:
        for name in only_a:
            work.append((name, args.folder_a / name, None, "A-only → magenta"))
        for name in only_b:
            work.append((name, None, args.folder_b / name, "B-only → green"))

    if not work:
        sys.exit("[error] Nothing to process.")

    # ── Process ────────────────────────────────────────────────────────────
    print(f"Processing {len(work)} file(s)…")
    for name, pa, pb, label in sorted(work, key=lambda t: t[0]):
        print(f"  {name}  [{label}]")
        diff_pair(pa, pb, args.output / name)

    print(f"Done. Results written to: {args.output}")


if __name__ == "__main__":
    main()