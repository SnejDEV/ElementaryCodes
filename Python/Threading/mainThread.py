import threading
print(threading.currentThread().getName())

if(threading.current_thread()==threading.main_thread()):
    print("Executing MainThread")
else:
    print(threading.current_thread())
a = threading
print(a.currentThread())

#Note: threading.currentThread() is same as threading.current_thread()
