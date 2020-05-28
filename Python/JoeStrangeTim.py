import time
start = int(input())
start2= start+2
while True:
    time.sleep(1)
    print(start,"\t",start2)
    start+=1
    start2-=1
