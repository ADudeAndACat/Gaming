from random import randint

def roll_test(dice: int = 1, threshold: int = 1) -> None:
    rolls = [randint(1, 6) for roll in range(dice)]
    hits = 0
    misses = 0

    for roll in rolls:
        if roll == 5 or roll == 6:
            hits += 1
        elif roll == 1:
            misses += 1
    
    is_glitch = misses > (dice // 2)

    if is_glitch and hits == 0:
        test_status = "Critical Glitch"
    elif is_glitch:
        test_status = "Glitch"
    elif hits >= threshold:
        test_status = "Yes"
    else:
        test_status = "No"

    print(f"""
    -- TEST RESULTS --
    Success: {test_status}
    Roll Results: {rolls}
    Hits: {hits}
    Misses: {misses}
    """)

def main() -> None:
    dice_pool = int(input("# of Dice: "))
    threshold = int(input("Threshold: "))
    roll_test(dice_pool, threshold)

if __name__ == "__main__":
    main()