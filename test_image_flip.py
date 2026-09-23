import tempfile
import unittest
from pathlib import Path

from PIL import Image

from image_flip import create_comparison_page, flip_left_right


class TestImageFlip(unittest.TestCase):
    def test_flip_left_right_reverses_columns(self):
        img = Image.new("RGB", (3, 2), color="white")
        img.putpixel((0, 0), (255, 0, 0))
        img.putpixel((1, 0), (0, 255, 0))
        img.putpixel((2, 0), (0, 0, 255))
        img.putpixel((0, 1), (255, 255, 0))
        img.putpixel((1, 1), (0, 255, 255))
        img.putpixel((2, 1), (255, 0, 255))

        flipped = flip_left_right(img)

        self.assertEqual(flipped.size, img.size)
        self.assertEqual(flipped.getpixel((0, 0)), (0, 0, 255))
        self.assertEqual(flipped.getpixel((1, 0)), (0, 255, 0))
        self.assertEqual(flipped.getpixel((2, 0)), (255, 0, 0))
        self.assertEqual(flipped.getpixel((0, 1)), (255, 0, 255))
        self.assertEqual(flipped.getpixel((1, 1)), (0, 255, 255))
        self.assertEqual(flipped.getpixel((2, 1)), (255, 255, 0))

    def test_create_comparison_page_saves_output(self):
        img1 = Image.new("RGB", (20, 10), color="red")
        img2 = Image.new("RGB", (20, 10), color="blue")

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "comparison.png"
            saved = create_comparison_page([(img1, img2)], output_path)
            self.assertTrue(saved.exists())
            self.assertGreater(Image.open(saved).size[0], 0)
            self.assertGreater(Image.open(saved).size[1], 0)


if __name__ == "__main__":
    unittest.main()
