from random import randint
from typing import List, Callable

# Dictionary of dice roll functions
# Each lambda rolls a specified type of die `t` times, adds a modifier `m`, and returns a formatted list of results.
roll: dict[str, Callable[[int, int], List[str]]] = {
    "d4": lambda m=0, t=1: [f"{r} + {m} = {r + m}" for r in [randint(1, 4) for _ in range(t)]],
    "d6": lambda m=0, t=1: [f"{r} + {m} = {r + m}" for r in [randint(1, 6) for _ in range(t)]],
    "d8": lambda m=0, t=1: [f"{r} + {m} = {r + m}" for r in [randint(1, 8) for _ in range(t)]],
    "d10": lambda m=0, t=1: [f"{r} + {m} = {r + m}" for r in [randint(1, 10) for _ in range(t)]],
    "d12": lambda m=0, t=1: [f"{r} + {m} = {r + m}" for r in [randint(1, 12) for _ in range(t)]],
    "d20": lambda m=0, t=1: [f"{r} + {m} = {r + m}" for r in [randint(1, 20) for _ in range(t)]],
    "d100": lambda m=0, t=1: [f"{r} + {m} = {r + m}" for r in [randint(1, 100) for _ in range(t)]],
}

def main() -> None:
    print(roll["d20"]())

if __name__ == "__main__":
    main()
