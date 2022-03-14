from problems.identifying_functions_3 import add_new_customer

def test_add_new_customer_1():
    customer = Customer("Paul")
    add_new_customer(customer)

    assert "account created"
    assert "welcome email sent"
    assert "not added to mailing list"

    