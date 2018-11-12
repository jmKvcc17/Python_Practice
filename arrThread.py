import threading
from threading import Lock


# Globals
# create the lock object
lock = Lock()


def swap(arr, second_half_bool):
    
    if not second_half_bool:
        lock.acquire()
        arr[0:5] = arr[0:5][::-1]
        lock.release()
    else:
        lock.acquire()
        arr[5:10] = arr[5:10][::-1]
        lock.release()


if __name__ == '__main__':

    arr = list(range(1, 11))

    actArr = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    try:
       t1 = threading.Thread(target=swap, args=(arr, False))
       t2 = threading.Thread(target=swap, args=(arr, True))

       t1.start()
       t2.start()
    except:
        print("An error has occurred in a thread")

    for i in arr:
        print(i)

