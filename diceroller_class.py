import json
from random import randint
from typing import List
from datetime import datetime
import os


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
        Appends a dice roll to a list under the current date key in a JSON file.

        Args:
            roll (int): The dice roll result to append.
            filename (str, optional): The name of the JSON file to store the rolls. Defaults to 'rolls.json'.
        """
        current_date = datetime.now().strftime('%Y-%m-%d')

        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
        else:
            data = {}

        if current_date in data:
            data[current_date].append(roll)
        else:
            data[current_date] = [roll]

        with open(filename, 'w') as file:
            json.dump(data, file)

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
def roll_d20(mod: int = 0, times: int = 1) -> None:
    d20 = DiceRoller(20, mod, times)
    print(d20.roll())

def roll_d4(mod: int = 0, times: int = 1) -> None:
    d4 = DiceRoller(4, mod, times)
    print(d4.roll())

def roll_d6(mod: int = 0, times: int = 1) -> None:
    d6 = DiceRoller(6, mod, times)
    print(d6.roll())

def roll_d8(mod: int = 0, times: int = 1) -> None:
    d8 = DiceRoller(8, mod, times)
    print(d8.roll())

def roll_d10(mod: int = 0, times: int = 1) -> None:
    d10 = DiceRoller(10, mod, times)
    print(d10.roll())

def roll_d12(mod: int = 0, times: int = 1) -> None:
    d12 = DiceRoller(12, mod, times)
    print(d12.roll())

def roll_d100(mod: int = 0, times: int = 1) -> None:
    d100 = DiceRoller(100, mod, times)
    print(d100.roll())

def main() -> None:
    roll_d20(16, 3A)

if __name__ == "__main__":
    main()
