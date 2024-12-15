import json, os
from random import randint
from typing import List, Dict, Tuple
from datetime import datetime

class DiceRoller:
    def __init__(self, sides: int, mod: int = 0, times: int = 1) -> None:
        """
        Initializes the DiceRoller with the number of sides, modifier, and the number of rolls.

        Args:
            sides (int): The number of sides on the dice.
            mod (int, optional): The modifier to add to the roll. Defaults to 0.
            times (int, optional): The number of rolls to make. Defaults to 1.
        """
        self.sides = sides
        self.mod = mod
        self.times = times

    def add_roll_to_json(self, roll: int, filename: str = 'rolls.json') -> None:
        """
        Appends a dice roll tuple (sides, roll) to a list under the current date key in a JSON file.

        Args:
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
                        data: Dict[str, List[Tuple[int, int]]] = json.load(file)
                        if current_date in data:
                            data[current_date] = [tuple(item) for item in data[current_date]]
                except json.JSONDecodeError:
                    print(f"Warning: {filename} was corrupted. Starting fresh.")
                    data = {}
            else:
                data = {}

            roll_tuple = (self.sides, roll)

            if current_date in data:
                data[current_date].append(roll_tuple)
            else:
                data[current_date] = [roll_tuple]

            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error while handling roll data: {str(e)}")

    def roll(self) -> List[str]:
        """
        Rolls the dice the specified number of times, applies the modifier, and appends each roll to a JSON file.

        Returns:
            List[str]: A list of formatted strings showing the result of each roll.
        """
        results = []
        for _ in range(self.times):
            roll = randint(1, self.sides)
            self.add_roll_to_json(roll)  # Append the roll to the JSON file
            results.append(f'{roll} + {self.mod} = {roll + self.mod}')
        return results

# Each polyhedron dice as functions that create instances of the class
def d20(mod: int = 0, times: int = 1) -> None:
    """Rolls 20-sided dice."""
    roller = DiceRoller(20, mod, times)
    print(roller.roll())

def d4(mod: int = 0, times: int = 1) -> None:
    """Rolls 4-sided dice."""
    roller = DiceRoller(4, mod, times)
    print(roller.roll())

def d6(mod: int = 0, times: int = 1) -> None:
    """Rolls 6-sided dice."""
    roller = DiceRoller(6, mod, times)
    print(roller.roll())

def d8(mod: int = 0, times: int = 1) -> None:
    """Rolls 8-sided dice."""
    roller = DiceRoller(8, mod, times)
    print(roller.roll())

def d10(mod: int = 0, times: int = 1) -> None:
    """Rolls 10-sided dice."""
    roller = DiceRoller(10, mod, times)
    print(roller.roll())

def d12(mod: int = 0, times: int = 1) -> None:
    """Rolls 12-sided dice."""
    roller = DiceRoller(12, mod, times)
    print(roller.roll())

def d100(mod: int = 0, times: int = 1) -> None:
    """Rolls 100-sided dice."""
    roller = DiceRoller(100, mod, times)
    print(roller.roll())

def main() -> None:
    d20(16)

if __name__ == "__main__":
    main()
