from problems.identifying_classes import Invoice, InvoiceItem

def test_total_empty_0tax():
    invoice = Invoice(0)
    assert invoice.get_total() == 0

def test_total_1item_0tax():
    invoice = Invoice(0)
    invoice.add_item(InvoiceItem(3.0, 2))
    assert invoice.get_total() == 6

def test_total_1item_10tax():
    invoice = Invoice(.1)
    invoice.add_item(InvoiceItem(3.0, 2))
    assert invoice.get_total() == 6.6

