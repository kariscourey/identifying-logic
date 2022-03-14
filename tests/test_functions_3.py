from problems.identifying_functions_3 import add_new_customer, Customer, Mailer

# test case with add_to_mailing list = True
def test_add_new_customer_1():
    customer = Customer("Paul")
    add_new_customer(customer)
    assert customer.has_account == True

def test_add_new_customer_2():
    customer = Customer("Paul")
    add_new_customer(customer)
    assert Mailer.customer_received_welcome_email(customer) == True

def test_add_new_customer_3():
    customer = Customer("Paul")
    add_new_customer(customer)
    assert Mailer.customer_on_mailing_list(customer) == True

# test case with add_to_mailing list = False
def test_add_new_customer_4():
    customer = Customer("Jimi")
    add_new_customer(customer, False)
    assert customer.has_account == True

def test_add_new_customer_5():
    customer = Customer("Jimi")
    add_new_customer(customer, False)
    assert Mailer.customer_received_welcome_email(customer) == True

def test_add_new_customer_6():
    customer = Customer("Jimi")
    add_new_customer(customer, False)
    assert Mailer.customer_on_mailing_list(customer) == False

    