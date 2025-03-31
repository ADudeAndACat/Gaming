"""
Main entry point for the Gaming Utilities package.

This module serves as the central interface for all gaming utilities, providing
access to dice rolling, character stat generation, healing calculations, and crafting
features. It demonstrates the usage of different implementations and tools.
"""

from diceroller import d20, d12, d10, d8, d6, d4, d100
from diceroller_class import DiceRoller
from diceroller_dictionary import roll, roll_and_log
from statsmaker import (makepfstats, makedccstats, makedccstats_alt,
                       rollriftsstat, makeriftsstats, makeriftsstats_set)
from heals import clw, cmw, csw, ccw
from crafting import crafting, calculate_crafting_details
from demo import (demonstrate_dice_rolling, demonstrate_dictionary_rolls,
                 demonstrate_character_stats, demonstrate_healing,
                 demonstrate_crafting, demonstrate_rifts_stats,
                 run_demonstrations, tustleby_attack)

def main():
    """
    Main entry point for the Gaming Utilities package.
    
    Runs demonstrations of all available features to showcase functionality.
    Users can explore different dice rolling implementations, character stat generation,
    healing calculations, and crafting simulations.
    """
    print("Welcome to Gaming Utilities!")
    print("===========================")
    print("Running demonstrations of all features...")
    print()
    
    run_demonstrations()
    
    print()
    print("Demonstrations complete. Thank you for using Gaming Utilities!")

if __name__ == "__main__":
    main()