from functools import reduce, partial
from operator import add, mul


def factorial(n: int):
    if 0 < n < 2:
        return 1
    return n * factorial(n - 1)


class A:
    pass


func = factorial

if __name__ == "__main__":
    print(type(factorial), factorial(5))
    print(set(sorted(dir(factorial))) - set(sorted(dir(A))))

    print(list(map(func, range(1, 11))))

    print(list(map(func, filter(lambda x: x % 2, range(1, 6)))))
    print([func(i) for i in range(1, 6) if i % 2])

    print(reduce(add, range(1, 11)))
    print(sum(range(1, 11)))
    print(reduce(lambda x, y: x + y, range(1, 11)))

    # partial: 첫번째 인수를 고정 하고 추가 적인 인수만 변경 할 때
    print(mul(10, 10))
    five = partial(mul, 5)
    six = partial(five, 6)
    print(five(6))
    print(six())
    print([five(i) for i in range(1, 11)])
    print(list(map(five, range(1, 11))))
