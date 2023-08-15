import timeit


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class B:
    __slots__ = ["a", "b"]

    def __init__(self, a: str, b: int):
        self.a = a
        self.b = b


def time_checker(obj):
    def wrapper():
        obj.a = "hello"
        obj.b = 42
        del obj.a
        del obj.b

    return wrapper


if __name__ == "__main__":
    aa = A("hello", 1)
    print(aa.__dict__)

    bb = B("hello", 1)
    print(bb.__slots__)

    a_time = timeit.repeat(time_checker(aa), number=1000000)
    b_time = timeit.repeat(time_checker(bb), number=1000000)

    print(
        min(a_time)
    )  # min을 쓰지 않는 경우 [0.291029458, 0.29313416700000006, 0.293504667, 0.29303716700000004, 0.29543491600000005]
    print(min(b_time))  # 0.23433766600000006
