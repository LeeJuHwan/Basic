from typing import Dict, List
from multiprocessing import Manager
from multiprocessing.managers import DictProxy, SyncManager
from multiprocessing import Process


def worker(procnum: int, return_dict: Dict):
    """worker function"""
    print(str(procnum) + " represent!")
    return_dict[procnum] = procnum


if __name__ == "__main__":
    manager: SyncManager = Manager()
    return_dict: DictProxy = manager.dict()
    jobs: List = []
    for i in range(5):
        p: Process = Process(target=worker, args=(i, return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    print(return_dict.values())
