'''Implement a class called BankAccount that represents a bank account. The class should have private 2 attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account 3 balance. Ensure that the account balance 4 cannot be accessed directly from outside the class. Write a program to create an instance of the 5 BankAccount class and test the deposit and withdrawal functionality.'''

class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self._account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._account_balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account Balance for {self._account_holder_name}: ${self._account_balance}")

# Creating an instance of BankAccount
account = BankAccount("123456789", "John Doe", 1000.00)

# Testing deposit and withdrawal functionality
account.display_balance()
account.deposit(500.00)
account.withdraw(200.00)
account.display_balance()