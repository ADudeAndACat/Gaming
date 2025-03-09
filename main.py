"""
Main entry point for the Gaming Utilities package.
This file demonstrates the usage of all available modules and their functions.
"""

from diceroller import d20, d12, d10, d8, d6, d4, d100
from diceroller_class import DiceRoller
from diceroller_dictionary import roll, roll_and_log
from statsmaker import makepfstats, makedccstats, makemoredccstats
from heals import clw, cmw, csw, ccw
from crafting import crafting
# Import demo functions from demo.py
from demo import (demonstrate_dice_rolling, demonstrate_dictionary_rolls,
                 demonstrate_character_stats, demonstrate_healing,
                 demonstrate_crafting, run_demonstrations, tustleby_attack)

def main():
    clw(12)
    

if __name__ == "__main__":
    main()
