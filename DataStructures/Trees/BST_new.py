class Node:

     def __init__(self,value):
          self.value = value
          self.right = None
          self.left = None

class BST():
     def __init__(self):
          self.root = None

     def insert(self,value):
          node = Node(value)
          nodeRef = self.root

          while(True):
               if(self.root==None):
                    self.root =  node
                    break
               else:
                    if(value>nodeRef.value and nodeRef.right==None):
                         nodeRef.right=node
                         break
                    elif(value<nodeRef.value and nodeRef.left==None):
                         nodeRef.left=node
                         break
                    nodeRef = nodeRef.right if(value>nodeRef.value) else nodeRef.left

     def search(self,value):
          nodeRef = self.root
          while(nodeRef!=None):
               if(nodeRef.value==value):
                    return(True)
               else:
                    if(value > nodeRef.value):
                         nodeRef = nodeRef.right
                    elif(value < nodeRef.value):
                         nodeRef = nodeRef.left
          return(False)

     def func(self,point,nodeRef,dirP):
          if(nodeRef.value>point.value):
               point.right = dirP
          elif(nodeRef.value<point.value):
               point.left = dirP

     def delete(self,value):

          nodeRef = self.root
          point = None

          while(nodeRef != None):

                 if(nodeRef.value == value):
  
                      if(nodeRef.right==None):                        #works for leaf nodes as well as nodes with oly a left node
                           self.func(point,nodeRef,nodeRef.left)
                           return
  
                      elif(nodeRef.right != None and nodeRef.right.left == None):    #child has a right node nd the right node doesnt have a left node
                           nodeRef.right.left = nodeRef.left
                           self.func(point,nodeRef,nodeRef.right)
                           return

                      elif(nodeRef.right != None and nodeRef.right.left != None):    #child has a right node and the right node has a/further left nodes
                           l = nodeRef.right.left
                           lb = nodeRef.right

                           while(l.left != None):
                                lb = l
                                l=l.left

                           lb.left = l.right                     #if the last left node has a right node

                           l.right = nodeRef.right
                           l.left = nodeRef.left

                           self.func(point,nodeRef,l)
                           return
                           

                 else:
                      if(value>nodeRef.value):
                           point = nodeRef
                           nodeRef = nodeRef.right
                      elif(value<nodeRef.value):
                           point = nodeRef
                           nodeRef = nodeRef.left
                    
          return(False)


a=BST()
a.insert(9)
a.insert(4)
a.insert(1)
a.insert(6)
a.insert(20)
a.insert(15)
a.insert(170) 
