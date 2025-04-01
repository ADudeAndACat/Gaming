"""
Object-oriented implementation of dice rolling for tabletop RPGs.

This module provides a class-based approach for dice rolling with support for 
modifiers and multiple rolls. All dice rolls are logged to a JSON file for analysis.
"""

import os
from random import randint

from utils import add_roll_to_json, validate_positive_integer, format_roll_result
from config import DEFAULT_DICE_SIDES

class DiceRoller:
    """A class for rolling dice with various configurations."""
    
    def __init__(self, sides: int, mod: int = 0, times: int = 1) -> None:
        """
        Initializes the DiceRoller with the number of sides, modifier, and the number of rolls.

        Args:
            sides (int): The number of sides on the die.
            mod (int, optional): Modifier to apply to each roll. Defaults to 0.
            times (int, optional): Number of rolls to perform. Defaults to 1.
            
        Raises:
            ValueError: If sides or times is less than 1.
        """
        validate_positive_integer(sides, "Number of sides")
        validate_positive_integer(times, "Number of rolls")
        
        self.sides = sides
        self.mod = mod
        self.times = times
    
    def roll(self) -> list[dict[str, int]]:
        """
        Performs the dice roll(s) based on the configured parameters.
        
        Returns:
            list[dict[str, int]]: A list of dictionaries containing roll details.
        """
        results = []
        for _ in range(self.times):
            roll_value = randint(1, self.sides)
            results.append({
                "roll": roll_value,
                "modifier": self.mod,
                "total": roll_value + self.mod
            })
            add_roll_to_json(self.sides, roll_value)
        return results
    
    def format_results(self) -> list[str]:
        """
        Formats the dice roll results as strings.
        
        Returns:
            list[str]: A list of formatted strings describing each roll.
        """
        results = self.roll()
        return [format_roll_result(r["roll"], r["modifier"]) for r in results]

# Functions that create instances of the DiceRoller class for specific polyhedron dice
def d20(mod: int = 0, times: int = 1) -> list[str]:
    """
    Rolls 20-sided dice with optional modifier.
    
    Args:
        mod (int, optional): Modifier to add to each roll. Defaults to 0.
        times (int, optional): Number of dice to roll. Defaults to 1.
        
    Returns:
        list[str]: Formatted results of the dice rolls.
    """
    roller = DiceRoller(20, mod, times)
    result = roller.format_results()
    print(result)  # Print for immediate feedback
    return result

def d4(mod: int = 0, times: int = 1) -> list[str]:
    """
    Rolls 4-sided dice with optional modifier.
    
    Args:
        mod (int, optional): Modifier to add to each roll. Defaults to 0.
        times (int, optional): Number of dice to roll. Defaults to 1.
        
    Returns:
        list[str]: Formatted results of the dice rolls.
    """
    roller = DiceRoller(4, mod, times)
    result = roller.format_results()
    print(result)
    return result

def d6(mod: int = 0, times: int = 1) -> list[str]:
    """
    Rolls 6-sided dice with optional modifier.
    
    Args:
        mod (int, optional): Modifier to add to each roll. Defaults to 0.
        times (int, optional): Number of dice to roll. Defaults to 1.
        
    Returns:
        list[str]: Formatted results of the dice rolls.
    """
    roller = DiceRoller(6, mod, times)
    result = roller.format_results()
    print(result)
    return result

def d8(mod: int = 0, times: int = 1) -> list[str]:
    """
    Rolls 8-sided dice with optional modifier.
    
    Args:
        mod (int, optional): Modifier to add to each roll. Defaults to 0.
        times (int, optional): Number of dice to roll. Defaults to 1.
        
    Returns:
        list[str]: Formatted results of the dice rolls.
    """
    roller = DiceRoller(8, mod, times)
    result = roller.format_results()
    print(result)
    return result

def d10(mod: int = 0, times: int = 1) -> list[str]:
    """
    Rolls 10-sided dice with optional modifier.
    
    Args:
        mod (int, optional): Modifier to add to each roll. Defaults to 0.
        times (int, optional): Number of dice to roll. Defaults to 1.
        
    Returns:
        list[str]: Formatted results of the dice rolls.
    """
    roller = DiceRoller(10, mod, times)
    result = roller.format_results()
    print(result)
    return result

def d12(mod: int = 0, times: int = 1) -> list[str]:
    """
    Rolls 12-sided dice with optional modifier.
    
    Args:
        mod (int, optional): Modifier to add to each roll. Defaults to 0.
        times (int, optional): Number of dice to roll. Defaults to 1.
        
    Returns:
        list[str]: Formatted results of the dice rolls.
    """
    roller = DiceRoller(12, mod, times)
    result = roller.format_results()
    print(result)
    return result

def d100(mod: int = 0, times: int = 1) -> list[str]:
    """
    Rolls 100-sided dice (percentile dice) with optional modifier.
    
    Args:
        mod (int, optional): Modifier to add to each roll. Defaults to 0.
        times (int, optional): Number of dice to roll. Defaults to 1.
        
    Returns:
        list[str]: Formatted results of the dice rolls.
    """
    roller = DiceRoller(100, mod, times)
    result = roller.format_results()
    print(result)
    return result

def main() -> None:
    """
    Demonstrate the object-oriented dice rolling implementation.
    
    Shows examples of using the DiceRoller class with different dice types,
    modifiers, and multiple rolls.
    """
    print("Object-Oriented Dice Roller Demonstration")
    print("========================================")
    
    print("\nUsing dice helper functions:")
    print(f"d20 roll: {d20()}")
    print(f"d6+3 roll: {d6(3)}")
    print(f"2d8 rolls: {d8(times=2)}")
    
    print("\nDirect class usage:")
    # Create a d20 roller
    d20_roller = DiceRoller(20)
    print(f"Basic d20 roll: {d20_roller.format_results()}")
    
    # Create a d6 roller with +2 modifier
    d6_roller = DiceRoller(6, 2)
    print(f"d6+2 roll: {d6_roller.format_results()}")
    
    # Create a roller for 3d4
    d4_roller = DiceRoller(4, 0, 3)
    print(f"3d4 rolls: {d4_roller.format_results()}")
    
    # Custom-sided dice
    custom_roller = DiceRoller(30)  # A 30-sided die
    print(f"d30 roll: {custom_roller.format_results()}")
    
    print("\nThis module provides an object-oriented approach to dice rolling.")
    print("All results are automatically logged to the roll history file.")

if __name__ == "__main__":
    main()
