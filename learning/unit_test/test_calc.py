import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 4), 5)
        self.assertEqual(calc.add(5, -1), 4)
        self.assertEqual(calc.add(1, -10), -9)

    def test_minus(self):
        self.assertEqual(calc.minus(1, 5), -4)
        self.assertEqual(calc.minus(5, -1), 6)
        self.assertEqual(calc.minus(-1, -5), 4)

    def test_multiply(self):
        self.assertEqual(calc.mul(40, 10), 400)
        self.assertEqual(calc.mul(0, 49), 0)
        self.assertEqual(calc.mul(-4, -1), 4)

    def test_divide(self):
        self.assertEqual(calc.div(10, 2), 5)
        self.assertEqual(calc.div(-1, -1), 1)
        self.assertEqual(calc.div(5, 2), 2.5)

        with self.assertRaises(ValueError):
            calc.div(0, 0)


if __name__ == "__main__":
    unittest.main()
