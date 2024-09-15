from random import randint
from typing import List

# Main dice rolling function
def d(sides: int, mod: int = 0, times: int = 1) -> List[str]:
    return [f'{die_roll} + {mod} = {die_roll + mod}' for die_roll in [randint(1, sides) for roll in range(times)]]

# Each polyhedron dice
def d20(mod: int = 0, times: int = 1) -> None:
    print(d(20, mod, times))

def d4(mod: int = 0, times: int = 1) -> None:
    print(d(4, mod, times))

def d6(mod: int = 0, times: int = 1) -> None:
    print(d(6, mod, times))

def d8(mod: int = 0, times: int = 1) -> None:
    print(d(8, mod, times))

def d10(mod: int = 0, times: int = 1) -> None:
    print(d(10, mod, times))

def d12(mod: int = 0, times: int = 1) -> None:
    print(d(12, mod, times))

def d100(mod: int = 0, times: int = 1) -> None:
    print(d(100, mod, times))

# Cure Light Wounds
def clw(level: int) -> None:
    if level < 1:
        raise ValueError('Level must be 1 or higher.')
    mod: int = level if level <= 4 else 5
    roll: int = randint(1, 8)
    print(f'{roll} + {mod} = {roll + mod} damage healed.')

# Cure Moderate Wounds
def cmw(level: int) -> None:
    if level < 1:
        raise ValueError('Level must be 1 or higher.')
    mod: int = level if level <= 9 else 10
    roll: int = randint(2, 16)
    print(f'{roll} + {mod} = {roll + mod} damage healed.')

# Cure Serious Wounds
def csw(level: int) -> None:
    if level < 1:
        raise ValueError('Level must be 1 or higher.')
    mod: int = level if level <= 14 else 15
    roll: int = randint(3, 24)
    print(f'{roll} + {mod} = {roll + mod} damage healed.')

# Cure Critical Wounds
def ccw(level: int) -> None:
    if level < 1:
        raise ValueError('Level must be 1 or higher.')
    mod: int = level if level <= 19 else 20
    roll: int = randint(4, 32)
    print(f'{roll} + {mod} = {roll + mod} damage healed.')

# Cure (select) Wounds
def cure(wounds: str, level: int) -> None:
    if level < 1:
        raise ValueError('Level must be 1 or higher.')

    if wounds == 'light':
        mod: int = level if level <= 4 else 5
        roll: int = randint(1, 8)
    elif wounds == 'moderate':
        mod: int = level if level <= 9 else 10
        roll: int = randint(2, 16)
    elif wounds == 'serious':
        mod: int = level if level <= 14 else 15
        roll: int = randint(3, 24)
    elif wounds == 'critical':
        mod: int = level if level <= 19 else 20
        roll: int = randint(4, 32)
    else:
        raise ValueError('Invalid wound type specified.')

    print(f'{roll} + {mod} = {roll + mod} damage healed.')

def main() -> None:
    cure('serious', 10)

if __name__ == "__main__":
    main()