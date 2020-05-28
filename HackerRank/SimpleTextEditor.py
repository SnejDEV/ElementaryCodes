s = ''
ref = []

for x in range(0,int(input())):
     inp = input().split(' ')

     if(inp[0]=='1'):
          ref.append(s)
          s += inp[1]
          
     elif(inp[0]=='2'):
          ref.append(s)
          s=s[0:len(s)-int(inp[1])]
               
     elif(inp[0]=='3'):
          print(s[int(inp[1])-1])

     elif(inp[0]=='4'):         
          s=ref.pop()

          
     
