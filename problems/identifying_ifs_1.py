"""
Class: Customer
"""


class Customer:
    def __init__(self, name, club_member=False):
        self.name = name
        self.club_member = club_member
        self.purchases = []

    def is_club_member(self):
        return self.club_member

    def get_purchases(self):
        return self.purchases


"""
Requirements:

If a customer is _a club member_ or
is a first time customer,
then apply 10% discount to order.
"""

# complete this function based on the requirements
def calculate_discount(customer):
    pass


# this is where you should end up
def calculate_discount_final(customer):
    num_purchases = len(customer.get_purchases())
    if num_purchases == 0 or customer.is_club_member():
        return 0.1
    return 0
