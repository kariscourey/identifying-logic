from problems.identifying_classes import InvoiceItem

def test_item_1():
    item = InvoiceItem(1.00, 1)
    assert item.get_total() == 1.0

def test_item_2():
    item = InvoiceItem(1.13, 4)
    assert item.get_total() == 4.52

