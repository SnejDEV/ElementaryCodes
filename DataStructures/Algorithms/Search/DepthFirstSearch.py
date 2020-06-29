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
a.insert(11)
a.insert(4)
a.insert(2)
a.insert(5)
a.insert(10)
a.insert(15)

l=[]

def DFS_IN(b):
    global l
    if(b.left!=None):
        DFS_IN(b.left)
    l.append(b.value)
    if(b.right!=None):
        DFS_IN(b.right)

def DFS_PRE(b):
    global l
    l.append(b.value)
    if(b.left!=None):
        DFS_PRE(b.left)
    if(b.right!=None):
        DFS_PRE(b.right)

def DFS_POST(b):
    global l
    if(b.left!=None):
        DFS_POST(b.left)
    if(b.right!=None):
        DFS_POST(b.right)
    l.append(b.value)

def traverse():
    global l
    l=[]
    inp = int(input("Enter an appropriate DFS order \n 1) In-Order \n 2) Pre-Order \n 3) Post-Order \n"))
    if(inp==1):
        DFS_IN(a.root)
        return(l)
    elif(inp==2):
        DFS_PRE(a.root)
        return(l)
    elif(inp==3):
        DFS_POST(a.root)
        return(l)

                













        
