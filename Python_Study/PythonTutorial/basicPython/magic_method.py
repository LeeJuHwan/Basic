class Friuts:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return f"Fruit class info : {self._name}, {self._price}"

    def __add__(self, x):
        return self._price + x._price

    def __sub__(self, x):
        return self._price - x._price

    def __lt__(self, x):
        if self._price < x._price:
            return True
        return False

    def __gt__(self, x):
        if self._price > x._price:
            return True
        return False

    def __le__(self, x):
        if self._price <= x._price:
            return True
        return False

    def __ge__(self, x):
        if self._price >= x._price:
            return True
        return False


if __name__ == "__main__":
    c = Friuts("Orange", 7500)
    c2 = Friuts("Banana", 3000)

    # magic method excute
    print(c + c2)
    print(c - c2)
    print(c < c2)
    print(c > c2)
