import threading
import os


def task():
    print(f"task >> thread id: {threading.get_native_id()}")
    print(f"task >> process id: : {os.getpid()}")


if __name__ == "__main__":
    print(f"hello os: {os.getpid()}")

    thread1 = threading.Thread(target=task).start()
    thread2 = threading.Thread(target=task).start()
    thread3 = threading.Thread(target=task).start()
