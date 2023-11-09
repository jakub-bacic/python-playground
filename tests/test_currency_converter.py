from python_playground.currency_converter import convert_currency
from python_playground.money import Money


def test_convert_same_currency():
    value = Money(123, "PLN")
    assert convert_currency(value, "PLN") == value
