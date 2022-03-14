"""
A customer dictionary will look like this:

customer = {
    "age": integer,
    "parental_consent_form": "signed", # anything else doesn't count
    "safety_class_date": "2001-01-01", # anything other than None counts
}

The age field is guaranteed to exist, but the
others may or may not be present.
"""


"""
Requirements:

If a person is an adult 
or has a parental consent form 
and has taken a safety class, 
they they may sign up for sky diving

"""

# this is where the instructor and students will start
def customer_can_skydive(customer):
    pass


# this is where you should end up
def customer_can_skydive_final(customer):
    if customer["age"] >= 18 or (
        customer.get("parental_consent_form") == "signed" and
        customer.get("safety_class_date") != None
    ):
        return True
    return False
