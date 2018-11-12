
from threading import Lock, Thread

# Globals
# create the lock object
lock = Lock()
g = 0

def add_one():
   """
   Just used for demonstration. It’s bad to use the ‘global’
   statement in general.
   """
   
   global g
   # lock g so other threads can't use it
   lock.acquire()
   for i in range(1, 100):
       print("Minus {}".format(i))
       g -= i
   # unlock g so other threads can access g
   lock.release()

def add_two():
   global g
   lock.acquire()
   for i in range(1, 100):
        print("Plus {}".format(i))
        g += (i + 2)
   lock.release()

threads = []
for func in [add_one, add_two]:
   threads.append(Thread(target=func))
   threads[-1].start()

for thread in threads:
   """
   Waits for threads to complete before moving on with the main
   script.
   """
   thread.join()

print(g)