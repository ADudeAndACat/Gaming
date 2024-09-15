from random import randint
from typing import List, Dict

# Roll a stat (3d6) for basic DCC stats
def rollstat() -> int:
    return randint(3, 18)

# Roll a Pathfinder stat using the highest 3 out of 4d6
def rollpfstat() -> int:
    rolls: List[int] = [randint(1, 6) for _ in range(4)]
    highest_to_lowest_top3: List[int] = sorted(rolls, reverse=True)[:3]
    return sum(highest_to_lowest_top3)

# Generate and print 6 Pathfinder stats
def makepfstats() -> None:
    print([rollpfstat() for _ in range(6)])

# Generate DCC stats and print them formatted
def makedccstats() -> None:
    stats: str = (
        f"Str: {rollstat()}\n"
        f"Agi: {rollstat()}\n"
        f"Sta: {rollstat()}\n"
        f"Per: {rollstat()}\n"
        f"Int: {rollstat()}\n"
        f"Luck: {rollstat()}"
    )
    print(stats)

# Generate DCC stats and return them as a dictionary
def makemoredccstats() -> Dict[str, int]:
    return {
        "Str": rollstat(),
        "Agi": rollstat(),
        "Sta": rollstat(),
        "Per": rollstat(),
        "Int": rollstat(),
        "Luck": rollstat(),
    }

def main() -> None:
    makepfstats()

if __name__ == "__main__":
    main()
