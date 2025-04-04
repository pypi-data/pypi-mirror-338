import unittest
from pyalert import PyAlert

class TestPyAlert(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(FileNotFoundError):
            PyAlert("invalid.json", "invalid_token.json")

if __name__ == "__main__":
    unittest.main()