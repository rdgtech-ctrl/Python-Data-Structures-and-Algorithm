# Multithreading (Shared Memory)
from threading import Thread

count = 0

def increment():
    global count
    count += 1

t1 = Thread(target=increment)
t2 = Thread(target=increment)
# Both threads t1 and t2 modify the same variable
t1.start()
t2.start()

t1.join()
t2.join()

print(count)

# Multiprocessing (Separate Memory)
from multiprocessing import Process

count =  0 

def increment():
    global count
    count += 1
    print(count)

p1 = Process(target=increment)
p2 = Process(target=increment)

p1.start()
p2.start()

p1.join()
p2.join()

print(count)
"""
Each process gets its own copy of count.

Changes inside a process do not affect the main process.

This example clearly shows the core difference:

Multithreading  -> Shared Memory
Multiprocessing -> Separate Memory
"""