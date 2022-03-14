from problems.identifying_functions_1 import celsius_to_f, f_to_celsius


def test_c_to_f_1():
    c = 0.0
    answer = 32.0
    result = celsius_to_f(c)
    assert result == answer


def test_c_to_f_2():
    c = 100.0
    answer = 212.0
    result = celsius_to_f(c)
    assert result == answer


def test_f_to_c_1():
    f = 32.0
    answer = 0.0
    result = f_to_celsius(f)
    assert result == answer


def test_f_to_c_2():
    f = 212.0
    answer = 100.0
    result = f_to_celsius(f)
    assert result == answer
