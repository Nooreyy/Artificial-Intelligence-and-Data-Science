'''A bank system needs to manage customer accounts.

Create a class called BankAccount with the following:

Attributes:

account_holder
balance
Methods:

deposit(amount) → adds money to balance
withdraw(amount) → subtracts money from balance
show_balance() → displays current balance
Create an object and perform one deposit and one withdrawal, then display the final balance.

'''

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def show_balance(self):
        print(f"Current balance for {self.account_holder}: ${self.balance}")

# Create an object of BankAccount
account = BankAccount("John Doe")
# Perform a deposit
account.deposit(500)
# Perform a withdrawal
account.withdraw(200)
# Display the final balance
account.show_balance()
