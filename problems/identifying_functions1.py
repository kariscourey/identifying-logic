
class Customer:
    def __init__(self, name, club_member=False):
        self.name = name
        self.club_member = club_member
        self.purchases = []
    
    def is_club_member(self):
        return self.club_member

    def purchases(self):
        return self.purchases


def calculate_discount(customer):
    purchases = customer.purchases()
    if customer.is_club_member() or len(purchases) == 0:
        return 0.1
    return 0.0
    