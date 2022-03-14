from problems.identifying_ifs_3 import customer_can_skydive

# test: customer is 18 years old
def test_customer_can_skydive1():
    customer = {
        "age": 18,
    }
    assert customer_can_skydive(customer) == True


# test: customer is 99 years old
def test_customer_can_skydive2():
    customer = {
        "age": 99,
    }
    assert customer_can_skydive(customer) == True


# test: customer is 17 and has no consent form or safety class
def test_customer_can_skydive3():
    customer = {
        "age": 17,
    }
    assert customer_can_skydive(customer) == False


# test: customer is 17 and has safety class but no consent form
def test_customer_can_skydive4():
    customer = {
        "age": 17,
        "parental_consent_form": "waiting to receive",
        "safety_class_date": "2022-01-01",
    }
    assert customer_can_skydive(customer) == False


# test: customer is 17 and has consent form but no safety class
def test_customer_can_skydive5():
    customer = {
        "age": 17,
        "parental_consent_form": "signed",
    }
    assert customer_can_skydive(customer) == False


# test: customer is 17 and has safety class and consent form
def test_customer_can_skydive6():
    customer = {
        "age": 17,
        "parental_consent_form": "signed",
        "safety_class_date": "2022-01-01",
    }
    assert customer_can_skydive(customer) == True
