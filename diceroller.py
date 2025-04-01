"""
Functional implementation of dice rolling for tabletop RPGs.

This module provides functions for simulating dice rolls commonly used in 
tabletop role-playing games, with support for modifiers and multiple rolls.
All roll results are logged to a JSON file for later analysis.
"""

import os
from random import randint

from config import DEFAULT_DICE_SIDES
from utils import add_roll_to_json, validate_positive_integer, format_roll_result

def d(sides: int, mod: int = 0, times: int = 1) -> list[dict[str, int]]:
    """
    Rolls a die with a specified number of sides a given number of times, with an optional modifier.

    Args:
        sides (int): The number of sides on the die.
        mod (int, optional): Modifier to add to the roll. Defaults to 0.
        times (int, optional): Number of rolls. Defaults to 1.

    Returns:
        list[dict[str, int]]: A list of dictionaries containing roll details.
        
    Raises:
        ValueError: If sides or times is less than 1.
    """
    validate_positive_integer(sides, "Number of sides")
    validate_positive_integer(times, "Number of rolls")

    results = []
    for _ in range(times):
        roll = randint(1, sides)
        total = roll + mod
        results.append({
            "roll": roll,
            "modifier": mod,
            "total": total
        })
        add_roll_to_json(sides, roll)
    return results

def format_results(results: list[dict[str, int]]) -> list[str]:
    """
    Converts roll result dictionaries into a list of formatted strings.

    Args:
        results (list[dict[str, int]]): List of dictionaries containing roll details.

    Returns:
        list[str]: List of formatted strings describing each roll.
    """
    return [format_roll_result(r["roll"], r["modifier"]) for r in results]

# Polyhedral dice functions
def d20(mod: int = 0, times: int = 1) -> list[str]:
    """
    Rolls 20-sided dice with optional modifier.
    
    Args:
        mod (int, optional): Modifier to add to each roll. Defaults to 0.
        times (int, optional): Number of dice to roll. Defaults to 1.
        
    Returns:
        list[str]: Formatted results of the dice rolls.
    """
    results = d(20, mod, times)
    return format_results(results)

def d4(mod: int = 0, times: int = 1) -> list[str]:
    """
    Rolls 4-sided dice with optional modifier.
    
    Args:
        mod (int, optional): Modifier to add to each roll. Defaults to 0.
        times (int, optional): Number of dice to roll. Defaults to 1.
        
    Returns:
        list[str]: Formatted results of the dice rolls.
    """
    results = d(4, mod, times)
    return format_results(results)

def d6(mod: int = 0, times: int = 1) -> list[str]:
    """
    Rolls 6-sided dice with optional modifier.
    
    Args:
        mod (int, optional): Modifier to add to each roll. Defaults to 0.
        times (int, optional): Number of dice to roll. Defaults to 1.
        
    Returns:
        list[str]: Formatted results of the dice rolls.
    """
    results = d(6, mod, times)
    return format_results(results)

def d8(mod: int = 0, times: int = 1) -> list[str]:
    """
    Rolls 8-sided dice with optional modifier.
    
    Args:
        mod (int, optional): Modifier to add to each roll. Defaults to 0.
        times (int, optional): Number of dice to roll. Defaults to 1.
        
    Returns:
        list[str]: Formatted results of the dice rolls.
    """
    results = d(8, mod, times)
    return format_results(results)

def d10(mod: int = 0, times: int = 1) -> list[str]:
    """
    Rolls 10-sided dice with optional modifier.
    
    Args:
        mod (int, optional): Modifier to add to each roll. Defaults to 0.
        times (int, optional): Number of dice to roll. Defaults to 1.
        
    Returns:
        list[str]: Formatted results of the dice rolls.
    """
    results = d(10, mod, times)
    return format_results(results)

def d12(mod: int = 0, times: int = 1) -> list[str]:
    """
    Rolls 12-sided dice with optional modifier.
    
    Args:
        mod (int, optional): Modifier to add to each roll. Defaults to 0.
        times (int, optional): Number of dice to roll. Defaults to 1.
        
    Returns:
        list[str]: Formatted results of the dice rolls.
    """
    results = d(12, mod, times)
    return format_results(results)

def d100(mod: int = 0, times: int = 1) -> list[str]:
    """
    Rolls 100-sided dice (percentile dice) with optional modifier.
    
    Args:
        mod (int, optional): Modifier to add to each roll. Defaults to 0.
        times (int, optional): Number of dice to roll. Defaults to 1.
        
    Returns:
        list[str]: Formatted results of the dice rolls.
    """
    results = d(100, mod, times)
    return format_results(results)

def main() -> None:
    """
    Demonstrate the functional dice rolling implementation.
    
    Shows examples of using various dice types with different modifiers and multiple rolls.
    """
    print("Functional Dice Roller Demonstration")
    print("===================================")
    
    print("\nBasic dice rolls:")
    print(f"d20 roll: {d20()}")
    print(f"d12 roll: {d12()}")
    print(f"d10 roll: {d10()}")
    print(f"d8 roll: {d8()}")
    print(f"d6 roll: {d6()}")
    print(f"d4 roll: {d4()}")
    print(f"d100 (percentile) roll: {d100()}")
    
    print("\nRolls with modifiers:")
    print(f"d20+5: {d20(5)}")
    print(f"d8-2: {d8(-2)}")
    
    print("\nMultiple dice rolls:")
    print(f"3d6: {d6(times=3)}")
    print(f"4d8+3: {d8(3, 4)}")
    
    print("\nThis module provides a functional approach to dice rolling.")
    print("All results are automatically logged to the roll history file.")

if __name__ == "__main__":
    main()
