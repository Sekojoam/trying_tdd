import pytest
from calc.calculator import string_calculator

# TDD Kata: string calculator
# 1. An empty string returns zero
# 2. A single number returns the value
# 3. Two numbers, comma delimited, returns the sum
# 4. Two numbers, newline delimited, returns the sum
# 5. Three numbers, delimited either way, returns the sum
# 6. Negative numbers throw an exception
# 7. Numbers greater than 1000 are ignored
# 8. A single char delimiter can be defined on the first line (e.g. //# for a '#' as the delimiter)
# 9. A multi char delimiter can be defined on the first line (e.g. //[###] for '###' as the delimiter)
# 10. Many single or multi-char delimiters can be defined (each wrapped in single brackets)


def test_string_calculator_should_return_zero_on_empty_string():
    result = string_calculator("")
    assert result == 0


def test_string_calculator_should_return_correct_numeric_value_on_one():
    result = string_calculator("1")
    assert result == 1


def test_string_calculator_should_return_correct_numeric_value_on_two():
    result = string_calculator("2")
    assert result == 2


def test_string_calculator_should_return_correct_numeric_value_on_three():
    result = string_calculator("3")
    assert result == 3


def test_string_calculator_should_return_five_when_delimited_by_comma_2_3():
    result = string_calculator("2,3")
    assert result == 5


def test_string_calculator_should_return_nine_when_delimited_by_comma_3_6():
    result = string_calculator("3,6")
    assert result == 9


def test_string_calculator_should_return_100_when_delimited_by_comma_34_66():
    result = string_calculator("34,66")
    assert result == 100


def test_string_calculator_should_return_100_when_delimited_by_newline_34_66():
    result = string_calculator("34\n66")
    assert result == 100


def test_string_calculator_should_return_70_when_delimited_by_newline_4_66():
    result = string_calculator("4\n66")
    assert result == 70


def test_string_calculator_should_return_10_when_delimited_by_newline_4_6():
    result = string_calculator("4\n6")
    assert result == 10


def test_string_calculator_should_return_10_when_delimited_by_comma_or_newline_2_2_6():
    result = string_calculator("2,2,6")
    assert result == 10


def test_string_calculator_should_return_100_when_delimited_by_comma_or_newline_20_20_60():
    result = string_calculator("20,20,60")
    assert result == 100


def test_string_calculator_should_return_82_when_delimited_by_comma_or_newline_2_20_60():
    result = string_calculator("2\n20\n60")
    assert result == 82


def test_string_calculator_should_throw_exception_for_minus_one():
    with pytest.raises(ValueError, match="must be a positive integer"):
        string_calculator("-1")


def test_string_calculator_should_throw_exception_for_minus_ten():
    with pytest.raises(ValueError, match="must be a positive integer"):
        string_calculator("-10")


def test_string_calculator_should_return_160_for_60_100_1200():
    result = string_calculator("60\n100\n1200")
    assert result == 160


def test_string_calculator_should_return_1200_for_200_1000_1500():
    result = string_calculator("200\n1000\n1500")
    assert result == 1200


def test_string_calculator_should_return_1200_for_200_1000_2500():
    result = string_calculator("200,1000,2500")
    assert result == 1200


def test_string_calculator_should_return_1200_for_200_1000_2500_with_hashtag():
    result = string_calculator("//#200#1000#2500")
    assert result == 1200


def test_string_calculator_should_return_200_for_200_2500_with_hashtag():
    result = string_calculator("//#200#2500")
    assert result == 200


# 9. A multi char delimiter can be defined on the first line (e.g. //[###] for '###' as the delimiter)


def test_string_calculator_should_return_200_for_150_50_with_delimiter():
    result = string_calculator("//[###]150###50")
    assert result == 200


def test_string_calculator_should_return_201_for_150_51_with_delimiter():
    result = string_calculator("//[--]150--51")
    assert result == 201
