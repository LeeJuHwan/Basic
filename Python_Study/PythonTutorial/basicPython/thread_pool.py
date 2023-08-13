import time
import logging
from concurrent.futures import ThreadPoolExecutor


FORMAT = "%(asctime)s: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt="%H:%M:%S")


def task(name):
    logging.info(f"Sub-Thread {name}: starting")

    result = 0
    for i in range(100001):
        result += i

    logging.info(f"Sub-Thread {name}: \tresult: {result}")
    return result


def main():
    logging.info("MAIN THREAD: before creating and running thread")

    # max_workers : 작업의 개 수가 넘어가면 직접 설정이 유리함
    # excute = ThreadPoolExecutor(max_workers=3)
    # task1 = excute.submit(task, ("First",))
    # task2 = excute.submit(task, ("Second",))

    # print(f"task1 result: {task1.result()}")
    # print(f"task2 result: {task2.result()}")

    with ThreadPoolExecutor(max_workers=3) as excute:  # queue를 사용하여 작업 스케줄링을 지원 해 줌
        tasks = excute.map(task, ["First", "Second", "Thrid", "Fourth", "Fifth"])

        print(list(tasks))


if __name__ == "__main__":
    main()
