"""
Class: Customer
"""
class Customer:
    def __init__(self, name):
        self.name = name
        self.has_account = False
        self.on_mailing_list = False;
        self.purchases = []

    def create_account(self):
        self.has_account = True

    def add_to_mailing_listp

class Mailer:
    def add_to_mailing_list(customer):
        customer.mailing_list = True
    def customer_on_mailing_list(customer):
        return customer.mailing_list
        
"""
Requirements

When a customer signs up:
create new account
send welcome email
add to mailing list, if they opted in

"""

def add_new_customer(customer, add_to_mailing_list=True):
    # 1 - create new account

    # 2 - send welcome email

    # 3 - add to mailing list
    if add_to_mailing_list:
        # ...

