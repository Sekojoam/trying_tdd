# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".


from fizzbuzz.fizzbuzz_code import fb_translator


def test_fb_translator_should_return_fizz_up_to_three():
    assert fb_translator(3) == "12Fizz"


def test_fb_translator_up_to_five():
    assert fb_translator(5) == "12Fizz4Buzz"


def test_fb_translator_up_to_ten():
    assert fb_translator(10) == "12Fizz4BuzzFizz78FizzBuzz"


def test_fb_translator_up_to_fifteen():
    assert fb_translator(15) == "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz"


def test_fb_translator_up_to_thirthy():
    assert fb_translator(30) == "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz1617Fizz19BuzzFizz2223FizzBuzz26Fizz2829FizzBuzz"
