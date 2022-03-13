from problems.identifying_ifs1 import Customer, calculate_discount

def test_calculate_discount1():
    customer = Customer("lyn")
    assert calculate_discount(customer) == 0.1