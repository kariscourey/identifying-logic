

def customer_can_skydive(customer):
    if customer["age"] >= 18 or (
        customer.get("parental_consent_form") == "signed" and
        customer.get("safety_class_date") != None
    ):
        return True
    return False