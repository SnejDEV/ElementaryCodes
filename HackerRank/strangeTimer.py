
#NOTE:- THIS CODE IS NOT SCALABLE AND EFFICIENT
'''val,c,n=0,3,2
inp=int(input())

for x in range(1,inp+1):                #Runs till inp
    val=c
    if(c==1):
        c=3*n
        n+=2
        continue
    c-=1
print(val)'''

n,r=int(input()),3
while(n>r):
    n-=r
    r*=2
print((r+1)-n)


"""QUESTION:
    1-3
    2-2
    3-1

    4-6
    5-5
    6-4
    7-3
    8-2
    9-1

    10-12
    11-11
    12-9
    13-8
    17-7
    16-5
    17-4
    18-3
    19-2
    20-1
"""   
