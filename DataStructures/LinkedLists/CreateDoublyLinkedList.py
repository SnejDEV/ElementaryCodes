class Node():
     def __init__(self,val):
          self.value = val
          self.prev = None
          self.next = None

class DLinkedList:

     def __init__(self,value):
          node = Node(value)
          self.head = node
          self.tail = self.head                   #pointer to head

     def append(self,value):
          node = Node(value)
          node.prev = self.tail
          self.tail.next = node
          self.tail = node                        #pointer to node

     def prepend(self,value):
          node = Node(value)
          node.next = self.head
          self.head.prev = node
          self.head = node

     def retList(self):
          nodeRef = self.head
          rVal = []
          rVal.append(nodeRef.value)
          while(nodeRef.next != None):
               nodeRef = nodeRef.next
               rVal.append(nodeRef.value)
          return(rVal)

     def __str__(self):
          rVal = self.retList()
          return(str(rVal))

     def insert(self,index,value):
          if(index==0):
               self.prepend(value)
               rVal=self.retList()
               return(rVal)

          node = Node(value)
          nodeRef = self.head
          for x in range(0,index-1):
               nodeRef = nodeRef.next
          node.next = nodeRef.next

          nodeRef.next.prev = node
          node.prev = nodeRef

          nodeRef.next = node

          rVal=self.retList()
          return(rVal)

     def delete(self,index):
          if(index==0):
               self.head.prev = None
               self.head = self.head.next
               rVal=self.retList()
               return(rVal)

          nodeRef = self.head
          for x in range(0,index-1):
               nodeRef = nodeRef.next

          nodeRef.next.prev = nodeRef
          nodeRef.next = nodeRef.next.next
          
          if(len(self.retList()) == index):
               self.tail = nodeRef  
          
          rVal=self.retList()
          return(rVal)

     def reverse(self):
          if(len(self.retList()) == 1):
               return(self.retList())

          A = self.head
          B = self.head.next
          HeadRef = self.head                #so head becomes tail nd tail becomes head....storing head in a temp variable
          A.prev = B

          while(B!=None):
               temp = B.next
               B.next = A
               A.prev = B

               A = B
               B = temp
               self.tail = A

          self.head.next = None
          self.head = self.tail
          self.head.prev = None
          self.tail = HeadRef                #Else problems occurs in append when u create pointers with self.tail
          rVal=self.retList()
          return(rVal)
