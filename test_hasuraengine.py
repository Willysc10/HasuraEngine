# test_hasuraengine.py
"""
Tests for HasuraEngine module.
"""

import unittest
from hasuraengine import HasuraEngine

class TestHasuraEngine(unittest.TestCase):
    """Test cases for HasuraEngine class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HasuraEngine()
        self.assertIsInstance(instance, HasuraEngine)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HasuraEngine()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
