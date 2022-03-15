# Write a class that meets these requirements.
#
# Name:       BankAccount
#
# Required state:
#    * opening balance, the amount of money in the bank account
#
# Behavior:
#    * get_balance()      # Returns how much is in the bank account
#    * deposit(amount)    # Adds money to the current balance
#    * withdraw(amount)   # Reduces the current balance by amount
#
# Example:
#    account = BankAccount(100)
#
#    print(account.get_balance())  # prints 100
#    account.withdraw(50)
#    print(account.get_balance())  # prints 50
#    account.deposit(120)
#    print(account.get_balance())  # prints 170
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

# class BankAccount:                                          # solution
#     def __init__(self, balance):                            # solution
#         self.balance = balance                              # solution

#     def get_balance(self):                                  # solution
#         return self.balance                                 # solution

#     def withdraw(self, amount):                             # solution
#         self.balance -= amount                              # solution

#     def deposit(self, amount):                              # solution
#         self.balance += amount                              # solution

# TODO: Should we add tests for Bank account?