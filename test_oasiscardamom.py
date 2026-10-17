# test_oasiscardamom.py
"""
Tests for OasisCardamom module.
"""

import unittest
from oasiscardamom import OasisCardamom

class TestOasisCardamom(unittest.TestCase):
    """Test cases for OasisCardamom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OasisCardamom()
        self.assertIsInstance(instance, OasisCardamom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OasisCardamom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
