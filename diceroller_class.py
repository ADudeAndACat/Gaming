from random import randint
from typing import List

class DiceRoller:
    def __init__(self, sides: int, mod: int = 0, times: int = 1) -> None:
        self.sides = sides
        self.mod = mod
        self.times = times

    def roll(self) -> List[str]:
        """
        Rolls the dice the specified number of times and applies the modifier.
        Returns a list of formatted strings showing the result of each roll.
        """
        return [f'{die_roll} + {self.mod} = {die_roll + self.mod}'
                for die_roll in [randint(1, self.sides) for _ in range(self.times)]]

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
