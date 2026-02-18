"""
Unit tests for main.py
"""
import unittest
from main import greet


class TestGreet(unittest.TestCase):
    """Test cases for the greet function."""
    
    def test_greet_default(self):
        """Test greet with default parameter."""
        result = greet()
        self.assertEqual(result, "Hello, World!")
    
    def test_greet_custom_name(self):
        """Test greet with custom name."""
        result = greet("Alice")
        self.assertEqual(result, "Hello, Alice!")
    
    def test_greet_empty_string(self):
        """Test greet with empty string."""
        result = greet("")
        self.assertEqual(result, "Hello, !")


if __name__ == "__main__":
    unittest.main()
