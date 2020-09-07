import threading,time
from threading import Thread

def displayNumbers():
    i = 0
    for x in range(0,10):
        print(threading.current_thread())
        print(i)
        i+=1
        time.sleep(2)
        

if __name__ == "__main__":
    t = Thread(target=displayNumbers)
    t.start()
    for y in range(0,10):
        print(threading.current_thread())
        time.sleep(1)
    
