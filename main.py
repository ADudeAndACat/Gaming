"""
Main entry point for the Gaming Utilities package.
This file demonstrates the usage of all available modules and their functions.
"""

from diceroller import d20, d12, d10, d8, d6, d4, d100
from diceroller_class import DiceRoller
from statsmaker import makepfstats, makedccstats, makemoredccstats
from heals import clw, cmw, csw, ccw
from crafting import crafting

def demonstrate_dice_rolling():
    """Demonstrate different dice rolling implementations"""
    print("\n=== Dice Rolling Demonstrations ===")
    
    # Functional implementation
    print("\nFunctional Implementation:")
    print("Rolling d20 with +5 modifier:", d20(5))
    print("Rolling 4d6:", d6(times=4))
    print("Rolling d100:", d100())

    # Class-based implementation
    print("\nClass-based Implementation:")
    d20_roller = DiceRoller(20)
    print("Rolling d20:", d20_roller.roll())
    
    # Multiple dice types
    print("\nVarious Dice Types:")
    print("d4:", d4())
    print("d6:", d6())
    print("d8:", d8())
    print("d10:", d10())
    print("d12:", d12())

def demonstrate_character_stats():
    """Demonstrate character stat generation"""
    print("\n=== Character Stat Generation ===")
    
    print("\nPathfinder Stats:")
    makepfstats()
    
    print("\nDungeon Crawl Classics Stats:")
    makedccstats()
    
    print("\nDetailed DCC Stats:")
    dcc_stats = makemoredccstats()
    for stat, value in dcc_stats.items():
        print(f"{stat}: {value}")

def demonstrate_healing():
    """Demonstrate healing spell calculations"""
    print("\n=== Healing Spells ===")
    
    print("\nCure Light Wounds (Level 3):")
    clw(3)
    
    print("\nCure Moderate Wounds (Level 5):")
    cmw(5)
    
    print("\nCure Serious Wounds (Level 7):")
    csw(7)
    
    print("\nCure Critical Wounds (Level 9):")
    ccw(9)

def demonstrate_crafting():
    """Demonstrate crafting calculations"""
    print("\n=== Crafting Calculator ===")
    
    # Example crafting calculation
    result = crafting(roll=15, dc=20, price=100, cf_yn='y', acc=20)
    print("\nCrafting Result (Roll=15, DC=20, Price=100sp, with Crafter's Fortune):")
    print(result)

def main():
    """Main function demonstrating all utilities"""
    print("=== Gaming Utilities Demonstration ===")
    
    while True:
        print("\nAvailable Demonstrations:")
        print("1. Dice Rolling")
        print("2. Character Stats")
        print("3. Healing Spells")
        print("4. Crafting")
        print("5. Run All Demonstrations")
        print("0. Exit")
        
        choice = input("\nSelect a demonstration (0-5): ")
        
        if choice == '1':
            demonstrate_dice_rolling()
        elif choice == '2':
            demonstrate_character_stats()
        elif choice == '3':
            demonstrate_healing()
        elif choice == '4':
            demonstrate_crafting()
        elif choice == '5':
            demonstrate_dice_rolling()
            demonstrate_character_stats()
            demonstrate_healing()
            demonstrate_crafting()
        elif choice == '0':
            print("\nExiting Gaming Utilities. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
