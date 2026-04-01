import unittest
from app import greet, farewell

class TestApp(unittest.TestCase):

    def test_greet(self):
        result = greet("Andrew")
        self.assertIn("Andrew", result)
        self.assertIn("AIDI 2004", result)

    def test_farewell(self):
        result = farewell("Andrew")
        self.assertIn("Andrew", result)

if __name__ == "__main__":
    unittest.main()