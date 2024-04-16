# Importing necessary libraries
import time
import multiprocessing

# Recording the start time
start = time.perf_counter()

# Defining a variable
a = 1

# Defining a static method that increments the value of a by 1
@staticmethod
def inc():
    return a + 1

# Defining a function that simulates a time-consuming task
def do_something(i=None):
    print('Sleeping 1 second...', i if i else "")  # Informing the user that the task has started
    time.sleep(1)  # Simulating a time-consuming task by sleeping for 1 second
    print('Done sleeping...', i if i else "")  # Informing the user that the task has finished

# Creating two separate processes that will execute the time-consuming task concurrently
p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

# Starting the processes
p1.start()
p2.start()

# Waiting for the processes to finish
p1.join()
p2.join()

print("I'm going on!")  # Informing the user that the program will continue

# Recording the finish time
finish = time.perf_counter()

# Printing the total time taken to execute the two processes
print(f'Finished in {round(finish-start, 2)} second(s)')

# Now, let's do the same but with 10 processes

# Creating a list to hold the processes
processes = []

# Recording the start time
start = time.perf_counter()

# Creating and starting 10 processes that will execute the time-consuming task concurrently
for _ in range(10):
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)
    
# Waiting for all the processes to finish
for process in processes:
    process.join()
    
# Recording the finish time
finish = time.perf_counter()



# Printing the total time taken to execute the 100 processes
print(f'Finished in {round(finish-start, 2)} second(s)')
# Recording the start time
start = time.perf_counter()

# Creating and starting 10 processes that will execute the time-consuming task concurrently
for _ in range(100):
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)
    
# Waiting for all the processes to finish
for process in processes:
    process.join()
    
# Recording the finish time
finish = time.perf_counter()

# Printing the total time taken to execute the 100 processes
print(f'Finished in {round(finish-start, 2)} second(s)')


# Printing the total time taken to execute the 1000 processes
print(f'Finished in {round(finish-start, 2)} second(s)')
# Recording the start time
start = time.perf_counter()

# Creating and starting 10 processes that will execute the time-consuming task concurrently
for i in range(1000):
    p = multiprocessing.Process(target=do_something, args=[i])
    p.start()
    processes.append(p)
    
# Waiting for all the processes to finish
for process in processes:
    process.join()
    
# Recording the finish time
finish = time.perf_counter()

# Printing the total time taken to execute the 1000 processes
print(f'Finished in {round(finish-start, 2)} second(s)')