from random import randint
from typing import List, Dict

# Roll a stat (3d6) for basic DCC stats
def rollstat() -> int:
    return randint(3, 18)

def rollstat_until(until: int) -> int:
    attempts = 0
    while True:
        attempts += 1
        result = rollstat()
        if result >= until:
            print(f"Found after {attempts} attempts")
            return result

# Roll a Pathfinder stat using the highest 3 out of 4d6
def rollpfstat() -> int:
    rolls: List[int] = [randint(2, 6) for _ in range(4)]
    highest_to_lowest_top3: List[int] = sorted(rolls, reverse=True)[:3]
    return sum(highest_to_lowest_top3)

def rollpfstat_until(until: int) -> int:
    attempts = 0
    while True:
        attempts += 1
        result = rollpfstat()
        if result >= until:
            print(f"Found after {attempts} attempts")
            return result

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

def makemoredccstats_until(until: Dict[str, int]) -> Dict[str, int]:
    attempts = 0
    while True:
        attempts += 1
        result = makemoredccstats()
        # Return as soon as any stat meets or exceeds its target
        for stat in result:
            if result[stat] >= until[stat]:
                print(f"Found after {attempts} attempts")
                return result

# Generate a single Rifts stat
def makeriftsstat() -> int:
    roll = randint(3, 18)
    if roll >= 16:
        extra = randint(1, 6)
        if extra == 6:
            bonus = randint(1, 6)
            roll += extra + bonus
        else:
            roll += extra
    return roll

def makeriftsstat_until(until: int) -> int:
    attempts = 0
    while True:
        attempts += 1
        result = makeriftsstat()
        if result >= until:
            print(f"Found after {attempts} attempts")
            return result

# Generate 8 random Rifts stats
def makeriftsstats() -> List[int]:
    return [makeriftsstat() for roll in range(8)]

def makeriftsstats_until(until: int) -> List[int]:
    attempts = 0
    while True:
        attempts += 1
        result = makeriftsstats()
        # Return as soon as any stat meets or exceeds the target value
        for stat in result:
            if stat >= until:
                print(f"Found after {attempts} attempts")
                return result

def makeriftsstatsformatted() -> Dict[str, int]:
    return {
        "IQ": makeriftsstat(),
        "ME": makeriftsstat(),
        "MA": makeriftsstat(),
        "PS": makeriftsstat(),
        "PP": makeriftsstat(),
        "PE": makeriftsstat(),
        "PB": makeriftsstat(),
        "Spd": makeriftsstat(),
    }

def makeriftsstatsformatted_until(until: int) -> Dict[str, int]:
    attempts = 0
    while True:
        attempts += 1
        result = makeriftsstatsformatted()
        # Return as soon as any stat meets or exceeds the target value
        for stat in result:
            if result[stat] >= until:
                print(f"Found after {attempts} attempts")
                return result


def main() -> None:
    # Example usage
    print("Rolling Rifts stats until any stat is 18 or higher:")
    stats = makeriftsstats_until(18)
    print(stats)

if __name__ == "__main__":
    main()
