''' Note : Pointers are created from one object to another by a linking word CREATED BY US, In this code the LINKING WORD is next
           REMEMBER, IT IS THE OBJECTS WHICH ARE POINTING and THESE OBJECTS ARE STORED IN VARIABLES

           Eg.: a=obj1
                b=obj1

                IN THE ABOVE CASE AS BOTH a and b REFER TO obj1, therefoe it is said a and b are POINTING TO obj1 '''


class Node:
     def __init__(self,value):
          self.value = value
          self.next = None

class LinkedList:
     def __init__(self):

          self.head = None
          self.tail = None
          self.length = 0

     def retList(self):

          rVal =[]
          nodeRef = self.head
          rVal.append(nodeRef.value)              #this calls the inbuilt append function coz it is called by a list and not an object
          while(nodeRef.next != None):
               nodeRef = nodeRef.next
               rVal.append(nodeRef.value)

          return(rVal)

     def __str__(self):

          rVal = self.retList()
          return(str(rVal))


     def append(self,value):

          node = Node(value)

          if(self.length==0):
               self.head = node
               self.tail = node
               ''' Both head and tail are POINTING(referring) to the same object viz node '''
          else:
               self.tail.next = node    #REMEMBER self.tail refers to the node object viz was created during previous append
               self.tail = node         #self.tail starts pointing to the node object created during this append FACILITAING THE PREVIOUS STEP(facilitates next append)
               ''' Also self.head still points to the FIRST object and that object points(next) points to the objects created later on '''

          self.length += 1

     def prepend(self,value):

          node = Node(value)

          if(self.length==0):
               self.append(value)
               return

          node.next = self.head    #new node object starts pointing to the head object which itself IS A node object
          self.head = node         #now head starts referring to this new object as it is prepended to the previous object

          self.length += 1

     def insert(self,index,value):

          nodeRef = self.head      #so if nodeRef changes, THE OBJECT CHANGES AS nodeRef is storing it
          
          if(index==0):
               self.prepend(value)
          else:
               node = Node(value)
               for x in range(0,index-1):
                    nodeRef = nodeRef.next
               node.next = nodeRef.next
               nodeRef.next = node
               self.length += 1

     def delete(self,index):
          
          nodeRef = self.head

          if(index==0):
               nodeRef = nodeRef.next
          else:
               for x in range(0,index-1):
                    nodeRef = nodeRef.next
               nodeRef.next = nodeRef.next.next

          self.length -= 1

     def reverse(self):

          A = self.head
          B = self.head.next
          self.tail = self.head

          while(B!=None):

               temp = B.next
               B.next = A

               A=B
               B=temp

          self.tail = self.head
          self.head = A
          self.tail.next = None             
