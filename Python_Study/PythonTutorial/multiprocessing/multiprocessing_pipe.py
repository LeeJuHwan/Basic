from multiprocessing import Pipe, Process, current_process
import time, os


def worker(p_id, base_num, conn):
    process_id = os.getpid()
    process_name = current_process().name

    sub_total = 0

    for i in range(base_num):
        sub_total += 1
    
    conn.send(sub_total)
    conn.close()  # Pipe memory free

    print(f"Process ID: {process_id}, Process name: {process_name}\tID: {p_id}")
    print(f"Result: {sub_total}")

def main():
    parent_process_id = os.getpid()
    print(f"Parent process ID: {parent_process_id}")

    start = time.time()
    
    # Pipe
    parent_conn, child_conn = Pipe()  # 부모 커넥션, 자식 커넥션 생성
    
    t = Process(name=str(1), target=worker, args=(1, 50000000, child_conn))

    t.start()
    t.join()
    
    print(f"{'-'*3} {time.time() - start } seconds {'-'* 3}")

    
    print()
    print(f"Main process total total count = {parent_conn.recv()}")
    print("Main process done.")
          
    


if __name__ == "__main__":
    main()
