"""
class: InvoiceItem

required state:
- price    : unit price of the item
- quantity : the number or amount of the item purchased

methods:
- get_total() : return the line total (price * quantity)

example:
item = InvoiceItem(2.50, 3)
print(item.get_total())     # 7.5

"""

# TODO: implement this class
class InvoiceItem:
    def __init__(self, price, quantity):
        pass

    def get_total(self):
        pass


"""
class Invoice

required state:
- tax_rate       : the tax-rate for this invoice

methods:
- add_item(item) : add an InvoiceItem to this invoice
- get_subtotal() : return the subtotal for all of the items
- get_tax()      : return the tax as a percentage of the subtotal
- get_total()    : return the sum of the subtotal and the taxes

example:
invoice = Invoice(0.1)
invoice.add_item(InvoiceItem(1.1, 2))
invoice.add_item(InvoiceItem(5.0, 1))

print(invoice.get_subtotal()) # 7.2
print(invoice.get_tax())      # 0.72
print(invoice.get_total())    # 7.92

"""

# TODO: implement this class
class Invoice:
    def __init__(self, tax_rate):
        pass

    def add_item(self, item):
        pass

    def get_subtotal(self):
        pass

    def get_tax(self):
        pass

    def get_total(self):
        pass
    

