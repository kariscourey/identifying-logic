from problems.identifying_functions_2 import read_json_data


def test_read_json_1():
    data = read_json_data("test.json")
    assert data["foo"] == "bar"
    assert data["list"] == [1, 2, 3]


def test_read_json_2():
    data = read_json_data("none.json")
    assert data == None
