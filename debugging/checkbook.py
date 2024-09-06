#!/usr/bin/python3

class Checkbook:
    """
    A class representing a simple checkbook with deposit, withdraw, and balance checking functionality.
    """

    def __init__(self):
        """
        Initialize the Checkbook with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.

        Args:
            amount (float): The amount to deposit.
        """
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        """
        Print the current balance of the checkbook.
        """
        print(f"Current Balance: ${self.balance:.2f}")

def get_float_input(prompt):
    """
    Repeatedly prompt the user for input until a valid float is entered.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        float: The valid float value entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    """
    The main function that runs the checkbook program.
    It creates a Checkbook instance and handles user interaction.
    """
    cb = Checkbook()
    while True:
        # Prompt the user for action and convert to lowercase for case-insensitive comparison
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        
        if action == 'exit':
            break  # Exit the program
        elif action == 'deposit':
            # Get deposit amount and perform deposit
            amount = get_float_input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            # Get withdrawal amount and perform withdrawal
            amount = get_float_input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            # Display current balance
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
