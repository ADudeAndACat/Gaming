# Get inputs from the user or another source
ROLL = int(input("Roll: "))
LEVEL = int(input("Alchemist level: "))
DC = int(input("DC: "))
PRICE = int(input("Price (sp): "))
CF_yn = input("Crafter's Fortune (Y/N): ")
SWIFT_ALCH = input("Swift Alchemy (Y/N): ")
ACC = int(input("Acceleration (+10 x?): ")) * 10

def craftc(ROLL: int = 10, LEVEL: int = 0, DC: int = 20, PRICE: int = 100, CF_yn: str = "n", ACC: int = 1,
           SWIFT_ALCH: str = "n") -> str:
    # Constants and variables
    if CF_yn.lower() == "y":
        CF: int = 5
    else:
        CF: int = 0

    if SWIFT_ALCH.lower() == "y":
        week: int = 3.5
    else:
        week: int = 7

    # Calculations
    days: float = week / ((((ROLL + LEVEL) + CF) * (DC + ACC)) / PRICE)
    hours: float = days * 24
    cost: float = PRICE / 3

    # Round the float values to two decimal places
    days = round(days, 2)
    hours = round(hours, 2)
    cost = round(cost, 2)

    return f"TIME: {days} days ({hours} hours) / COST: {cost} sp"


# Call the function with the provided arguments
result = craftc(ROLL, LEVEL, DC, PRICE, CF_yn, ACC, SWIFT_ALCH)
print(result)