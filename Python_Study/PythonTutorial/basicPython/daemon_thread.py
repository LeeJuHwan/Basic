import threading
import time
import logging


FORMAT = "%(asctime)s: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt="%H:%M:%S")


def thread_func(name: str, d: int):
    logging.info(f"SUB THREAD {name}: starting")
    for i in d:
        print(i)
    logging.info(f"SUB THREAD {name}: finishing")


if __name__ == "__main__":
    logging.info("MAIN THREAD: before creating thread")
    x = threading.Thread(target=thread_func, args=("First", range(20000)), daemon=True)
    y = threading.Thread(target=thread_func, args=("Two", range(10000)), daemon=True)
    logging.info("MAIN THREAD: before running thread")

    x.start()
    y.start()
    # x.join()  # daemon일 때 join을 쓰면 anti pattern에 해당함

    logging.info("MAIN THREAD: wait for the thread to finish")
    logging.info("MAIN THREAD: all done")
