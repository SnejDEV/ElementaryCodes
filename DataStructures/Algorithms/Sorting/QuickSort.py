def swap(n,k,a):
    a[n]=a[n]+a[k]
    a[k]=a[n]-a[k]
    a[n]=a[n]-a[k]
    return(a)

def lpivot(a):
    p=len(a)-1
    x=0

    while(x<p):
        if((p-x)==1):
            if(a[x]>a[p]):
                a=swap(p,x,a)
            x+=1
            continue
        if(a[x]>a[p]):
            a=swap(p-1,x,a)
            a=swap(p,p-1,a)
            p=p-1
        elif(a[x]<a[p]):
            x+=1
    return(p)

def qs(a):            #QuickSort
    if(len(a)==1):
        return a
    m = lpivot(a)
    left = a[0:m]
    right = a[m:]
    return (qs(left)+qs(right))
