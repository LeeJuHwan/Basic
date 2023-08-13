import threading
import time
import logging


FORMAT = "%(asctime)s: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt="%H:%M:%S")


def thread_func(name: str):
    logging.info(f"SUB THREAD {name}: starting")
    time.sleep(3)
    logging.info(f"SUB THREAD {name}: finishing")


if __name__ == "__main__":
    logging.info("MAIN THREAD: before creating thread")

    x = threading.Thread(target=thread_func, args=("First",))
    logging.info("MAIN THREAD: before running thread")

    x.start()
    x.join()

    logging.info("MAIN THREAD: wait for the thread to finish")
    logging.info("MAIN THREAD: all done")
