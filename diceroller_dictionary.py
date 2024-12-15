import json, os
from random import randint
from typing import List, Callable
from datetime import datetime


# Function to log rolls to a JSON file
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
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    data: dict = json.load(file)
                    if current_date in data:
                        data[current_date] = [tuple(item) for item in data[current_date]]
            except json.JSONDecodeError:
                print(f"Warning: {filename} was corrupted. Starting fresh.")
                data = {}
        else:
            data = {}

        roll_tuple = (sides, roll)

        if current_date in data:
            data[current_date].append(roll_tuple)
        else:
            data[current_date] = [roll_tuple]

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error while handling roll data: {str(e)}")


# Dictionary of dice roll functions with improved typing and documentation
roll: dict[str, Callable[[int, int], List[str]]] = {
    "d4": lambda m=0, t=1: [f"{(r := randint(1, 4))} + {m} = {r + m}" for _ in range(t)],
    "d6": lambda m=0, t=1: [f"{(r := randint(1, 6))} + {m} = {r + m}" for _ in range(t)],
    "d8": lambda m=0, t=1: [f"{(r := randint(1, 8))} + {m} = {r + m}" for _ in range(t)],
    "d10": lambda m=0, t=1: [f"{(r := randint(1, 10))} + {m} = {r + m}" for _ in range(t)],
    "d12": lambda m=0, t=1: [f"{(r := randint(1, 12))} + {m} = {r + m}" for _ in range(t)],
    "d20": lambda m=0, t=1: [f"{(r := randint(1, 20))} + {m} = {r + m}" for _ in range(t)],
    "d100": lambda m=0, t=1: [f"{(r := randint(1, 100))} + {m} = {r + m}" for _ in range(t)],
}


def roll_and_log(dice_type: str, mod: int = 0, times: int = 1) -> List[str]:
    """
    Rolls a specific type of die and logs the results.
    
    Args:
        dice_type (str): The type of die to roll (e.g., "d20", "d6")
        mod (int, optional): Modifier to add to each roll. Defaults to 0.
        times (int, optional): Number of times to roll. Defaults to 1.
    
    Returns:
        List[str]: List of formatted roll results
    """
    sides = int(dice_type[1:])  # Extract number of sides from dice type
    results = roll[dice_type](mod, times)
    
    # Log each roll
    for result in results:
        roll_value = int(result.split()[0])  # Extract the raw roll value
        add_roll_to_json(sides, roll_value)
    
    return results


def main() -> None:
    """Example usage of the dice rolling system."""
    # Roll a d20 with modifier 5, four times
    results = roll_and_log("d20", 5, 4)
    print(f"Rolling d20+5 four times: {results}")


if __name__ == "__main__":
    main()
