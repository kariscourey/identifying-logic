"""
Class: Order
"""


class Order:
    def __init__(self, items, partial_order=False):
        self.items = items
        self.partial_order = partial_order
        self.paid = False

    def num_items(self):
        return len(self.items)

    def items_ready_to_ship(self):
        num_items = self.num_items()
        if num_items == 3:
            return 2
        return num_items

    def is_paid(self):
        return self.paid

    def ship_partial_order(self):
        return self.partial_order


"""
Requirements:

If order has been paid for 
and all items ordered are ready for delivery 
or the order is marked for "individual shipments", 
then ship the items that are ready to ship.
"""


# this is where the instructor and students will start
def order_ready_to_ship(order):
    pass


# this is where you should end up
def order_ready_to_ship_final(order):
    if order.is_paid() and (
        order.num_items() == order.items_ready_to_ship() or order.ship_partial_order()
    ):
        return True
    return False
