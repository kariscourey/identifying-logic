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
    def __init__(self, price, quantity):  # double underscores = dunder, "dunder init"
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity

# create an instance (or copy) of this InvoiceItem class

item = InvoiceItem(2.50, 3)
candy = InvoiceItem(1.00, 10)

print(item.get_total()) # printing an instance of a class yields memory location, name of class
print(candy.get_total())


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

# invoice class is "stubbed out" -- bones are there, but need to finish
# use self when accessing variables outside of current function in class
class Invoice:
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_subtotal(self):
        subtotal = 0

        for item in self.items:  # item is an instance of InvoiceItem
            # add item total to subtotal
            subtotal += item.get_total()
        return subtotal

    def get_tax(self):
        subtotal = self.get_subtotal()
        tax = subtotal * self.tax_rate
        return tax

    def get_total(self):
        subtotal = self.get_subtotal()
        tax = self.get_tax()
        return subtotal + tax


invoice = Invoice(0.1)
invoice.add_item(InvoiceItem(1.1, 2))
invoice.add_item(InvoiceItem(5.0, 1))

print(invoice.get_subtotal()) # 7.2
print(invoice.get_tax())      # 0.72
print(invoice.get_total())    # 7.92

# 1. Python creates an empty object (the instance)
# 2. Python calls __init__ and passes it the instance (self) (used to stick things that we pass things in on the self -- args, init vars, etc.)
# 3. Python attaches all methods to the instance

karis_invoice = Invoice(0.2)  # this calls dunder init
karis_invoice.add_item(InvoiceItem(13, 2))
karis_invoice.add_item(InvoiceItem(670, 1))

print(karis_invoice.get_total())
