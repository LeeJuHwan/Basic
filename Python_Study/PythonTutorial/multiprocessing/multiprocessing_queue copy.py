from multiprocessing import Queue, Process, current_process
import time, os


def worker(p_id, base_num, q):
    process_id = os.getpid()
    process_name = current_process().name

    sub_total = 0

    for i in range(base_num):
        sub_total += 1
    
    q.put(sub_total)

    print(f"Process ID: {process_id}, Process name: {process_name}\tID: {p_id}")
    print(f"Result: {sub_total}")

def main():
    parent_process_id = os.getpid()
    print(f"Parent process ID: {parent_process_id}")

    process_list = []

    start = time.time()
    
    # Queue 
    q = Queue()
    
    for i in range(5):
        t = Process(name=str(i), target=worker, args=(i, 10000000, q))
        process_list.append(t)

        t.start()
    
    for process in process_list:
        process.join()
    
    print(f"{'-'*3} {time.time() - start } seconds {'-'* 3}")

    q.put("exit")
    total = 0

    while True:
        tmp = q.get()
        if tmp == "exit":
            break
        else:
            total += tmp
    
    print()
    print(f"Main process total total count = {total}")
    print("Main process done.")
          
    


if __name__ == "__main__":
    main()
