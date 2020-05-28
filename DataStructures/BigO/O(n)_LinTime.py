#from timeit import default_timer as timer

start,end=0,0
a=["nemo" for x in range(0,100000)]

def findNemo(array):
    #global start,end
    #start=timer()
    for x in array:
        if(x=="nemo"):
            print("Found NEMO!")
    #end=timer()
findNemo(a) ######  O(100000) ---LinearTime
print(end-start)
