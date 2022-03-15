"""
Write a class that meets these requirements.

Name:       SavingsAccount

Parent class: BankAccount

Required state:
   * opening balance, the amount of money in the bank account
   * interest rate, the percent used to calculate the compounded interest

Behavior:
   * get_balance()      # Returns how much is in the bank account
   * deposit(amount)    # Adds money to the current balance
   * withdraw(amount)   # Reduces the current balance by amount
   * compond_interest() # Adds the value of interest_rate * balance to balance (balance must be an integer)
Example:
   account = SavingsAccount(100, 0.05)

   print(account.get_balance())  # prints 100
   account.withdraw(50)
   print(account.get_balance())  # prints 50
   account.deposit(120)
   print(account.get_balance())  # prints 170
   account.compound_interest()
   print(account.get_balance())  # prints ??

"""


# Write your solution here


