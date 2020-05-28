i = int(input())
stri={}

for x in range(0,i):
     var = input()
     try:
          stri[var] += 1
     except:
          stri[var] = 1
          
j = int(input())
a = []

for y in range(0,j):
     var = input()
     try:
          a.append(stri[var])
     except:
          a.append(0)

for z in a:
     print(z)
     
