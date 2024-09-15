from random import randint

def rollstat():
    # print(randint(3, 18))
    return randint(3, 18)

def rollpfstat():
    rolls = [randint(3, 6) for _ in range(4)]
    highest_to_lowest_top3 = sorted(rolls, reverse=True)[:3]
    stat = sum(highest_to_lowest_top3)
    return stat

def makepfstats():
    print([rollpfstat() for _ in range(6)])

def makedccstats():
    stats = f"Str: {rollstat()} \nAgi: {rollstat()} \nSta: {rollstat()} \nPer: {rollstat()} \nInt: {rollstat()} \nLuck: {rollstat()}"
    print(stats)
    # return stats

def makemoredccstats():
    stats = {
        "Str": rollstat(),
        "Agi": rollstat(),
        "Sta": rollstat(),
        "Per": rollstat(),
        "Int": rollstat(),
        "Luck": rollstat(),
    }
    return stats

def main():
    makepfstats()

if __name__ == "__main__":
    main()