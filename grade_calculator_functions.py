def get_integer_input() -> int:
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Error: Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    return f"{number} is an Even number." if number % 2 == 0 else f"{number} is an Odd number."

def main():
    number = get_integer_input()
    result = check_even_odd(number)
    print(result)

if _name_ == "_main_":
    main()