class Node:

     def __init__(self,value):
          self.value = value
          self.next  = None

class Stack:

     def __init__(self):
          self.head = None
          self.tail = None
          self.length = 0

     def push(self,value):                    #append
          node = Node(value)

          if(self.length==0):
               self.head = node
               self.tail = node
          else:
               node.next = self.head
               self.head = node

          self.length += 1

     def pop(self):
          temp = self.head.value
          self.head = self.head.next
          self.length -= 1
          if(self.length==0):
               self.tail = None            #On popping vals @length = 0, the object despite being deleted at head node,
                                           #the tail node still has the the object, therefore we delete that node
          return(temp)

     def peek(self):
          return(self.head.value)

class Queue:

     def __init__(self):
          self.stack1 = Stack()
          self.stack2 = Stack()

     def enqueue(self,value):
          self.stack1.push(value)
          if(self.stack2.length==0):
               self.stack2.push(self.stack1.tail.value)

     def dequeue(self):
          nodeRef = self.stack1.head
          temp = self.stack2.pop()

          self.stack1.length -= 1
          
          if(self.stack1.head==self.stack1.tail):
               self.stack1.head = None
               self.stack1.tail = None
               return(temp)
          
          for x in range(0,self.stack1.length-2):
               nodeRef = nodeRef.next
          nodeRef.next = None
          self.stack1.tail = nodeRef

          self.stack2.push(self.stack1.tail.value)
          return(temp)

     def peek(self):
          return(self.stack2.head.value)
          
                    












     
