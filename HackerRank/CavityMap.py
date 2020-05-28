a,s=[],''
n=int(input())

def accept():
    global n,a
    for x in range(0,n):
        a.append("")
        while(len(a[x])!=n):
            a[x]=list((input().strip()))
        for y in range(0,n):
          a[x][y]=int(a[x][y])
    #print(a)

accept()

for x in range(1,n-1):
    for y in range(1,n-1):
          v=a[x][y]
          lv=a[x][y-1]
          rv=a[x][y+1]
          tv=a[x-1][y]
          bv=a[x+1][y]
          l=[lv,rv,tv,bv]

          count=0
          
          for z in l:
               if(z!='X' and v>z):
                    count+=1
          if(count==4):
              a[x][y]="X"

for x in range(0,n):
     for y in range(0,n): 
          v=a[x][y]
          s=s+str(v)
     print(s)
     s=""


                    
