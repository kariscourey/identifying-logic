from problems.identifying_loops_3 import contains

# test: True when target is in the list
def test_stringify_list1():
    lst = ["cat", "dog", "pie"]
    result = contains(lst, "dog")
    assert result is True


# test: False when target is not in the list
def test_stringify_list2():
    lst = ["cat", "dog", "pie"]
    result = contains(lst, "duck")
    assert result is False
