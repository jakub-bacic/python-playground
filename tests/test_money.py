from python_playground.money import Money


def test_money_str():
    assert str(Money(20, "PLN")) == '20 PLN'
