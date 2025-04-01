"""
A module for generating character statistics for various RPG systems.

This module provides functions for generating character ability scores for different
tabletop RPG systems, including Pathfinder, Dungeon Crawl Classics (DCC), and Rifts.
Each system implements its own set of generation rules and stat formats.
"""

from random import randint
from typing import List, Dict

def rollstat() -> int:
    """
    Roll a single stat using 3d6 (3-18 range).
    
    Returns:
        int: A random number between 3 and 18, inclusive.
    """
    return randint(3, 18)

def rollstat_until(until: int) -> int:
    """
    Keep rolling 3d6 until a stat >= until is achieved.
    
    Args:
        until (int): The target value to reach or exceed.
        
    Returns:
        int: The first stat that meets or exceeds the target value.
    """
    attempts = 0
    while True:
        attempts += 1
        stat = rollstat()
        if stat >= until:
            print(f"Found stat >= {until} after {attempts} attempts")
            return stat
        elif attempts % 100 == 0:  # Print progress every 100 attempts
            print(f"Still trying... {attempts} attempts so far")

def rollpfstat() -> int:
    """
    Roll a single Pathfinder stat using 4d6, dropping the lowest die.
    
    Returns:
        int: Sum of the highest three dice (range 3-18).
    """
    rolls: list[int] = [randint(1, 6) for _ in range(4)]
    highest_to_lowest_top3: list[int] = sorted(rolls, reverse=True)[:3]
    return sum(highest_to_lowest_top3)

def rollpfstat_until(until: int) -> int:
    """
    Keep rolling Pathfinder stats until one >= until is achieved.
    
    Args:
        until (int): The target value to reach or exceed.
        
    Returns:
        int: The first Pathfinder stat that meets or exceeds the target value.
    """
    attempts = 0
    while True:
        attempts += 1
        stat = rollpfstat()
        if stat >= until:
            print(f"Found Pathfinder stat >= {until} after {attempts} attempts")
            return stat
        elif attempts % 100 == 0:  # Print progress every 100 attempts
            print(f"Still trying... {attempts} attempts so far")

def makepfstats() -> list[int]:
    """
    Generate a complete set of 6 Pathfinder ability scores.
    
    Returns:
        list[int]: A list of 6 Pathfinder ability scores.
    """
    return [rollpfstat() for _ in range(6)]

def makepfstats_until(until: int) -> list[int]:
    """
    Generate Pathfinder stats until at least one meets or exceeds the target.
    
    Args:
        until (int): The target value to reach or exceed.
        
    Returns:
        list[int]: The first set of 6 stats where at least one meets/exceeds the target.
    """
    attempts = 0
    while True:
        attempts += 1
        stats = makepfstats()
        if max(stats) >= until:
            print(f"Found at least one stat >= {until} after {attempts} attempts")
            return stats
        elif attempts % 100 == 0:  # Print progress every 100 attempts
            print(f"Still trying... {attempts} sets generated so far")

def makedccstats() -> dict[str, int]:
    """
    Generate a complete set of DCC ability scores.
    
    Returns:
        dict[str, int]: Dictionary containing all DCC ability scores.
    """
    return {
        "Strength": rollstat(),
        "Agility": rollstat(),
        "Stamina": rollstat(),
        "Personality": rollstat(),
        "Intelligence": rollstat(),
        "Luck": rollstat()
    }

def makedccstats_until(until: int) -> dict[str, int]:
    """
    Generate DCC stats until at least one meets or exceeds the target.
    
    Args:
        until (int): The target value to reach or exceed.
        
    Returns:
        dict[str, int]: The first set of DCC stats where at least one meets/exceeds the target.
    """
    attempts = 0
    while True:
        attempts += 1
        stats = makedccstats()
        if max(stats.values()) >= until:
            print(f"Found DCC stats with one >= {until} after {attempts} attempts")
            return stats
        elif attempts % 100 == 0:  # Print progress every 100 attempts
            print(f"Still trying... {attempts} attempts so far")

def makedccstats_alt() -> dict[str, int]:
    """
    Generate a complete set of DCC ability scores (alternative implementation).
    
    Returns:
        dict[str, int]: Dictionary containing all DCC ability scores.
    """
    stats = {}
    for stat in ["Strength", "Agility", "Stamina", "Personality", "Intelligence", "Luck"]:
        stats[stat] = rollstat()
    return stats

