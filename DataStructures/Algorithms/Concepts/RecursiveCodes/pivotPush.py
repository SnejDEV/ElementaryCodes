#This the concept used in Quick Sort
def swap(n,k,a):
    a[n]=a[n]+a[k]
    a[k]=a[n]-a[k]
    a[n]=a[n]-a[k]
    return(a)

def lpivot(a):
    p=len(a)-1
    x=0
    while(x!=p):
        print(a)
        if(a[p]<a[x]):
            if((p-x)==1):
                a=swap(x,p,a)
                p=p-1
                continue
            a=swap(x,p-1,a)
            a=swap(p,p-1,a)
            p=p-1
            continue
        x+=1
    return(a)
