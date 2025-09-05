import unittest
from unittest.mock import patch

import simple_calculator.main as calculator


class TestMainFunction(unittest.TestCase):
    @patch("builtins.input")
    @patch("builtins.print")
    def test_sum_action(self, mock_print, mock_input):
        # Simulate: action=1 (Sum), a=3, b=2
        mock_input.side_effect = ["1", "3", "2"]
        calculator.main()
        mock_print.assert_called_with(5)  # Sum: 3 + 2

    @patch("builtins.input")
    @patch("builtins.print")
    def test_subtraction_reversed(self, mock_print, mock_input):
        # action=2 (Subtraction), a=10, b=8, reversed_diff=Y
        mock_input.side_effect = ["2", "10", "8", "Y"]
        calculator.main()
        mock_print.assert_called_with(-2)  # Reversed: 8 - 10

    @patch("builtins.input")
    @patch("builtins.print")
    def test_multiplication(self, mock_print, mock_input):
        # action=3 (Multiplication), a=2, b=5
        mock_input.side_effect = ["3", "2", "5"]
        calculator.main()
        mock_print.assert_called_with(10)  # 2 * 5

    @patch("builtins.input")
    @patch("builtins.print")
    def test_division_integer(self, mock_print, mock_input):
        # action=4 (Division), a=10, b=3, division type="integer"
        mock_input.side_effect = ["4", "10", "3", "integer"]
        calculator.main()
        mock_print.assert_called_with(3)  # 10 // 3

    # You can add more tests for error handling, other division types, etc.


if __name__ == "__main__":
    unittest.main()
