import time
from random import randint
from typing import Callable, List

# Decorator to measure the execution time of a function with high precision
def measure_time(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # High-precision timer
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.8f} seconds")
        return result
    return wrapper

# Base dice rolling function
@measure_time
def d(sides: int, mod: int = 0, times: int = 1) -> List[str]:
    results: List[str] = []
    for _ in range(times):
        roll: int = randint(1, sides)
        result = f"{roll} + {mod} = {roll + mod}"
        results.append(result)
    return results

@measure_time
def d20(mod: int = 0, times: int = 1) -> List[str]:
    return d(20, mod, times)

# Dictionary with lambda functions for dice rolls
roll = {
    "d20": lambda m=0, t=1: [f"{r} + {m} = {r + m}" for r in [randint(1, 20) for _ in range(t)]],
}

# Class-based dice roller
class DiceRoller:
    def __init__(self, sides: int, mod: int = 0, times: int = 1) -> None:
        self.sides = sides
        self.mod = mod
        self.times = times

    @measure_time
    def roll(self) -> List[str]:
        results: List[str] = []
        for _ in range(self.times):
            roll = randint(1, self.sides)
            results.append(f"{roll} + {self.mod} = {roll + self.mod}")
        return results

# Main function with test cases
def main() -> None:
    # Function-based tests
    print(d20())
    print(d20(10))
    print(d20(2, 5))

    # Dictionary-based test (manual timing for dictionary-based rolls)
    start_time = time.perf_counter()
    print(roll["d20"]())
    end_time = time.perf_counter()
    print(f"Execution time for roll['d20']: {end_time - start_time:.8f} seconds")

    # Class-based test
    dice_roller = DiceRoller(20, 2, 5)
    dice_roller.roll()

if __name__ == "__main__":
    main()
