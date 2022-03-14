from problems.identifying_loops_2 import longest

# test: returns longest
def test_longest1():
    lst = ["a", "hg", "l"]
    result = longest(lst)
    assert result ==  "hg"

# test: returns empty string when longest is length 0
def test_longest1():
    lst = [""]
    result = longest(lst)
    assert result ==  ""
