"""
Shared utility functions for the Gaming package.

This module provides common functionality used across different modules
in the Gaming package.
"""

import json
import os
import logging
from datetime import datetime

# Set up basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Type aliases for better readability
RollTuple = tuple[int, int]  # (sides, roll)
RollHistory = dict[str, list[RollTuple]]  # date -> list of rolls

def add_roll_to_json(sides: int, roll: int, filename: str | None = None) -> None:
    """
    Appends a dice roll tuple (sides, roll) to a list under the current date key in a JSON file.

    Args:
        sides (int): The number of sides on the die.
        roll (int): The dice roll result to append.
        filename (str | None, optional): The name of the JSON file to store the rolls. 
                                  If None, uses the default from config.

    Raises:
        IOError: If there is an issue with file operations.
        json.JSONDecodeError: If the JSON file is corrupted.
    """
    # Input validation
    validate_positive_integer(sides, "sides")
    if roll < 1 or roll > sides:
        raise ValueError(f"Roll value {roll} is invalid for a {sides}-sided die")
    
    # Try to import the config module for default filename
    try:
        from config import ROLL_HISTORY_FILE
        
        if filename is None:
            filename = ROLL_HISTORY_FILE
    except ImportError:
        # Fallback if config module is not available
        if filename is None:
            filename = 'rolls.json'
        logging.warning("Config module not found, using default filename: rolls.json")
        
    current_date = datetime.now().strftime('%Y-%m-%d')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        data: dict[str, list[list[int]]] = {}
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError as e:
                logging.warning(f"File {filename} was corrupted. Starting fresh. Error: {str(e)}")
        
        # Create the roll tuple and append it
        roll_data = [sides, roll]
        
        if current_date in data:
            data[current_date].append(roll_data)
        else:
            data[current_date] = [roll_data]
            
        # Ensure the directory exists
        ensure_directory_exists(os.path.dirname(file_path))
            
        # Write back to file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
            
    except Exception as e:
        logging.error(f"Error saving roll to {filename}: {str(e)}")
        raise IOError(f"Failed to save roll data: {str(e)}")

def ensure_directory_exists(directory_path: str) -> None:
    """
    Ensures that the specified directory exists, creating it if necessary.

    Args:
        directory_path (str): Path to the directory to check/create.
    """
    if directory_path and not os.path.exists(directory_path):
        os.makedirs(directory_path)

def validate_positive_integer(value: int, name: str) -> None:
    """
    Validates that a value is a positive integer.

    Args:
        value (int): The value to validate.
        name (str): The name of the value (for error messages).

    Raises:
        ValueError: If the value is not a positive integer.
    """
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer, got {type(value).__name__}")
    
    if value <= 0:
        raise ValueError(f"{name} must be positive, got {value}")

def format_roll_result(roll: int, modifier: int = 0) -> str:
    """
    Formats a dice roll result as a string.

    Args:
        roll (int): The dice roll value.
        modifier (int, optional): Modifier applied to the roll. Defaults to 0.

    Returns:
        str: Formatted string representing the roll result.
    """
    if modifier == 0:
        return str(roll)
    
    total = roll + modifier
    modifier_str = f"+{modifier}" if modifier > 0 else str(modifier)
    return f"{roll} ({total} = {roll}{modifier_str})"

def main() -> None:
    """
    Demonstrate the utility functions in this module.
    
    Shows examples of using the various utility functions that support 
    other modules in the Gaming package.
    """
    print("Gaming Utilities - Shared Utility Functions")
    print("=========================================")
    
    # Demonstrate format_roll_result
    print("\n1. Format Roll Result:")
    print(f"  Basic roll (8): {format_roll_result(8)}")
    print(f"  Roll with positive modifier (8, +3): {format_roll_result(8, 3)}")
    print(f"  Roll with negative modifier (8, -2): {format_roll_result(8, -2)}")
    
    # Demonstrate validate_positive_integer
    print("\n2. Validate Positive Integer:")
    print("  Validating value 5 as 'dice sides'...")
    try:
        validate_positive_integer(5, "dice sides")
        print("  Validation passed")
    except ValueError as e:
        print(f"  Validation failed: {str(e)}")
        
    print("  Validating value 0 as 'times'...")
    try:
        validate_positive_integer(0, "times")
        print("  Validation passed")
    except ValueError as e:
        print(f"  Validation failed: {str(e)}")
    
    # Demonstrate ensure_directory_exists
    import tempfile
    import os
    temp_dir = os.path.join(tempfile.gettempdir(), "gaming_utils_demo")
    print(f"\n3. Ensure Directory Exists:")
    print(f"  Creating directory: {temp_dir}")
    ensure_directory_exists(temp_dir)
    if os.path.exists(temp_dir):
        print(f"  Directory exists")
    else:
        print(f"  Failed to create directory")
    
    # Demonstrate add_roll_to_json
    print("\n4. Add Roll to JSON:")
    print("  Adding roll data (d20, result 15) to a temporary file...")
    temp_file = os.path.join(temp_dir, "temp_rolls.json")
    try:
        add_roll_to_json(20, 15, temp_file)
        if os.path.exists(temp_file):
            print(f"  Roll data saved to {temp_file}")
            with open(temp_file, "r") as f:
                print(f"  File content preview: {f.read()[:100]}...")
    except Exception as e:
        print(f"  Failed to save roll data: {str(e)}")
    
    print("\nThis module provides shared utilities used across the Gaming package.")
    print("Import specific functions as needed to avoid code duplication.")

if __name__ == "__main__":
    main()
