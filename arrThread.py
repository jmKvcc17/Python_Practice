import threading
import time

def swap(arr, second_half_bool):
    
    if second_half_bool == False:
        arr[0:5] = arr[0:5][::-1]
    else:
        arr[5:10] = arr[5:10][::-1]


if __name__ == '__main__':

    arr = list(range(1, 11))
    
    try:
       t1 = threading.Thread(target=swap, args=(arr, False))
       t2 = threading.Thread(target=swap, args=(arr, True))

       t1.start()
       t2.start()
    except:
        print("An error has occured in a thread")

    
    
    for i in arr:
        print(i)

