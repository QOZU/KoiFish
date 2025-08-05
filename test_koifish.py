# test_koifish.py
"""
Tests for KoiFish module.
"""

import unittest
from koifish import KoiFish

class TestKoiFish(unittest.TestCase):
    """Test cases for KoiFish class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KoiFish()
        self.assertIsInstance(instance, KoiFish)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KoiFish()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
