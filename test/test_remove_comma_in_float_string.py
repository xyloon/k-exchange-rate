from kexr.kexr import remove_comma_in_float_string


def test_remove_comma_in_float_string_number_string():
    assert remove_comma_in_float_string("a") is None


def test_remove_comma_in_float_string_number_integer():
    assert remove_comma_in_float_string("1") == 1


def test_remove_comma_in_float_string_number_float():
    assert remove_comma_in_float_string("1.1") == 1.1


def test_remove_comma_in_float_string_number_comma_float():
    assert remove_comma_in_float_string("12,001.1") == 12001.1


def test_remove_comma_in_float_string_number_comma_float_space():
    assert remove_comma_in_float_string("  12,001.1  ") == 12001.1



