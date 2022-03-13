from problems.identifying_ifs1 import Customer, calculate_discount

# test: brand new customer, no purchases, not a club member
def test_calculate_discount1():
    customer = Customer("lyn")
    assert calculate_discount(customer) == 0.1

# test: customer with two purchases, not a club member
def test_calculate_discount2():
    customer = Customer("lyn")
    customer.purchases = [1,2]
    assert calculate_discount(customer) == 0

# test : customer with two purchases, IS a club member
def test_calculate_discount3():
    customer = Customer("lyn")
    customer.purchases = [1,2]
    customer.club_member = True
    assert calculate_discount(customer) == 0.1

# test: new customer, is a club member
def test_calculate_discount4():
    customer = Customer("lyn")
    customer.club_member = True
    assert calculate_discount(customer) == 0.1

