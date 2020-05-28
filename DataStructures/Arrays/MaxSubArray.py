#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
a=input().split()
a=list(map(int,a))

a.sort(reverse=True)
s=0

for x in a:
     if((s+x)>s):
          s+=x
     elif((s+x)<s):
          break
print(s)
