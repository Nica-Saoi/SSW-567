import unittest
from triangle import classify_triangle

class TestTriangle(unittest.TestCase):
    """Test cases for the classify_triangle function."""

    def test_equilateral(self):
        self.assertEqual(classify_triangle(2, 2, 2), "Equilateral")
        self.assertNotEqual(classify_triangle(1, 2, 3), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(2, 2, 3), "Isosceles")
        self.assertNotEqual(classify_triangle(2, 3, 4), "Isosceles")

    def test_scalene_and_right(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right")
        self.assertNotEqual(classify_triangle(4, 4, 4), "Scalene and Right")
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")


    def test_invalid(self):
        self.assertEqual(classify_triangle(100, 2, 0), "Not a Triangle")

if __name__ == "__main__":
    unittest.main(exit=False)

    print("\nCompleted triangle tests.")
