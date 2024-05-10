import threading
import time

# Define a function to be executed by the thread
def daemon_function():
    while True:
        print("Daemon thread is running...")
        time.sleep(1)

# Create a daemon thread
daemon_thread = threading.Thread(target=daemon_function)
daemon_thread.daemon = True  # Mark the thread as a daemon thread
daemon_thread.start()

# Main program continues executing...
time.sleep(5)
print("Main program is exiting...")

# Note:
# Daemon thread will run until program exits
# once the program terminates, Daemon thread will also terminate.
