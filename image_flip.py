from __future__ import annotations

from pathlib import Path

from PIL import Image
import matplotlib.pyplot as plt


def flip_left_right(image: Image.Image) -> Image.Image:
    """Return a new image flipped horizontally (left-right)."""
    if not isinstance(image, Image.Image):
        raise TypeError("image must be a PIL Image object")

    return image.transpose(Image.FLIP_LEFT_RIGHT)


def show_original_and_flipped(image: Image.Image | str | Path) -> Image.Image:
    """Display the original image and the horizontally flipped version side by side.

    The function accepts either a PIL image or a path to an image file.
    """
    if isinstance(image, (str, Path)):
        loaded = Image.open(image)
        original = loaded.copy()
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
    plt.show()
    return flipped


if __name__ == "__main__":
    sample_path = Path("sample_input.png")
    if not sample_path.exists():
        sample = Image.new("RGB", (300, 180), color=(240, 240, 240))
        for x in range(0, 300, 30):
            for y in range(0, 180, 30):
                sample.putpixel((x, y), ((x * 2) % 256, (y * 3) % 256, (x + y) % 256))
        sample.save(sample_path)

    show_original_and_flipped(sample_path)
