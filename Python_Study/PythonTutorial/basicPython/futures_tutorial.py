import os
import time
from concurrent.futures import (
    ThreadPoolExecutor,
    ProcessPoolExecutor,
    wait,
    as_completed,
)


WORK_LIST = [10000, 1000000, 1000000, 10000000]


def sum_generator(n):
    return sum(n for n in range(1, n + 1))


def main():
    worker = len(WORK_LIST)

    start = time.time()
    futures_list = []

    with ThreadPoolExecutor() as excute:  # -> Thread: 0.84s
        # with futures.ProcessPoolExecutor() as excute:  # -> Process: 1.03s
        # map: 작업 순서 유지, 즉시 실행
        # result = excute.map(sum_generator, WORK_LIST)
        for work in WORK_LIST:
            # future반환
            future = excute.submit(sum_generator, work)

            # 스케줄링
            futures_list.append(future)
            print(
                f"SCHEDULEL: {work}: {future}"
            )  # SCHEDULEL: 10000000: <Future at 0x7fc1d00d4850 state=pending>
        # # wait: 일정 시간 동안 작업이 이루어진 후 처리 해야 하는 비동기 처리
        # result = wait(futures_list, timeout=7)
        # print(
        #     f"completed Tasks: {str(result.done)}"
        # )  # completed Tasks: {<Future at 0x7fc1d810a8e0 state=finished returned int>
        # print(f"failed tasks: {str(result.not_done)}")
        # result_print = [future.result() for future in result.done]

        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled()

            end = time.time()
            result_print = f"Future Result: {result}, Done: {done}, run-time: {end-start:.2f}s\nFuture Canclled: {cancelled}"
            print(result_print)
    # end = time.time()
    # msg = f"\n Result -> {result_print} Time: {end - start:.2f}s"
    # print(msg)


if __name__ == "__main__":
    main()
