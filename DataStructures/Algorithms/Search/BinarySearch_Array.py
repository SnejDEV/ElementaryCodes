import math

def search(a,n):
    m = math.floor(len(a)/2)
    if(a[m-1]==n):
        print("Found :)")
    elif(len(a)==1):
        print("Not Found :(")
    elif(n>a[m-1]):
        search(a[m:],n)
    elif(n<a[m-1]):
        search(a[0:m],n)
