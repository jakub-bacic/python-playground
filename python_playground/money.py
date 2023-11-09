class Money:
    def __init__(self, value, currency):
        self.value = value
        self.currency = currency

    def __str__(self):
        return f"{self.value} {self.currency}"
