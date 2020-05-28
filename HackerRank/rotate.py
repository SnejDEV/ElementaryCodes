s=''

class Node:
     def __init__(self,value):
          self.value = value
          self.next = None

class LL():
     def __init__(self):
          self.head = None
          self.tail = None

     def append(self,value):
          node = Node(value)
          if(self.head == None and self.tail == None):
               self.head = node
               self.tail = node
          else:
               self.tail.next = node
               self.tail = node

inp=list(map(int,input().split()))
l = LL()
array = list(map(int,input().split()))
for x in array:
     l.append(x)
for y in range(0,inp[1]):
     temp = l.head
     l.tail.next = temp
     l.tail = temp
     l.head = l.head.next
     temp.next = None
nodeRef = l.head
while(nodeRef!=None):
     s+=str(nodeRef.value)+' '
     nodeRef = nodeRef.next
print(s)
