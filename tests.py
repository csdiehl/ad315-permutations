import unittest
from unittest.mock import patch
import math
from combos import main, getItem

class TestMainFunctions(unittest.TestCase):

    # Gets a valid integer from the user
    @patch('builtins.input', side_effect=['5'])
    def test_getItem_valid_input(self, mock_input):
        
        result = getItem("Enter a positive integer")
        self.assertEqual(result, 5)

    # keeps prompting until user enters a valid choice
    @patch('builtins.input', side_effect=['-1', '0', '3'])
    def test_getItem_invalid_then_valid_input(self, mock_input):
        result = getItem("Enter a positive integer")
        self.assertEqual(result, 3)

    # doesn't crash if you try to enter something that isn't a number
    @patch('builtins.input', side_effect=['lalala', 'hello', '3'])
    def test_string_input(self, mock_input):
        result = getItem("Enter a positive integer")
        self.assertEqual(result, 3)

    # Calculations combos and permutations correctly
    @patch('builtins.input', side_effect=['6', '2'])
    @patch('builtins.print')
    def test_main_permutations_combinations(self, mock_print, mock_input):
        main()
        
        mock_print.assert_any_call('The number of permutations is', math.perm(6, 2))
        mock_print.assert_any_call('The number of combinations is', math.comb(6, 2))

if __name__ == '__main__':
    unittest.main()