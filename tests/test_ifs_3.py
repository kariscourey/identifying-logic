from problems.identifying_ifs_3 import customer_can_skydive


def test_customer_can_skydive1():
    customer = {
        "age": 18,
    }
    assert customer_can_skydive(customer) == True

def test_customer_can_skydive2():
    customer = {
        "age": 99,
    }
    assert customer_can_skydive(customer) == True

def test_customer_can_skydive3():
    customer = {
        "age": 17,
    }
    assert customer_can_skydive(customer) == False

def test_customer_can_skydive4():
    customer = {
        "age": 17,
        "parental_consent_form": "waiting to receive",
        "safety_class_date": "2022-01-01"
    }
    assert customer_can_skydive(customer) == False

def test_customer_can_skydive5():
    customer = {
        "age": 17,
        "parental_consent_form": "signed",
    }
    assert customer_can_skydive(customer) == False

def test_customer_can_skydive6():
    customer = {
        "age": 17,
        "parental_consent_form": "signed",
        "safety_class_date": "2022-01-01"
    }
    assert customer_can_skydive(customer) == True
