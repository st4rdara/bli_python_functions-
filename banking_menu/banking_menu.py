def display_menu():
    """Display the banking options to the user."""
    print("\n--- Banking Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def get_balance(balance):
    """Display current balance."""
    print(f"Your current balance is: ${balance:}")

def deposit(balance):
    """Handle deposit transactions."""
    try:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print(f"${amount:} deposited successfully.")
        else:
            print("Amount must be greater than zero.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return balance

def withdraw(balance):
    """Handle withdrawal transactions."""
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Insufficient funds.")
        elif amount > 0:
            balance -= amount
            print(f"${amount:} withdrawn successfully.")
        else:
            print("Amount must be greater than zero.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return balance

def main():
    """Run the banking application."""
    # 1. Set the starting balance.
    balance = 1000.00
    
    # 5. Continue until the user chooses Exit.
    while True:
        # 2. Display the menu.
        display_menu()
        
        # 3. Accept the user's choice.
        choice = input("Enter your choice (1-4): ").strip()
        
        # 4. Call the appropriate function.
        if choice == "1":
            get_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you for using the banking application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()
