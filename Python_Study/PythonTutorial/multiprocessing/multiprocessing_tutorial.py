from typing import Final
from multiprocessing import Process
import time
import logging


FORMAT: Final[str] = "%(asctime)s: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt="%H:%M:%S")


def proc(name: str):
    print(f"Sub Process start >> {name}")
    time.sleep(3)
    print(f"Sub Process finish >> {name}")


def main():
    p: Process = Process(target=proc, args=("First",))
    logging.info("Main Process: before create process")

    p.start()

    logging.info("Main Process running")
    logging.info("Main Process terminated")
    p.terminate()
    logging.info("Main Process wait for finish sub-process")
    p.join()
    print(f"Process p is alive: {p.is_alive()}")


if __name__ == "__main__":
    main()
