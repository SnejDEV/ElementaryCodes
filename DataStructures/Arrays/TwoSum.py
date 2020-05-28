#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
a=input().split()
a=list(map(int,a))
b=int(input())

def rec(i):
     val=a[i]
     for y in range(0,len(a)):
          x=a[y]
          if(y==i):
               continue
          elif((x+val)==b):
               return i,y
     i+=1
     rec(i)   

ans1,ans2 = rec(0)
print(str(ans1)+','+str(ans2))
