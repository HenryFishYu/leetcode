import threading
import time

def reverse_arr(arr:[],k:int):
    length = len(arr)
    for i in range(0,length,k):
        if i+k>length:
            continue
        else:
            arr[i:i+k] = reversed(arr[i:i+k])

if __name__ == "__main__":
    arr = [4,3,7,10,2,1]
    res = []
    threads = []

    def sorting_thread(num):
        time.sleep(num)
        res.append(num)

    for num in arr:
        threads.append(threading.Thread(target=sorting_thread,args=(num,)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(res)



