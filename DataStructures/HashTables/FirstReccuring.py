def find(a):                                      #TimeC = O(n)#SpaceC = O(n)
     d={}
     for x in a:
          if(x not in list(dict.keys(d))):
               d[x]=0
          d[x]=d[x]+1
          if(d[x]==2):
               return(x)
     return "undefined"


a=input().split()
a=list(map(int,a))
print(find(a))
