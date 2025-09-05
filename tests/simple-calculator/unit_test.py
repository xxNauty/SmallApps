import unittest

from simple_calculator import main as calculator


class TestSimpleCalculator(unittest.TestCase):
    def test_string_to_num(self) -> None:
        self.assertEqual(3.4, calculator.string_to_num("3.4"))
        self.assertEqual(3, calculator.string_to_num("3"))

        self.assertTrue(isinstance(calculator.string_to_num("0"), int))
        self.assertTrue(isinstance(calculator.string_to_num("0.0"), float))

        with self.assertRaises(ValueError):
            calculator.string_to_num("qwe")
        with self.assertRaises(ValueError):
            calculator.string_to_num("1q")
        with self.assertRaises(ValueError):
            calculator.string_to_num("q1")
        with self.assertRaises(ValueError):
            calculator.string_to_num("1.1.1")

        self.assertEqual(float, type(calculator.string_to_num("1.1")))
        self.assertEqual(int, type(calculator.string_to_num("1")))

    def test_custom_sum(self) -> None:
        self.assertEqual(5, calculator.custom_sum(3, 2))
        self.assertEqual(5, calculator.custom_sum(2, 3))
        self.assertEqual(-5, calculator.custom_sum(-2, -3))
        self.assertEqual(0, calculator.custom_sum(2, -2))

        with self.assertRaises(TypeError):
            calculator.custom_sum("2", 1)
        with self.assertRaises(TypeError):
            calculator.custom_sum(2, "2")

    def test_custom_difference(self) -> None:
        self.assertEqual(2, calculator.custom_difference(10, 8))
        self.assertEqual(-2, calculator.custom_difference(10, 8, True))
        self.assertEqual(-2, calculator.custom_difference(8, 10))
        self.assertEqual(18, calculator.custom_difference(10, -8))

        with self.assertRaises(TypeError):
            calculator.custom_difference("a", 2)
        with self.assertRaises(TypeError):
            calculator.custom_difference(2, "2")

    def test_custom_product(self) -> None:
        self.assertEqual(10, calculator.custom_product(2, 5))
        self.assertEqual(10, calculator.custom_product(5, 2))
        self.assertEqual(-10, calculator.custom_product(-2, 5))
        self.assertEqual(10, calculator.custom_product(-2, -5))

        with self.assertRaises(TypeError):
            calculator.custom_product("a", 2)
        with self.assertRaises(TypeError):
            calculator.custom_product(2, "2")

    def test_custom_quotient(self) -> None:
        self.assertEqual(10, calculator.custom_quotient(100, 10))
        self.assertAlmostEqual(calculator.custom_quotient(100, 10), calculator.custom_quotient(1000, 100, "normal"))
        self.assertEqual(33, calculator.custom_quotient(100, 3, "integer"))
        self.assertEqual(1, calculator.custom_quotient(100, 3, "modulus"))

        with self.assertRaises(TypeError):
            calculator.custom_quotient("1", 1)
        with self.assertRaises(TypeError):
            calculator.custom_quotient(1, "1")
        with self.assertRaises(TypeError):
            calculator.custom_quotient(1, 1, "not_supported_type")

        with self.assertRaises(ZeroDivisionError):
            calculator.custom_quotient(1, 0)


if __name__ == "__main__":
    unittest.main()
