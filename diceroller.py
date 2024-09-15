from random import randint

# Main dice rolling function
def d(sides, mod=0, times=1):
    return [f'{die_roll} + {mod} = {die_roll + mod}' for die_roll in [randint(1, sides) for roll in range(times)]]

# Each polyhedron dice
def d20(mod=0, times=1):
    print(d(20, mod, times))

def d4(mod=0, times=1):
    print(d(4, mod, times))

def d6(mod=0, times=1):
    print(d(6, mod, times))

def d8(mod=0, times=1):
    print(d(8, mod, times))

def d10(mod=0, times=1):
    print(d(10, mod, times))

def d12(mod=0, times=1):
    print(d(12, mod, times))

def d100(mod=0, times=1):
    print(d(100, mod, times))


def main():
    d20(16)

if __name__ == "__main__":
    main()