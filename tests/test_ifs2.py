from problems.identifying_ifs2 import Order, order_ready_to_ship

# test: order is NOT paid, has 2 items, both items ready to ship
def test_order_ready1():
    order = Order([1,2])
    assert order_ready_to_ship(order) == False

# test: order is paid, has 2 items, both items ready to ship
def test_order_ready2():
    order = Order([1,2])
    order.paid = True
    assert order_ready_to_ship(order) == True

# test: order is not paid, has 3 items, only two items ready to ship
def test_order_ready3():
    order = Order([1,2,3])
    assert order_ready_to_ship(order) == False

# test: order is paid, has 3 items, only two items ready to ship
def test_order_ready4():
    order = Order([1,2,3])
    order.paid = True
    assert order_ready_to_ship(order) == False

# test: order is paid, has 3 items, only two items ready to ship
def test_order_ready5():
    order = Order([1,2,3])
    order.paid = True
    order.partial_order = True
    assert order_ready_to_ship(order) == True



