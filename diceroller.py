import json, os
from random import randint
from typing import List
from datetime import datetime

def add_roll_to_json(roll: int, filename: str = 'rolls.json') -> None:
    """
    Appends a dice roll to a list under the current date key in a JSON file.

    Args:
        roll (int): The dice roll result to append.
        filename (str, optional): The name of the JSON file to store the rolls. Defaults to 'rolls.json'.
    """
    # Get the current date as a string (format: YYYY-MM-DD)
    current_date: str = datetime.now().strftime('%Y-%m-%d')

    # Load existing data from the JSON file if it exists, otherwise initialize an empty dictionary
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data: dict = json.load(file)
    else:
        data = {}

    # Append the roll to the current date key; create a new list if it doesn't exist
    if current_date in data:
        data[current_date].append(roll)
    else:
        data[current_date] = [roll]

    # Write the updated data back to the file
    with open(filename, 'w') as file:
        json.dump(data, file)

def d(sides: int, mod: int = 0, times: int = 1) -> List[str]:
    """
    Rolls a die with a specified number of sides a given number of times, with an optional modifier.

    Args:
        sides (int): The number of sides on the die.
        mod (int, optional): Modifier to add to the roll. Defaults to 0.
        times (int, optional): Number of rolls. Defaults to 1.

    Returns:
        List[str]: A list of strings of results.
    """
    results: List[str] = []
    for dice in range(times):
        roll: int = randint(1, sides)
        result = f"{roll} + {mod} = {roll + mod}"
        results.append(result)
        add_roll_to_json(roll)
    return results

# Polyhedral dice functions
def d20(mod: int = 0, times: int = 1) -> None:
    """Rolls 20-sided dice."""
    print(d(20, mod, times))

def d4(mod: int = 0, times: int = 1) -> None:
    """Rolls 4-sided dice."""
    print(d(4, mod, times))

def d6(mod: int = 0, times: int = 1) -> None:
    """Rolls 6-sided dice."""
    print(d(6, mod, times))

def d8(mod: int = 0, times: int = 1) -> None:
    """Rolls 8-sided dice."""
    print(d(8, mod, times))

def d10(mod: int = 0, times: int = 1) -> None:
    """Rolls 10-sided dice."""
    print(d(10, mod, times))

def d12(mod: int = 0, times: int = 1) -> None:
    """Rolls 12-sided dice."""
    print(d(12, mod, times))

def d100(mod: int = 0, times: int = 1) -> None:
    """Rolls 100-sided dice."""
    print(d(100, mod, times))

def main() -> None:
    d20(14)

if __name__ == "__main__":
    main()

