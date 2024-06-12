
import unittest
from cnst import cnst

class TestBuiltins(unittest.TestCase):
    def test_cnst(self):
        for i in range(-10, 10):
            self.assertEqual(cnst(i), i, f"Failed for input: {i}")

if __name__ == '__main__':
    unittest.main()