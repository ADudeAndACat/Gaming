"""
Dictionary-based implementation of dice rolling for tabletop RPGs.

This module provides a lightweight dictionary-based approach to dice rolling
using lambda functions, with support for optional modifiers and multiple rolls.
"""

from random import randint
from utils import add_roll_to_json, validate_positive_integer
from config import DEFAULT_DICE_SIDES

# Dictionary of dice roll functions
roll = {
    "d4": lambda m=0, t=1: [f"{(r := randint(1, 4))} + {m} = {r + m}" for _ in range(t)],
    "d6": lambda m=0, t=1: [f"{(r := randint(1, 6))} + {m} = {r + m}" for _ in range(t)],
    "d8": lambda m=0, t=1: [f"{(r := randint(1, 8))} + {m} = {r + m}" for _ in range(t)],
    "d10": lambda m=0, t=1: [f"{(r := randint(1, 10))} + {m} = {r + m}" for _ in range(t)],
    "d12": lambda m=0, t=1: [f"{(r := randint(1, 12))} + {m} = {r + m}" for _ in range(t)],
    "d20": lambda m=0, t=1: [f"{(r := randint(1, 20))} + {m} = {r + m}" for _ in range(t)],
    "d100": lambda m=0, t=1: [f"{(r := randint(1, 100))} + {m} = {r + m}" for _ in range(t)]
}


def roll_and_log(dice_type, mod=0, times=1):
    """
    Rolls a specific type of die and logs the results.
    
    Args:
        dice_type: The type of die to roll (e.g., "d20", "d6")
        mod: Modifier to add to each roll. Defaults to 0.
        times: Number of times to roll. Defaults to 1.
    
    Returns:
        List of formatted roll results
        
    Raises:
        ValueError: If dice_type is not valid, mod is negative, or times is less than 1
        KeyError: If dice_type is not in the roll dictionary
    """
    # Validate inputs
    validate_positive_integer(times, "Number of rolls")
    if mod < 0:
        raise ValueError(f"Modifier must be non-negative, got {mod}")
    
    if not dice_type.startswith('d'):
        raise ValueError(f"Invalid dice type: {dice_type}. Must start with 'd' followed by number of sides.")
    
    try:
        sides = int(dice_type[1:])  # Extract number of sides from dice type
        validate_positive_integer(sides, "Number of sides")
    except ValueError:
        raise ValueError(f"Invalid dice type: {dice_type}. Must be in format 'd<number>'.")
    
    # Check if the dice type exists in our dictionary
    if dice_type not in roll:
        raise KeyError(f"Unsupported dice type: {dice_type}")
    
    # Get the results
    results = roll[dice_type](mod, times)
    
    # Log each roll
    for result in results:
        # Extract the raw roll value from the formatted string
        try:
            roll_value = int(result.split()[0])  # Extract the raw roll value
            add_roll_to_json(sides, roll_value)
        except (IndexError, ValueError) as e:
            # This shouldn't happen with our formatting, but just in case
            import logging
            logging.warning(f"Could not parse roll result: {result}. Error: {str(e)}")
    
    return results


def main():
    """
    Demonstrate the dictionary-based dice rolling implementation.
    
    Shows examples of direct dictionary access and using the roll_and_log function
    with different dice types, modifiers, and multiple rolls.
    """
    print("Dictionary-Based Dice Roller Demonstration")
    print("=========================================")
    
    print("\nUsing roll_and_log function:")
    print(f"d20 roll: {roll_and_log('d20')}")
    print(f"d20+5 roll: {roll_and_log('d20', 5)}")
    print(f"3d6 rolls: {roll_and_log('d6', times=3)}")
    print(f"2d8+2 rolls: {roll_and_log('d8', 2, 2)}")
    print(f"d100 (percentile) roll: {roll_and_log('d100')}")
    
    print("\nDirect dictionary access:")
    print(f"d20 roll: {roll['d20'](0, 1)}")
    print(f"d6+3 roll: {roll['d6'](3, 1)}")
    print(f"4d4 rolls: {roll['d4'](0, 4)}")
    
    print("\nAvailable dice types:")
    for dice_type in roll.keys():
        print(f"- {dice_type}")
    
    print("\nThis module provides a dictionary-based approach to dice rolling.")
    print("All results are automatically logged to the roll history file.")


if __name__ == "__main__":
    main()
