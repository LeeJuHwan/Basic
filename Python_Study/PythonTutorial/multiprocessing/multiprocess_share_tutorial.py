from typing import List
from multiprocessing import Process, current_process, Array, Value
from multiprocessing.sharedctypes import Synchronized, SynchronizedBase
import os


def generate_update_number(v: Synchronized):
    for _ in range(50):
        v.value += 1
    print(f"Process: {current_process().name}\tdata: {v.value}")


def main():
    parent_process_id: int = os.getpid()
    print(f"Parent process ID: {parent_process_id}")

    processes: List = []

    # Process share to data, also can use another library
    # from multiprocess import shared_memory
    # from multiprocess import Manager
    # share_numbers = Array("i", range(50))
    share_value: SynchronizedBase = Value("i", 0)  # integer -> i

    for _ in range(1, 10):
        p: Process = Process(target=generate_update_number, args=(share_value,))
        processes.append(p)

        p.start()

    for process in processes:
        process.join()

    print(f"Final data in parent process : {share_value}")


if __name__ == "__main__":
    main()
