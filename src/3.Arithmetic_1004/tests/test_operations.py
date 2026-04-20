"""arithmetic.operations 단위 테스트."""

import unittest

from arithmetic.operations import add, divide, multiply, subtract


class TestAdd(unittest.TestCase):
    def test_integers(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_floats(self) -> None:
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)


class TestSubtract(unittest.TestCase):
    def test_positive_result(self) -> None:
        self.assertEqual(subtract(5, 2), 3)

    def test_negative_result(self) -> None:
        self.assertEqual(subtract(2, 5), -3)


class TestMultiply(unittest.TestCase):
    def test_basic(self) -> None:
        self.assertEqual(multiply(4, 5), 20)

    def test_by_zero(self) -> None:
        self.assertEqual(multiply(100, 0), 0)


class TestDivide(unittest.TestCase):
    def test_basic(self) -> None:
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero_raises(self) -> None:
        with self.assertRaises(ZeroDivisionError) as ctx:
            divide(1, 0)
        self.assertIn("0으로 나눌", str(ctx.exception))

    def test_negative_divisor(self) -> None:
        self.assertEqual(divide(10, -2), -5)


if __name__ == "__main__":
    unittest.main()
