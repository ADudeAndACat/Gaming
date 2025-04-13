"""
Main entry point for the Gaming Utilities package.

This module serves as the central interface for all gaming utilities, providing
access to dice rolling, character stat generation, healing calculations, and crafting
features. It demonstrates the usage of different implementations and tools.
"""

from diceroller import d20, d12, d10, d8, d6, d4, d100
from diceroller_class import DiceRoller
from diceroller_dictionary import roll, roll_and_log
from statsmaker import (
    makepfstats,
    makedccstats,
    makedccstats_alt,
    rollriftsstat,
    makeriftsstats,
    makeriftsstats_set,
)
from heals import clw, cmw, csw, ccw
from crafting import crafting, calculate_crafting_details
from demo import (
    demonstrate_dice_rolling,
    demonstrate_dictionary_rolls,
    demonstrate_character_stats,
    demonstrate_healing,
    demonstrate_crafting,
    demonstrate_rifts_stats,
    run_demonstrations,
    tustleby_attack,
)


def main():
    print(d20(17))

if __name__ == "__main__":
    main()
