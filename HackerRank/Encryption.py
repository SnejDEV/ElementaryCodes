import math
inp,row,col,a,b='',0,0,0,0
tex=''
count=0
fs,final=[],''

def accept():
     global inp
     s=(input().strip()).lower()
     for x in s:
          if(x==' '):
               continue
          inp+=x

accept()
l = len(inp)
r=math.sqrt(l)

row=int(math.floor(r))
col=int(math.ceil(r))
if((row*col)<l):
     row=col
b=col
fs=['' for x in range(0,col)]

for x in range(0,row):
          tex+=inp[a:b]+' '
          a+=col
          b+=col

ar=tex.split()
for x in ar:
     p=0
     for y in x:
          fs[p]+=y
          p+=1

for x in fs:
     final+=x+' '
print(final.strip())
     
     
          
     

