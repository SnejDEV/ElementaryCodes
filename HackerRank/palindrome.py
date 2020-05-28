s=input()
n=int(input())
pos=[]
xy=''
ans=0

for x in range(0,n):
     pos.append(input())

def check(texP):
     global xy,s
     count=0

     rtex=''

     xy=texP.split()
     xy=list(map(int,xy))

     tex=s[xy[0]-1:xy[1]]

     text = [x for x in tex]
     num=len(text)
     pc=0
     re=0

     for y in range(0,num-1):
          ch=text[y]
          for z in range(y+1,num):
               if(ch==tex[z]):#and ch not in rtex):
                    if(ch in rtex):
                         re+=1
                    else:
                         rtex+=ch
                         pc+=1
               pc-=re
               re=0
     for z in text:
          if(z not in rtex):
               count+=1
     count=count if(count != 0) else pc
     return count
               
     

for x in pos:
     ans=check(x)
     print(ans)
     
       
