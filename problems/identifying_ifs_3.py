
# this is where the instructor and students will start
def customer_can_skydive(customer):
    pass

# this is where you should end up
def customer_can_skydive(customer):
    if customer["age"] >= 18 or (
        customer.get("parental_consent_form") == "signed" and
        customer.get("safety_class_date") != None
    ):
        return True
    return False
