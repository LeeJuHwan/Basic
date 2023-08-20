from typing import List
from multiprocessing import Process, current_process
import os


def generate_update_number(value: int):
    for _ in range(50):
        value += 1
    print(f"Process: {current_process().name}\tdata: {value}")


def main():
    parent_process_id: int = os.getpid()
    print(f"Parent process ID: {parent_process_id}")

    processes: List = []
    share_value: int = 0

    for _ in range(1, 10):
        p: Process = Process(target=generate_update_number, args=(share_value,))
        processes.append(p)

        p.start()

    for process in processes:
        process.join()

    print(f"Final data in parent process : {share_value}")


if __name__ == "__main__":
    main()
