import pytest
from fizz_buzz_func import fizzbuzz

@pytest.mark.parametrize('numero,expected',[(3,'Fizz'), (5,'Buzz'), (15, 'FizzBuzz'), (4, 4)])
def test_fizzbuzz(numero, expected):
    assert  fizzbuzz(numero) == expected