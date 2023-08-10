from inspect import getgeneratorstate


def coroutine_func():
    print("coroutine start")
    i = yield
    print(f"receive: {i}")


def coroutine2_func(x):
    print(f"coroutine2 start x: {x}")
    y = yield x
    print(f"receive y: {y}")
    z = yield x + y
    print(f"add operation: {z}")


def coroutine_yield():
    for i in "AB":
        yield i

    for j in range(1, 4):
        yield j


def coroutine_yield_from():
    yield from "AB"
    yield from range(1, 4)


co = coroutine_func()

# anti coroutine
# co2 = coroutine_func()

co3 = coroutine2_func(10)
co_yield = coroutine_yield()
co_yield_form = coroutine_yield_from()

if __name__ == "__main__":
    # ------------- coroutine practice ---------------
    # print(co, type(co))
    # next(co)
    # co.send(100)  # 서브루틴
    # next(co)

    # co2.send(100)  # next로 yield 지점 까지 이동 하고 데이터 전송 해야 함

    # ------------- coroutine state -------------------
    # print(getgeneratorstate(co3))  # GEN GEN_CREATED: 대기 상태
    # print(next(co3))  # next를 통해 코루틴 상태 이동 (yield - x)
    # print(getgeneratorstate(co3))  # GEN_SUSPENDED: Yield 대기 상태
    # co3.send(100)  # 코루틴 상태 이동 (yield - y)
    # print(getgeneratorstate(co3))  # GEN_SUSPENDED: Yield 대기 상태
    # try:
    #     co3.send(100)  # 코루틴 상태 이동 (yield - z)
    #     print(getgeneratorstate(co3))  # GEN_CLOSED: 실행 완료 상태 (stop iteration 발생으로 실행 X)
    # except StopIteration:
    #     print(getgeneratorstate(co3))  # GEN_CLOSED 여기서 발동

    print(list(co_yield))
    print(list(co_yield_form))
