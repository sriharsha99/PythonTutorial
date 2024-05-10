import time
import threading

from workers.SquaredSumWorker import SquaredSumWorker
from workers.SleepyWorkers import SleepyWorker

def calculate_sum_square(n):
    sum_squares = 0
    for i in range(n):
        sum_squares += i**2
    print (sum_squares)

def sleep_a_little(seconds):
    time.sleep(seconds)

def main():
    calc_start_time = time.time()
    current_threads=[]
    for i in range(5):
        maximum_value = (i+1) * 1000000
        
        # t = threading.Thread(target=calculate_sum_square, args=(maximum_value,))
        # t.start()

        t = SquaredSumWorker(maximum_value)
        
        current_threads.append(t)
        # calculate_sum_square((i+1) * 1000000)
    for i in range(len(current_threads)):
        current_threads[i].join()
    print ('Calculating sum of squares took:', round(time.time() - calc_start_time, 1))

    sleep_start_time = time.time()
    current_threads=[]
    for seconds in range(1,6):
        
        # t = threading.Thread(target=sleep_a_little, args=(seconds, ))
        # t.start()

        t = SleepyWorker(seconds=seconds)


        # t.join() # execution is blocked until this single thread is complete. so 
                 # it will take 15 seconds
        current_threads.append(t)
        # sleep_a_little(seconds)

    for i in range(len(current_threads)):
        current_threads[i].join() # execution is blocked until all these threads are done
    print ("sleep took:", round(time.time() - sleep_start_time, 1))
    
if __name__=='__main__':
    main()


# Note:
# 1. we could able to bring down the sleep of 15 seconds to 5 seconds
# using threading.

# 2. we couldn't able to do much with computational threads