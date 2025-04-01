"""
Test runner script for the Gaming package.

This script discovers and runs all unittest tests in the 'test' directory.
"""
import sys
import os
import unittest
from pathlib import Path

def discover_and_run_tests():
    """Discover and run unittest tests."""
    # Add the parent directory to sys.path
    parent_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, parent_dir)
    
    # Print the path for debugging
    print(f"Added {parent_dir} to Python path")
    print(f"Current sys.path: {sys.path}")
    
    # Try to import Gaming to verify it's accessible
    try:
        import Gaming
        print(f"Successfully imported Gaming package from {Gaming.__file__}")
    except ImportError as e:
        print(f"ERROR: Could not import Gaming package: {e}")
    
    # Get the test directory
    test_dir = Path(__file__).parent / "test"
    
    # Discover all tests
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=str(test_dir), pattern="test_*.py")
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()

if __name__ == "__main__":
    print("Running Gaming package tests...")
    success = discover_and_run_tests()
    sys.exit(0 if success else 1)
