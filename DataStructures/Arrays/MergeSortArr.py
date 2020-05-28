#a=input().split()
#b=input().split()


def merge(a,b):
     
     if len(a)==0 or len(b)==0:
          return "Invalid Array Entered"

     a=list(map(int,a))
     b=list(map(int,b))
     i,j=1,1

     ap=a[0]
     bp=b[0]

     f=''


     while(ap or bp):
          if(bp==None or ap<bp):
               f+=str(ap)+' '
               ap=a[i] if(i<len(a)) else None
               i+=1
          else:
               f+=str(bp)+' '
               bp=b[j] if(j<len(b)) else None
               j+=1
     return f

ans=merge([],[4,6,30])
print(ans)
