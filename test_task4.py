import unittest
from cnst import cnst

class TestCnst(unittest.TestCase):
    def test_same_input_output(self):
        # Test case where input and output integers are the same
        input_int = 5
        expected_output = 5
        self.assertEqual(cnst(input_int), expected_output)

if __name__ == '__main__':
    unittest.main()