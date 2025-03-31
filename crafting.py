"""
Pathfinder crafting calculator for tabletop RPG.

This module provides functions to calculate crafting time, hours needed, and cost
based on Pathfinder RPG crafting rules. It takes into account skill check results,
item difficulty, price, and special modifiers like Crafter's Fortune.
"""

from config import DEFAULT_CRAFT_DC, DEFAULT_CRAFT_PRICE, DEFAULT_CRAFT_BONUS

def crafting(roll: int = 10, dc: int = DEFAULT_CRAFT_DC, 
            price: int = DEFAULT_CRAFT_PRICE, 
            cf_yn: str = "n", 
            acc: int = 0) -> str:
    """
    Calculate crafting time, hours, and cost based on Pathfinder crafting rules.
    
    The formula used is: (roll * DC) / price = days to craft
    
    Args:
        roll (int, optional): Craft skill check result. Defaults to 10.
        dc (int, optional): Difficulty class (DC) of the item. Defaults to 20.
        price (int, optional): Price of the item in silver pieces. Defaults to 100.
        cf_yn (str, optional): Whether Crafter's Fortune is active ('y' or 'n'). Defaults to "n".
        acc (int, optional): Acceleration bonus to crafting speed. Defaults to 0.
    
    Returns:
        str: Formatted string with days, hours, and cost
    """
    # Apply Crafter's Fortune bonus if applicable
    cf_bonus: int = DEFAULT_CRAFT_BONUS if cf_yn.lower() == 'y' else 0

    # Calculate days, hours, and cost
    days: float = ((roll + cf_bonus) * (dc + acc)) / price
    hours: float = days * 24
    cost: float = price / 3

    # Return the formatted result, rounding to two decimal places
    return f"{round(days, 2)} days / {round(hours, 2)} hours / {round(cost, 2)} sp"

def calculate_crafting_details(roll: int, dc: int, price: int, 
                               cf_yn: str = "n", 
                               acc: int = 0) -> tuple[float, float, float]:
    """
    Calculate detailed crafting metrics.
    
    Similar to the crafting function but returns values as a tuple instead of formatted string.
    
    Args:
        roll (int): Craft skill check result.
        dc (int): Difficulty class (DC) of the item.
        price (int): Price of the item in silver pieces.
        cf_yn (str, optional): Whether Crafter's Fortune is active ('y' or 'n'). Defaults to "n".
        acc (int, optional): Acceleration bonus to crafting speed. Defaults to 0.
        
    Returns:
        tuple[float, float, float]: A tuple containing (days, hours, cost)
    """
    # Apply Crafter's Fortune bonus if applicable
    cf_bonus: int = DEFAULT_CRAFT_BONUS if cf_yn.lower() == 'y' else 0

    # Calculate days, hours, and cost
    days: float = ((roll + cf_bonus) * (dc + acc)) / price
    hours: float = days * 24
    cost: float = price / 3
    
    return (days, hours, cost)

def main() -> None:
    """
    Interactive console interface for the crafting calculator.
    
    Prompts the user for input values and displays the crafting results.
    """
    print("Pathfinder Crafting Calculator")
    print("------------------------------")
    
    # Get inputs from the user
    try:
        roll = int(input("Roll (craft check result): "))
        dc = int(input(f"DC (difficulty class, default {DEFAULT_CRAFT_DC}): ") or DEFAULT_CRAFT_DC)
        price = int(input(f"Price in silver pieces (default {DEFAULT_CRAFT_PRICE}): ") or DEFAULT_CRAFT_PRICE)
        cf_yn = input("Crafter's Fortune active? (y/n, default n): ") or "n"
        acc_input = input("Acceleration modifier (default 0): ") or "0"
        acc = int(acc_input) * 10  # Convert to the acceleration bonus
        
        # Display the result of crafting
        result = crafting(roll, dc, price, cf_yn, acc)
        print("\nCrafting Result:")
        print(result)
        
    except ValueError as e:
        print(f"Error: Please enter valid numbers for roll, DC, price, and acceleration. {e}")

if __name__ == '__main__':
    main()
