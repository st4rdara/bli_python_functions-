def add(first_number, second_number):
    """Add two numbers."""
    return first_number + second_number


def subtract(first_number, second_number):
    """Subtract the second number from the first."""
    return first_number - second_number


def multiply(first_number, second_number):
    """Multiply two numbers."""
    return first_number * second_number


def divide(first_number, second_number):
    """Divide the first number by the second."""
    if second_number == 0:
        raise ValueError("You cannot divide by zero.")
    return first_number / second_number


def power(base, exponent=2):
    """Raise a number to a given power."""
    return base ** exponent


def square_root(number):
    """Calculate the square root of a number."""
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return number ** 0.5


def percentage(number, percent):
    """Calculate a percentage of a number."""
    return number * percent / 100


def get_number(message):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    """Run the scientific calculator."""

    while True:
        print("\n==========================")
        print("   SCIENTIFIC CALCULATOR")
        print("==========================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Percentage")
        print("8. Exit")
        print("==========================")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                first_number = get_number("Enter first number: ")
                second_number = get_number("Enter second number: ")
                result = add(first_number, second_number)
                print("Result:", result)

            elif choice == "2":
                first_number = get_number("Enter first number: ")
                second_number = get_number("Enter second number: ")
                result = subtract(first_number, second_number)
                print("Result:", result)

            elif choice == "3":
                first_number = get_number("Enter first number: ")
                second_number = get_number("Enter second number: ")
                result = multiply(first_number, second_number)
                print("Result:", result)

            elif choice == "4":
                first_number = get_number("Enter first number: ")
                second_number = get_number("Enter second number: ")
                result = divide(first_number, second_number)
                print("Result:", result)

            elif choice == "5":
                base = get_number("Enter the base: ")
                exponent_input = input(
                        "Enter the exponent:"
                )

                if exponent_input == "":
                    result = power(base)
                else:
                    exponent = float(exponent_input)
                    result = power(base, exponent)

                print("Result:", result)

            elif choice == "6":
                number = get_number("Enter a number: ")
                result = square_root(number)
                print("Result:", result)

            elif choice == "7":
                number = get_number("Enter the number: ")
                percent = get_number("Enter the percentage: ")
                result = percentage(number, percent)
                print("Result:", result)

            elif choice == "8":
                print("Thank you for using the Scientific Calculator!")
                break

            else:
                print("Invalid choice. Please select a number from 1 to 8.")

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
