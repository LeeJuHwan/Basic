from multiprocessing import Process
import os


def task1():
    print(f"task1 >> 자식 프로세스: {os.getpid()}")
    print(f"task1 >> 부모 프로세스: {os.getppid()}")


def task2():
    print(f"task2 >> 자식 프로세스: {os.getpid()}")
    print(f"task2 >> 부모 프로세스: {os.getppid()}")


def task3():
    print(f"task3 >> 자식 프로세스: {os.getpid()}")
    print(f"task3 >> 부모 프로세스: {os.getppid()}")


if __name__ == "__main__":
    print(f"부모 프로세스: {os.getpid()}")
    child1 = Process(target=task1).start()
    child2 = Process(target=task2).start()
    child3 = Process(target=task3).start()
