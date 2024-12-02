import unittest
from src.ui.app import start_app

class TestUI(unittest.TestCase):
    def test_start_app(self):
        # UI test can be more complex, typically using mock tools
        result = start_app()
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
