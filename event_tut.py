
import random, time
from threading import Event, Thread

event = Event() # create the event object

def waiter(event, nloops):

    for i in range(nloops):
        print("%s. Waiting for the flag to be set." % (i+1))
        event.wait() # Blocks until the flag becomes true (set()).
        print("Wait complete at:", time.ctime())
        event.clear() # Resets the flag.
        print()

def setter(event, nloops):

    for i in range(nloops):
        print("Setter sleeping...")
        time.sleep(random.randrange(2, 5)) # Sleeps for some time.
        event.set() # sets the event off, alerts waiter

threads = []
nloops = random.randrange(3, 6)

threads.append(Thread(target=waiter, args=(event, nloops)))
threads[-1].start()
threads.append(Thread(target=setter, args=(event, nloops)))
threads[-1].start()

for thread in threads:
    thread.join()

print("All done.")