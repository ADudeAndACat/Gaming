"""
Test configuration file.

This file contains fixtures and configuration for the Gaming package tests.
"""
import os
import sys
import unittest

# Add the parent directory to the path so we can import the Gaming package
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
print(f"Added {parent_dir} to Python path from conftest.py")

# Try to import Gaming to verify it's accessible
try:
    import Gaming
    print(f"Successfully imported Gaming package from {Gaming.__file__}")
except ImportError as e:
    print(f"ERROR in conftest.py: Could not import Gaming package: {e}")

# Sample data that can be used across test files
SAMPLE_DATA = {
    "sample_roll": "3d6",
    "sample_stats": [10, 12, 14, 8, 15, 11]
}

# Define a base test case class that other test classes can inherit from
class GamingBaseTestCase(unittest.TestCase):
    """Base test case class for Gaming package tests."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.sample_data = SAMPLE_DATA
