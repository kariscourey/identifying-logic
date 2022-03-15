from problems.identifying_inheritance_2 import SavingsAccount
from problems.identifying_inheritance import BankAccount

# test_init  

def test_init  ():
    account = SavingsAccount(10, 0.1)
    assert account.balance == 10
    assert account.interest_rate == 0.1

# test_get_balance

def test_get_balance():
    account = SavingsAccount(10, 0.1)
    assert account.get_balance() == 10

# test_withdraw

def test_withdraw():
    account = SavingsAccount(10, 0.1)
    account.withdraw(5)
    assert account.balance == 5

# test_deposit

def test_deposit():
    account = SavingsAccount(10, 0.1)
    account.deposit(10)
    assert account.balance == 20

# test_compound_interest_int

def test_interest():
    account = SavingsAccount(10, 0.1)
    account.compound_interest()
    assert type(account.balance) is int

# test_compound_interest

def test_interest():
    account = SavingsAccount(10, 0.1)
    account.compound_interest()
    assert account.balance == 11

# test_is_subclass

def test_is_subclass():
    account = SavingsAccount(10, 0.1)
    assert issubclass(SavingsAccount, BankAccount)
