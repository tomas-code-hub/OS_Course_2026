import threading
import time

# Shared global variable
counter = 0

# The Mutex (lock)
mutex = threading.Lock()

# Configuration
num_threads = 4
increments_per_thread = 100000 
expected_total = num_threads * increments_per_thread

# --- PART 1: The Problem (No Synchronization) ---
def worker_without_lock():
    global counter
    for _ in range(increments_per_thread):
        # We manually split the increment to force a Race Condition
        temp = counter
        # time.sleep(0) forces the thread to yield, allowing others to interfere
        time.sleep(0) 
        counter = temp + 1

# --- PART 2: The Solution (With Mutex/Lock) ---
def worker_with_lock():
    global counter
    for _ in range(increments_per_thread):
        # The Mutex prevents collisions, ensuring atomicity
        with mutex:
            temp = counter
            time.sleep(0) 
            counter = temp + 1

def run_experiment(target_function):
    global counter
    counter = 0 # Reset counter for each experiment
    
    threads = []
    
    for i in range(num_threads):
        t = threading.Thread(target=target_function)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
        
    return counter

if __name__ == '__main__':
    print("\n=== Assignment 4: Threads & Synchronization ===")
    
    # Part 1 execution
    print("\n[Part 1] Running 4 threads WITHOUT synchronization...")
    print("Expected result :", expected_total)
    actual_unlocked = run_experiment(worker_without_lock)
    print("Actual result   :", actual_unlocked)
    print(f"Loss            : {expected_total - actual_unlocked} increments")
    
    # Part 2 execution
    print("\n[Part 2] Running 4 threads WITH a Mutex (Lock)...")
    print("(Execution is slower because threads must wait for the lock)")
    print("Expected result :", expected_total)
    actual_locked = run_experiment(worker_with_lock)
    print("Actual result   :", actual_locked)
    
    if actual_locked == expected_total:
        print("Success! The Mutex protected the shared variable.")
    else:
        print("Failure: The counter is still inconsistent.")
