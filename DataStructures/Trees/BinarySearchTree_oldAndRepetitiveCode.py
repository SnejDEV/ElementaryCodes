class Node:
     def __init__(self,value):
          self.value = value
          self.left = None
          self.right = None

class BST:
     def __init__(self):
          self.root = None

     def insert(self,value):
          
          node = Node(value)

          if(self.root==None):
               self.root = node
          else:
               nodeRef = self.root
               while(True):
                    if(value>nodeRef.value and nodeRef.right == None):
                         nodeRef.right = node
                         break
                    elif(value<nodeRef.value and nodeRef.left == None):
                         nodeRef.left = node
                         break                   
                    nodeRef = nodeRef.right if(value>nodeRef.value) else nodeRef.left     

     def search(self,value):

          nodeRef = self.root

          while(True):
               if(nodeRef==None): 
                    return(False)
               elif(nodeRef.value==value):
                    return(True)
               else:
                    if(value>nodeRef.value):
                         nodeRef = nodeRef.right
                    elif(value<nodeRef.value):
                         nodeRef = nodeRef.left

     def delete(self,value):

          nodeRef = self.root
          point = None

          while(True):

               if(nodeRef==None):
                    return(False)
               elif(value>nodeRef.value):
                    point = nodeRef
                    nodeRef=nodeRef.right
               elif(value<nodeRef.value):
                    point=nodeRef
                    nodeRef=nodeRef.left

               if(nodeRef.value == value and nodeRef.right==None and nodeRef.left==None):       #leaf nodes
                    if(point.value<nodeRef.value):
                         point.right =  None
                    if(point.value>nodeRef.value):
                         point.left = None
                    break

               elif(nodeRef.value == value and nodeRef.right==None and nodeRef.left!=None):    #node to be deleted only has a left node
                    nodeRef.value = nodeRef.left.value
                    nodeRef.left = None
                    break

               elif(nodeRef.value == value and nodeRef.right.left==None):       #node to be deleted has a right child and the right child has no left child
                    delNodeLeft = nodeRef.left
                    if(point.value<nodeRef.value):
                         point.right = nodeRef.right
                         point.right.left = delNodeLeft
                    elif(point.value>nodeRef.value):
                         point.left = nodeRef.right
                         point.left.left=delNodeLeft
                    break

               elif(nodeRef.value == value and nodeRef.right.left!=None):       #node to be deleted has a right child and the right child has a left child

                    l = nodeRef.right.left
                    lb = nodeRef.right

                    while(l.left!=None):
                         lb = l
                         l = l.left

                    if(l.right != None):
                         lb.left = l.right
                         
                    l.right = nodeRef.right
                    l.left = nodeRef.left
                    
                    if(point.value<nodeRef.value):
                         point.right = l
                    elif(point.value>nodeRef.value):
                         point.left = l
                    break




a=BST()
a.insert(9)
a.insert(4)
a.insert(3)
a.insert(6)
a.insert(20)
a.insert(15)
a.insert(170)              
                    
                         
                    
                    










     
