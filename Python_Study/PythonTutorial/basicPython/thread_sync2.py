import time
import logging
from concurrent.futures import ThreadPoolExecutor
import threading

FORMAT = "%(asctime)s: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt="%H:%M:%S")


class FakeDataStore:
    """공유 자원"""

    def __init__(self):
        """Data, Heap 영역"""

        self.value = 0
        self._lock = threading.Lock()

    def update(self, n):
        """Stack 영역"""

        logging.info(f"Thread {n}: starting update -> value: {self.value}")

        # Lock - 동기화
        # self._lock.acquire()
        # logging.info(f"Thread {n} has lock")

        # local_copy = self.value
        # local_copy += 1
        # time.sleep(0.1)
        # self.value = local_copy

        # # Lock release
        # self._lock.release()
        # logging.info(f"Thread {n} about to release lock")

        with self._lock:
            logging.info(f"Thread {n} has lock")

            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy

            logging.info(f"Thread {n} about to release lock")

        logging.info(f"Thread {n}: finish update -> value: {self.value}")


if __name__ == "__main__":
    store = FakeDataStore()

    logging.info(f"Test update starting value is {store.value}")

    with ThreadPoolExecutor(max_workers=3) as excute:
        for n in ["First", "Second", "Third", "Four"]:
            excute.submit(store.update, n)

    logging.info(f"Test update ending value is {store.value}")
