import unittest
from PIL import Image

from image_flip import flip_left_right


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


if __name__ == "__main__":
    unittest.main()
