from random import randint
from typing import List

# Cure (select) Wounds
def cure(wounds: str, level: int, times: int = 1) -> None:
    if level < 1:
        raise ValueError("Level must be 1 or higher.")
    if times < 1:
        raise ValueError("Times must be 1 or higher.")

    results: List[str] = []
    total_healing: int = 0

    for _ in range(times):
        if wounds == "light":
            mod: int = level if level <= 4 else 5
            roll: int = randint(1, 8)
        elif wounds == "moderate":
            mod: int = level if level <= 9 else 10
            roll: int = randint(2, 16)
        elif wounds == "serious":
            mod: int = level if level <= 14 else 15
            roll: int = randint(3, 24)
        elif wounds == "critical":
            mod: int = level if level <= 19 else 20
            roll: int = randint(4, 32)
        else:
            raise ValueError("Invalid wound type specified.")
        
        healing = roll + mod
        total_healing += healing
        results.append(f"{roll} + {mod} = {healing}")

    print(f"{results} -> Cure {wounds.capitalize()} Wounds healed {total_healing} points of damage.")

# Cure Light Wounds
def clw(level: int, times: int = 1) -> None:
    """Cure Light Wounds"""
    cure("light", level, times)

# Cure Moderate Wounds
def cmw(level: int, times: int = 1) -> None:
    """Cure Moderate Wounds"""
    cure("moderate", level, times)

# Cure Serious Wounds
def csw(level: int, times: int = 1) -> None:
    """Cure Serious Wounds"""
    cure("serious", level, times)

# Cure Critical Wounds
def ccw(level: int, times: int = 1) -> None:
    """Cure Critical Wounds"""
    cure("critical", level, times)

def main() -> None:
    ccw(10, 3)

if __name__ == "__main__":
    main()