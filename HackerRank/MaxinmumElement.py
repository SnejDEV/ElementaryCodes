class Stack():
     def __init__(self):
          self.stack = []
          self.length = 0

     def push(self,value):
          self.stack.append(value)
          self.length+=1

     def peek(self):
          self.stack[self.length-1]

     def pop(self):
          self.length-=1
          return(self.stack.pop())

s=Stack()
maxV = 0

n = int(input())
while(n!=0):
     inp = input().split(' ')
     if(inp[0]=='1'):
          s.push(int(inp[1])) 
          if(int(inp[1])>maxV):
            maxV = int(inp[1])    
     elif(inp[0]=='2'):
        temp=s.pop()  
        if(s.stack==[]):
               maxV=0
        elif(temp==maxV):
            maxV=max(s.stack)
     elif(inp[0]=='3'):
          print(maxV)
     n-=1
