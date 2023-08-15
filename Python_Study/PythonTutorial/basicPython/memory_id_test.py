import sys


class Test:
    def __init__(self):
        self.value = 0

    def update(self):
        print(
            f"{type(self).__name__}: initialized {sys.getrefcount(self.value)}, {id(self.value)}"
        )
        self.value += 1
        print(
            f"{type(self).__name__}: updated {sys.getrefcount(self.value)}, {id(self.value)}"
        )


if __name__ == "__main__":
    s = Test()
    print(f"s ID: {id(s)}\ts VALUE: {id(s.value)}")
    s.update()
    print(f"s update VALUE: {id(s.value)}")
    p = Test()
    print(f"p ID: {id(p)}\ts VALUE: {id(p.value)}")
    p.update()
    print(f"p update VALUE: {id(p.value)}")
