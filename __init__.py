"""
Gaming Utilities Package

A collection of utilities for tabletop gaming, featuring dice simulation,
character generation, healing calculators, and crafting tools.
"""

__version__ = '1.0.0'
__author__ = 'Gaming Utilities Team'

# Export primary functions from each module
from .diceroller import d4, d6, d8, d10, d12, d20, d100, roll, roll_with_advantage, roll_with_disadvantage
from .diceroller_class import DiceRoller
from .diceroller_dictionary import roll_and_log
from .statsmaker import rollstat, makepfstats, makedccstats, makeriftsstats, makeriftsstats_set
from .crafting import crafting
from .heals import cure

# Make utility modules available to resolve import errors
from . import config
from . import utils

# Define what gets imported with "from Gaming import *"
__all__ = [
    # Dice rollers
    'd4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100', 
    'roll', 'roll_with_advantage', 'roll_with_disadvantage',
    'DiceRoller', 'roll_and_log',
    
    # Character stats
    'rollstat', 'makepfstats', 'makedccstats', 'makeriftsstats', 'makeriftsstats_set',
    
    # Game mechanics
    'crafting', 'cure',
    
    # Core modules
    'config', 'utils'
]

def main() -> None:
    """
    Demonstrate the functionality of the Gaming package.
    
    Provides examples of the core modules and functions.
    """
    print("Gaming Utilities Package Demonstration")
    print("================================")
    
    print("\n1. Rolling Dice:")
    print(f"  d20 roll: {d20()}")
    print(f"  3d6 roll: {[d6() for _ in range(3)]}")
    
    print("\n2. Character Stats:")
    print(f"  Pathfinder Stats: {makepfstats()}")
    
    print("\n3. Healing Spells:")
    messages, total = cure("light", 1)
    print(f"  Cure Light Wounds: {total} HP ({messages[0]})")
    
    print("\n4. Crafting Calculator:")
    print(f"  Simple craft (DC 15): {crafting(15, 15, 50)}")
    
    print("\nFor more demonstrations, run each module individually.")

if __name__ == "__main__":
    main()