def makedccstats_alt_until(until: int) -> dict[str, int]:
    """
    Generate DCC stats until at least one meets or exceeds the target.
    
    Args:
        until (int): The target value to reach or exceed.
        
    Returns:
        dict[str, int]: The first set of DCC stats where at least one meets/exceeds the target.
    """
    attempts = 0
    while True:
        attempts += 1
        stats = makedccstats_alt()
        if max(stats.values()) >= until:
            print(f"Found DCC stats with one >= {until} after {attempts} attempts")
            return stats
        elif attempts % 100 == 0:  # Print progress every 100 attempts
            print(f"Still trying... {attempts} attempts so far")

def rollriftsstat() -> int:
    """
    Roll a single Rifts stat with special rules for high rolls.
    If roll >= 16, add 1d6. If that d6 is 6, add another 1d6.
    
    Returns:
        int: The final stat value, potentially enhanced by bonus rolls.
    """
    roll = randint(3, 18)
    if roll >= 16:
        extra = randint(1, 6)
        if extra == 6:
            bonus = randint(1, 6)
            return roll + extra + bonus
        return roll + extra
    return roll

def rollriftsstat_until(until: int) -> int:
    """
    Keep rolling Rifts stats until one >= until is achieved.
    
    Args:
        until (int): The target value to reach or exceed.
        
    Returns:
        int: The first Rifts stat that meets or exceeds the target value.
    """
    attempts = 0
    while True:
        attempts += 1
        stat = rollriftsstat()
        if stat >= until:
            print(f"Found Rifts stat >= {until} after {attempts} attempts")
            return stat
        elif attempts % 100 == 0:  # Print progress every 100 attempts
            print(f"Still trying... {attempts} attempts so far")

def makeriftsstats() -> list[int]:
    """
    Generate a complete set of 8 Rifts ability scores.
    
    Returns:
        list[int]: A list of 8 Rifts ability scores.
    """
    return [rollriftsstat() for _ in range(8)]

def makeriftsstats_set() -> dict[str, int]:
    """
    Generate a complete set of Rifts ability scores with named attributes.
    
    Returns:
        dict[str, int]: Dictionary containing all Rifts ability scores with their names.
    """
    stats = makeriftsstats()
    return {
        "IQ": stats[0],
        "ME": stats[1],
        "MA": stats[2],
        "PS": stats[3],
        "PP": stats[4],
        "PE": stats[5],
        "PB": stats[6],
        "Spd": stats[7]
    }

def makeriftsstats_set_until(until: int) -> dict[str, int]:
    """
    Generate Rifts stats until at least one meets or exceeds the target.
    
    Args:
        until (int): The target value to reach or exceed.
        
    Returns:
        dict[str, int]: The first set of Rifts stats where at least one meets/exceeds the target.
    """
    attempts = 0
    while True:
        attempts += 1
        stats = makeriftsstats_set()
        if max(stats.values()) >= until:
            print(f"Found Rifts stats with one >= {until} after {attempts} attempts")
            return stats
        elif attempts % 100 == 0:  # Print progress every 100 attempts
            print(f"Still trying... {attempts} attempts so far")

def main() -> None:
    """
    Demonstrate the usage of various stat generation functions.
    
    Shows examples of generating character stats for different RPG systems
    using various rolling methods.
    """
    print("Character Stat Generator Demonstration")
    print("====================================")
    
    print("\n1. Basic Roll Method:")
    print(f"Standard 3d6 roll: {rollstat()}")
    
    print("\n2. Pathfinder Stats (4d6 drop lowest):")
    pf_stats = makepfstats()
    print(f"Full stat array: {pf_stats}")
    print("Individual stats:")
    for i, stat in enumerate(['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']):
        print(f"  {stat}: {pf_stats[i]}")
    
    print("\n3. Dungeon Crawl Classics Stats (3d6):")
    dcc_stats = makedccstats()
    print(f"Stats by name: {dcc_stats}")
    
    print("\n4. Alternative DCC Stats (detailed format):")
    dcc_alt_stats = makedccstats_alt()
    for stat_name, stat_value in dcc_alt_stats.items():
        print(f"  {stat_name}: {stat_value}")
    
    print("\n5. Rifts RPG Stats:")
    print(f"Single Rifts stat roll: {rollriftsstat()}")
    
    print("\n6. Complete Rifts Stats (array):")
    rifts_stats = makeriftsstats()
    print(f"Stat array: {rifts_stats}")
    
    print("\n7. Complete Rifts Stats (with names):")
    rifts_named_stats = makeriftsstats_set()
    for stat_name, stat_value in rifts_named_stats.items():
        print(f"  {stat_name}: {stat_value}")
    
    print("\nThis module provides various methods for generating character stats")
    print("for different tabletop role-playing game systems.")

if __name__ == "__main__":
    main()
