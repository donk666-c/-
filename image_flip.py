from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image
import matplotlib.pyplot as plt


VALID_EXTENSIONS = {".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tif", ".tiff", ".webp"}


def flip_left_right(image: Image.Image) -> Image.Image:
    """Return a new image flipped horizontally (left-right)."""
    if not isinstance(image, Image.Image):
        raise TypeError("image must be a PIL Image object")

    return image.transpose(Image.FLIP_LEFT_RIGHT)


def create_demo_image(path: str | Path) -> Image.Image:
    """Create a colorful sample image for quick testing."""
    sample = Image.new("RGB", (300, 180), color=(240, 240, 240))
    for x in range(0, 300, 30):
        for y in range(0, 180, 30):
            sample.putpixel((x, y), ((x * 2) % 256, (y * 3) % 256, (x + y) % 256))
    sample.save(path)
    return sample


def show_original_and_flipped(image: Image.Image | str | Path, output_path: str | Path | None = None) -> Image.Image:
    """Display the original and flipped versions side by side.

    When a graphical display is available, both images are shown on screen.
    In headless environments, the comparison is saved to a file instead.
    """
    if isinstance(image, (str, Path)):
        original = Image.open(image).copy()
    elif isinstance(image, Image.Image):
        original = image.copy()
    else:
        raise TypeError("image must be a PIL Image, str path, or pathlib.Path")

    flipped = flip_left_right(original)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(original)
    axes[0].set_title("Original")
    axes[0].axis("off")

    axes[1].imshow(flipped)
    axes[1].set_title("Left-Right Flipped")
    axes[1].axis("off")

    plt.tight_layout()

    if output_path is not None:
        flipped.save(output_path)

    try:
        plt.show()
    except Exception:
        fallback_path = Path(output_path) if output_path is not None else Path("comparison.png")
        fig.savefig(fallback_path.with_suffix(".png"), dpi=150)
        print(f"No display detected; saved comparison image to: {fallback_path.with_suffix('.png')}")
    finally:
        plt.close(fig)

    return flipped


def process_batch(input_dir: str | Path, output_dir: str | Path) -> list[Path]:
    """Flip every supported image in a directory and save them to the output directory."""
    source_dir = Path(input_dir)
    target_dir = Path(output_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    processed: list[Path] = []
    for image_path in sorted(source_dir.iterdir()):
        if image_path.is_file() and image_path.suffix.lower() in VALID_EXTENSIONS:
            img = Image.open(image_path)
            flipped = flip_left_right(img)
            output_path = target_dir / f"{image_path.stem}_flipped{image_path.suffix}"
            flipped.save(output_path)
            processed.append(output_path)
            print(f"Processed: {image_path.name} -> {output_path.name}")

    return processed


def main() -> None:
    parser = argparse.ArgumentParser(description="Flip an image left-right, display original + flipped versions, or process a folder of images.")
    parser.add_argument("input_path", nargs="?", default="sample_input.png", help="Path to a single image or a directory of images")
    parser.add_argument("-o", "--output", default=None, help="Output path for a single image or output folder for batch mode")
    args = parser.parse_args()

    input_path = Path(args.input_path)

    if input_path.is_dir():
        if args.output is None:
            output_dir = input_path / "flipped"
        else:
            output_dir = Path(args.output)
        results = process_batch(input_path, output_dir)
        print(f"Batch complete. {len(results)} images processed and saved to {output_dir}")
        return

    if not input_path.exists():
        input_path = Path("sample_input.png")
        create_demo_image(input_path)
        print(f"No input image found. Created demo image: {input_path}")

    output_path = args.output or "flipped_output.png"
    original = Image.open(input_path)
    flipped = show_original_and_flipped(original, output_path=output_path)
    print(f"Flipped image saved to: {output_path}")
    print(f"Original size: {original.size}, Flipped size: {flipped.size}")


if __name__ == "__main__":
    main()
