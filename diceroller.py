from random import randint
from typing import List

# Main dice rolling function
def d(sides: int, mod: int = 0, times: int = 1) -> List[str]:
    return [f'{die_roll} + {mod} = {die_roll + mod}' for die_roll in [randint(1, sides) for _ in range(times)]]

# Each polyhedron dice function
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

def main() -> None:
    d20(16)

if __name__ == "__main__":
    main()
