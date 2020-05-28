count = 0
dict ={}
fs = 0

for x in range(0,6):
          a=list(map(int,input().split(' ')))
          dict[x] = a

for x in range(0,4):
     for y in range(0,4):
          sum = dict[x][y]+dict[x][y+1]+dict[x][y+2]
          sum += dict[x+1][y+1]
          sum += dict[x+2][y]+dict[x+2][y+1]+dict[x+2][y+2]
          
          fs = sum if(count==0) else fs
          count += 1

          if(sum>fs):
               fs = sum


print(fs)
          
          
     
     
     
     
