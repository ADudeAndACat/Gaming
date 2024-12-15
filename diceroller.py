import json, os
from random import randint
from typing import List, Tuple, Dict, Union
from datetime import datetime

def add_roll_to_json(sides: int, roll: int, filename: str = 'rolls.json') -> None:
    """
    Appends a dice roll tuple (sides, roll) to a list under the current date key in a JSON file.

    Args:
        sides (int): The number of sides on the die.
        roll (int): The dice roll result to append.
        filename (str, optional): The name of the JSON file to store the rolls. Defaults to 'rolls.json'.
    """
    current_date: str = datetime.now().strftime('%Y-%m-%d')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        data: Dict[str, List[Union[Tuple[int, int], int]]] = {}
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                print(f"Warning: {filename} was corrupted. Starting fresh.")

        # Create the roll tuple and append it
        roll_tuple = (sides, roll)  # Using tuple as per type hint
        data.setdefault(current_date, []).append(roll_tuple)

        # Write the updated data back to the file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error while handling roll data: {str(e)}")

def d(sides: int, mod: int = 0, times: int = 1) -> List[Dict[str, int]]:
    """
    Rolls a die with a specified number of sides a given number of times, with an optional modifier.

    Args:
        sides (int): The number of sides on the die.
        mod (int, optional): Modifier to add to the roll. Defaults to 0.
        times (int, optional): Number of rolls. Defaults to 1.

    Returns:
        List[Dict[str, int]]: A list of dictionaries containing roll details.
    """
    if sides < 1:
        raise ValueError("Number of sides must be positive")
    if times < 1:
        raise ValueError("Number of rolls must be positive")

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

def format_roll_results(results: List[Dict[str, int]]) -> None:
    """Format and print roll results."""
    for result in results:
        if result["modifier"] != 0:
            print(f"{result['roll']} + {result['modifier']} = {result['total']}")
        else:
            print(f"{result['roll']}")

# Polyhedral dice functions
def d20(mod: int = 0, times: int = 1) -> None:
    """Rolls 20-sided dice."""
    format_roll_results(d(20, mod, times))

def d4(mod: int = 0, times: int = 1) -> None:
    """Rolls 4-sided dice."""
    format_roll_results(d(4, mod, times))

def d6(mod: int = 0, times: int = 1) -> None:
    """Rolls 6-sided dice."""
    format_roll_results(d(6, mod, times))

def d8(mod: int = 0, times: int = 1) -> None:
    """Rolls 8-sided dice."""
    format_roll_results(d(8, mod, times))

def d10(mod: int = 0, times: int = 1) -> None:
    """Rolls 10-sided dice."""
    format_roll_results(d(10, mod, times))

def d12(mod: int = 0, times: int = 1) -> None:
    """Rolls 12-sided dice."""
    format_roll_results(d(12, mod, times))

def d100(mod: int = 0, times: int = 1) -> None:
    """Rolls 100-sided dice."""
    format_roll_results(d(100, mod, times))

def main() -> None:
    d20(17)

if __name__ == "__main__":
    main()
