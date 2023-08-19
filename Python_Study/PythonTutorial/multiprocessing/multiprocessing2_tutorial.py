from typing import List
from multiprocessing import Process, current_process, Manager
from multiprocessing.managers import SyncManager, ListProxy
import os
import random
import time


def square(n: int, result_list: List):
    random_value: int = random.randint(1, 3)
    time.sleep(random_value)
    process_id: int = os.getpid()
    process_name: str = current_process().name

    result: int = n**2

    print(f"Process ID: {process_id}, Process Name: {process_name}")
    print(f"Result of {n} square: {result}\tsleep-time: {random_value}")

    result_list.append(random_value)


if __name__ == "__main__":
    parent_process_id: int = os.getpid()

    print(f"Parent process ID: {parent_process_id}")
    processes: List = []
    manager: SyncManager = Manager()
    total_list: ListProxy = manager.list()

    start: float = time.time()
    for i in range(1, 50):
        t: Process = Process(name=str(i), target=square, args=(i, total_list))
        processes.append(t)

        t.start()

    for process in processes:
        process.join()

    sleep_time: int = sum(total_list)
    print(
        f"Main process done\t running-time: {time.time() - start}\ntotal sleep-time: {sleep_time}"
    )
