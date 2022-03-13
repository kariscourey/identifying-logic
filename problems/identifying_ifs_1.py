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

# this is where you should end up
def calculate_discount(customer):
    num_purchases = len(customer.get_purchases())
    if num_purchases == 0 or customer.is_club_member():
        return 0.1
    return 0
