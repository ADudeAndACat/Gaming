"""
Configuration settings for the Gaming package.

This module centralizes configuration parameters used throughout the package.
"""

# File paths
ROLL_HISTORY_FILE = 'rolls.json'
DATA_DIR = 'data'

# System settings
DEFAULT_DICE_SIDES = [4, 6, 8, 10, 12, 20, 100]

# Game settings
DEFAULT_CRAFT_DC = 20
DEFAULT_CRAFT_PRICE = 100
DEFAULT_CRAFT_BONUS = 5  # Crafter's Fortune bonus

# Stats generation
MIN_STAT_VALUE = 3
MAX_STAT_VALUE = 18
PF_DICE_COUNT = 4  # 4d6 drop lowest for Pathfinder
DCC_DICE_COUNT = 3  # 3d6 for DCC
RIFTS_BONUS_THRESHOLD = 16  # Roll >= 16 gets bonus die

def main() -> None:
    """
    Demonstrate the configuration settings available in this module.
    
    Shows all the centralized configuration parameters that are used
    throughout the Gaming package.
    """
    print("Gaming Package Configuration Settings")
    print("===================================")
    
    print("\nFile Paths:")
    print(f"  Roll History File: {ROLL_HISTORY_FILE}")
    print(f"  Data Directory: {DATA_DIR}")
    
    print("\nSystem Settings:")
    print(f"  Default Dice Sides: {DEFAULT_DICE_SIDES}")
    
    print("\nGame Settings:")
    print(f"  Default Craft DC: {DEFAULT_CRAFT_DC}")
    print(f"  Default Craft Price: {DEFAULT_CRAFT_PRICE} sp")
    print(f"  Crafter's Fortune Bonus: +{DEFAULT_CRAFT_BONUS}")
    
    print("\nStat Generation Settings:")
    print(f"  Minimum Stat Value: {MIN_STAT_VALUE}")
    print(f"  Maximum Stat Value: {MAX_STAT_VALUE}")
    print(f"  Pathfinder Dice Count: {PF_DICE_COUNT}")
    print(f"  DCC Dice Count: {DCC_DICE_COUNT}")
    print(f"  RIFTS Bonus Threshold: {RIFTS_BONUS_THRESHOLD}")
    
    print("\nThis module centralizes configuration parameters used throughout the Gaming package.")
    print("Import specific settings directly from this module to ensure consistency across modules.")

if __name__ == "__main__":
    main()
