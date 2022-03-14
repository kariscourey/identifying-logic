from problems.identifying_loops_1 import stringify_list

# test: list is same length.
def test_stringify_list1():
    lst = [None, 1, {}, []]
    result = stringify_list(lst)
    assert len(lst) == len(result)


# test: turns None into a string
def test_stringify_list2():
    lst = [None, 1, {}, []]
    result = stringify_list(lst)
    assert result[0] == "None"


# test: turns integers into strings
def test_stringify_list3():
    lst = [1, 1, {}, []]
    result = stringify_list(lst)
    assert result[0] == "1"
