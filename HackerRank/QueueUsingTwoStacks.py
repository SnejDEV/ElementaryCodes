class Node:
     def __init__(self,value):
          self.value = value
          self.next =  None
          self.prev = None

class ST:                     #Stack
     def __init__(self):
          self.head = None
          self.tail = None
          self.length = 0

     def append(self,value):
          node = Node(value)
          if(self.length==0):
               self.head = node
               self.tail = node
          else:
               self.head.prev = node
               node.next = self.head
               self.head = node
          self.length+=1

     def delete(self):
          self.head = self.head.next
          self.length -= 1
          if(self.length==0):
               self.tail = None

     def rpop(self):
          if(self.tail.prev != None):
               self.tail.prev.next = None
          self.tail = self.tail.prev
          self.length -= 1
          if(self.length==0):
               self.head = None
          return(self.tail.value if self.tail != None else self.tail)

     def peek(self):
          try:
               return(self.head.value)
          except:
               return(None)

class queue:
     def __init__(self):
          self.a = ST()
          self.b = ST()

     def push(self,value):
          self.a.append(value)
          if(self.b.length==0):
               self.b.append(value)

     def pop(self):
          temp = self.b.head.value
          self.b.delete()
          v = self.a.rpop()
          if v!= None:
               self.b.append(v) 
          return temp

     def peek(self):
          try:
               return(self.b.head.value)
          except:
               return(None)

q = queue()
for x in range(0,int(input())):
     inp = input().split(' ')
     if(inp[0]=='1'):
          q.push(int(inp[1]))
     elif(inp[0]=='2'):
          q.pop()
     elif(inp[0]=='3'):
          print(q.peek())
