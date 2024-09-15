def crafting(roll: int = 10, dc: int = 20, price: int = 100, cf_yn: str = "n", acc: int = 0) -> str:
    # Apply Crafter's Fortune bonus if applicable
    cf_bonus: int = 5 if cf_yn.lower() == 'y' else 0

    # Calculate days, hours, and cost
    days: float = ((roll + cf_bonus) * (dc + acc)) / price
    hours: float = days * 24
    cost: float = price / 3

    # Return the formatted result, rounding to two decimal places
    return f"{round(days, 2)} days / {round(hours, 2)} hours / {round(cost, 2)} sp"

def main() -> None:
    # Get inputs from the user
    roll = int(input("Roll: "))
    dc = int(input("DC: "))
    price = int(input("Price (sp): "))
    cf_yn = input("Crafter's Fortune (Y/N): ")
    acc = int(input("Acceleration (x?): ")) * 10

    # Display the result of crafting
    print(crafting(roll, dc, price, cf_yn, acc))

if __name__ == '__main__':
    main()
