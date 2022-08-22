
class BankAccount:
    def __init__(self, opening_balance):
        self.balance = opening_balance  # need to store arg
        self.transactions = []

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        self.transactions.append(-amount)
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.transactions.append(amount)
        self.balance += amount
        return self.balance

class StatementMixin():  # doesn't need an init, only inherited; mixes methods into other classes

    # balance = 0  # static property

    def __init__(self):
        print("This is statementmixin's dunder init")

    def print_statement(self):
        print(type(self))  # prints "class ...SavingsAccount because SA inherits from statement -- self will always be the thing to the left of the dot"
        print(f"Balance = {self.balance}")
        for transaction in self.transactions:
            print(transaction)

    # def get_balance():
    #     pass  # wouldn't call because BankAccount is inherited in SavingsAccount first


# Bart doesn't suggest using StatementMixin (or any other mixins, for that matter)

# SavingsAccount is a subclass of BankAccount, StatementMixin
class SavingsAccount(BankAccount, StatementMixin): # multiple inheritance
    def __init__(self, opening_balance, interest_rate):
        # delegated setting the balance to the super class (BankAccount)
        # self.balance = opening_balance # already in BankAccount, unnecessary
        # set interest rate
        self.interest_rate = interest_rate

    def compound_interest(self):
        self.balance = self.balance + self.balance * self.interest_rate

    def get_balance(self):
        balance = super().get_balance()
        return "You've been hacked and your balance is " + str(balance)
    #     print("You've been hacked!")
    #     return "You've been hacked!"

    # get balance in sub class overrode that in super class




account = BankAccount(100)
# print(account.__dict__)  # takes instance of bank account and converts to dictionary
print(account.get_balance())

print(account.get_balance())
account.withdraw(50)
print(account.get_balance())
account.deposit(120)
print(account.get_balance())


account2 = BankAccount(0)
print(account2.get_balance())


account3 = SavingsAccount(1000, 0.05)

print(account3.get_balance())
account3.withdraw(454)
print(account3.get_balance())
account3.deposit(143)
print(account3.get_balance())
account3.compound_interest()
print(account3.get_balance())
account3.print_statement()
