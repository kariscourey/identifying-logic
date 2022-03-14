"""
class Mailer:
    def add_to_mailing_list(customer):
    def customer_on_mailing_list(customer):   
    def send_welcome_email(customer):
    def customer_received_welcome_email(customer):

"""

"""
Class: Customer
"""


class Customer:
    def __init__(self, name):
        self.name = name
        self.has_account = False
        self.on_mailing_list = False
        self.got_welcome_email = False

    def create_account(self):
        self.has_account = True


"""
Requirements

When a customer signs up:
- create new account
- send welcome email
- add to mailing list, if they opted in

"""

# TODO: Complete this function
def add_new_customer(customer, add_to_mailing_list=True):
    pass





# This is support code, ignore it


class Mailer:
    def add_to_mailing_list(customer):
        customer.on_mailing_list = True

    def customer_on_mailing_list(customer):
        return customer.on_mailing_list

    def send_welcome_email(customer):
        customer.got_welcome_email = True

    def customer_received_welcome_email(customer):
        return customer.got_welcome_email
