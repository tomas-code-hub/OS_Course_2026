import multiprocessing
import os

def child_task(conn):
    """
    Child process function: receives data, transforms it, and sends it back.
    """
    # Receive data from parent
    data = conn.recv()
    child_pid = os.getpid()
    print(f"Child  [PID {child_pid}] received: '{data}'")
    
    # Transform the data (convert to uppercase and reverse)
    transformed = data.upper()[::-1]
    print(f"Child  [PID {child_pid}] processing and sending back: '{transformed}'")
    
    # Send transformed data back to parent
    conn.send(transformed)
    conn.close()

if __name__ == "__main__":
    parent_pid = os.getpid()
    message = "Hello from Parent"
    
    # Create a Pipe for IPC (Inter-Process Communication)
    parent_conn, child_conn = multiprocessing.Pipe()
    
    print(f"Parent [PID {parent_pid}] original message: '{message}'")
    
    # Create and start the child process
    process = multiprocessing.Process(target=child_task, args=(child_conn,))
    process.start()
    
    print(f"Parent [PID {parent_pid}] sending data to child...")
    parent_conn.send(message)
    
    # Receive results from the child
    result = parent_conn.recv()
    print(f"Parent [PID {parent_pid}] received back: '{result}'")
    
    process.join()