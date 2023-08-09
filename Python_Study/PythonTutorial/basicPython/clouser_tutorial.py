class Averager:
    """클래스로 클로저 흉내내기"""

    def __init__(self):
        self.series = []

    def __call__(self, v: int):
        self.series.append(v)
        print(f"Inner >> {self.series} / {len(self.series)}")
        return sum(self.series) / len(self.series)


def closure_outer():
    # Closure zone
    series = []  # Free variable

    def average(v: int):
        series.append(v)
        print(f"Inner >> {series} / {len(series)}")
        return sum(series) / len(series)

    return average


# clouser anti pattern
def anti_clouser():
    cnt = 0
    total = 0

    def average(v):
        # nonlocal cnt, total
        cnt += 1  # len
        total += v  # sum
        return total / cnt

    return average


if __name__ == "__main__":
    # average = Averager()

    # print(dir(average))
    # print(average(10))
    # print(average(30))
    # print(average(50))

    average_clouser = closure_outer()
    print(average_clouser)
    print(average_clouser(10))
    print(average_clouser(30))
    print(average_clouser(50))

    # function inspection
    print(dir(average_clouser))
    print(average_clouser.__closure__[0].cell_contents)  # 클로저가 저장 하고 있는 데이터
    print(average_clouser.__code__.co_freevars)  # 클로저 영역 변수

    average_clouser2 = anti_clouser()
    print(
        average_clouser2(10)
    )  # not use nonlocal -> UnboundLocalError: local variable 'cnt' referenced before assignment
