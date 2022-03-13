class Customer:
    def __init__(self, name, club_member=False):
        self.name = name
        self.club_member = club_member
        self.purchases = []

    def is_club_member(self):
        return self.club_member

    def get_purchases(self):
        return self.purchases


# this is where the instructor and students will start
def calculate_discount_start(customer):
    pass


def calculate_discount(customer):
    num_purchases = len(customer.get_purchases())
    if num_purchases == 0 or customer.is_club_member():
        return 0.1
    return 0


"""
# starting point
def calculate_discount(customer):
    pass

# pass the first test
def calculate_discount(customer):
    return 0.1

# pass the second test
def calculate_discount(customer):
    if len(customer.get_purchases()) == 0:
        return 0.1
    return 0

# this is where they should end up
def calculate_discount(customer):
    num_purchases = len(customer.get_purchases())
    if num_purchases == 0 or customer.is_club_member():
        return 0.1
    return 0
"""
