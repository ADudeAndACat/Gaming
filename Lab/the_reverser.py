def reverse_input(user_input: str) -> str:
    if isinstance(user_input, str):
        print(user_input[::-1])
    else:
        print(str(user_input)[::-1])

def main():
    user_input = input("Enter a string: ")
    reverse_input(user_input)

if __name__ == "__main__":
    main()

