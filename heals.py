"""
Healing spell calculator for tabletop RPGs.

This module provides functions to calculate healing from various 'cure' spells
based on Pathfinder/D&D rules. Each type of healing spell has different dice
and modifier rules based on the caster level.
"""

from random import randint

def cure(wounds: str, level: int, times: int = 1) -> tuple[list[str], int]:
    """
    Calculate healing from a specified 'cure' spell based on the wound severity.

    Args:
        wounds (str): Type of wounds being cured ('light', 'moderate', 'serious', or 'critical').
        level (int): Caster level.
        times (int, optional): Number of times to cast the spell. Defaults to 1.

    Returns:
        tuple[list[str], int]: Tuple containing the list of individual healing results and total healing.
        
    Raises:
        ValueError: If level or times is less than 1, or if an invalid wound type is specified.
    """
    if level < 1:
        raise ValueError("Level must be 1 or higher.")
    if times < 1:
        raise ValueError("Times must be 1 or higher.")

    results: list[str] = []
    total_healing: int = 0

    for _ in range(times):
        dice_roll: int = 0
        level_cap: int = 0
        
        if wounds == "light":
            level_cap = min(level, 5)
            dice_roll = randint(1, 8)
            mod = level_cap
            total = dice_roll + mod
            results.append(f"CLW: {dice_roll} + {mod} = {total}")
            total_healing += total
        elif wounds == "moderate":
            level_cap = min(level, 10)
            roll1 = randint(1, 8)
            roll2 = randint(1, 8)
            mod = level_cap
            total = roll1 + roll2 + mod
            results.append(f"CMW: {roll1} + {roll2} + {mod} = {total}")
            total_healing += total
        elif wounds == "serious":
            level_cap = min(level, 15)
            roll1 = randint(1, 8)
            roll2 = randint(1, 8)
            roll3 = randint(1, 8)
            mod = level_cap
            total = roll1 + roll2 + roll3 + mod
            results.append(f"CSW: {roll1} + {roll2} + {roll3} + {mod} = {total}")
            total_healing += total
        elif wounds == "critical":
            level_cap = min(level, 20)
            roll1 = randint(1, 8)
            roll2 = randint(1, 8)
            roll3 = randint(1, 8)
            roll4 = randint(1, 8)
            mod = level_cap
            total = roll1 + roll2 + roll3 + roll4 + mod
            results.append(f"CCW: {roll1} + {roll2} + {roll3} + {roll4} + {mod} = {total}")
            total_healing += total
        else:
            raise ValueError(f"Unknown wound type: {wounds}")
    
    return results, total_healing


def clw(level: int, times: int = 1) -> tuple[list[str], int]:
    """
    Calculate healing from Cure Light Wounds spell.
    
    Cure Light Wounds heals 1d8 + level (max +5) points of damage.
    
    Args:
        level (int): Caster level.
        times (int, optional): Number of times to cast the spell. Defaults to 1.
        
    Returns:
        tuple[list[str], int]: Tuple containing the list of individual healing results and total healing.
    """
    return cure("light", level, times)


def cmw(level: int, times: int = 1) -> tuple[list[str], int]:
    """
    Calculate healing from Cure Moderate Wounds spell.
    
    Cure Moderate Wounds heals 2d8 + level (max +10) points of damage.
    
    Args:
        level (int): Caster level.
        times (int, optional): Number of times to cast the spell. Defaults to 1.
        
    Returns:
        tuple[list[str], int]: Tuple containing the list of individual healing results and total healing.
    """
    return cure("moderate", level, times)


def csw(level: int, times: int = 1) -> tuple[list[str], int]:
    """
    Calculate healing from Cure Serious Wounds spell.
    
    Cure Serious Wounds heals 3d8 + level (max +15) points of damage.
    
    Args:
        level (int): Caster level.
        times (int, optional): Number of times to cast the spell. Defaults to 1.
        
    Returns:
        tuple[list[str], int]: Tuple containing the list of individual healing results and total healing.
    """
    return cure("serious", level, times)


def ccw(level: int, times: int = 1) -> tuple[list[str], int]:
    """
    Calculate healing from Cure Critical Wounds spell.
    
    Cure Critical Wounds heals 4d8 + level (max +20) points of damage.
    
    Args:
        level (int): Caster level.
        times (int, optional): Number of times to cast the spell. Defaults to 1.
        
    Returns:
        tuple[list[str], int]: Tuple containing the list of individual healing results and total healing.
    """
    return cure("critical", level, times)


def main() -> None:
    """
    Demonstrate the healing spell calculator functions.
    
    Shows examples of casting various cure spells at different levels.
    """
    print("Healing Spell Calculator Demonstration")
    print("=====================================")
    
    print("\nBasic healing spells:")
    print("1. Cure Light Wounds (level 1):")
    results, total = clw(1)
    print(f"   Individual roll: {results}")
    print(f"   Total healing: {total}")
    
    print("\n2. Cure Moderate Wounds (level 5):")
    results, total = cmw(5)
    print(f"   Individual roll: {results}")
    print(f"   Total healing: {total}")
    
    print("\n3. Cure Serious Wounds (level 9):")
    results, total = csw(9)
    print(f"   Individual roll: {results}")
    print(f"   Total healing: {total}")
    
    print("\n4. Cure Critical Wounds (level 12):")
    results, total = ccw(12)
    print(f"   Individual roll: {results}")
    print(f"   Total healing: {total}")
    
    print("\nMultiple castings:")
    print("Casting Cure Light Wounds 3 times at level 3:")
    results, total = clw(3, 3)
    print(f"   Individual rolls: {results}")
    print(f"   Total healing: {total}")
    
    print("\nMaximum level bonuses:")
    print("Cure Light Wounds at level 10 (capped at +5):")
    clw(10)
    
    print("\nThis module calculates healing amounts for different cure spells.")
    print("Each spell uses different dice and has different level caps.")

if __name__ == "__main__":
    main()