import concurrent.futures
import logging

import queue
import random
import threading
import time


FORMAT = "%(asctime)s: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt="%H:%M:%S")


def producer(queue, event):
    """생산자: 네트워크 대기 상태인 서버"""

    while not event.is_set():
        msg = random.randint(1, 11)
        logging.info(f"Producer got message: {msg}")
        queue.put(msg)

    logging.info("Producer received event exiting")


def consumer(queue, event):
    """소비자: 데이터 읽고 쓰기 또는 DB 저장"""

    while not event.is_set() or not queue.empty():
        msg = queue.get()
        logging.info(f"Consumer storing message: {msg} (size = {queue.qsize()})")

    logging.info("Consumer sending event exiting")


if __name__ == "__main__":
    pipeline = queue.Queue(maxsize=10)

    event = threading.Event()  # 초기 값 = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as excute:
        excute.submit(producer, pipeline, event)
        excute.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")

        # flag 값을 0으로 변경 하며 프로그램을 종료함
        event.set()
