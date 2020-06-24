class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self,v):
        node = Node(v)

        if(self.length==0):
            self.head = node
            self.length+=1
        else:
            nodeRef = self.head

            while(nodeRef != None):
                if(v>nodeRef.value):
                    if(nodeRef.right == None):
                        nodeRef.right = node
                        break
                    nodeRef = nodeRef.right

                elif(v<nodeRef.value):
                    if(nodeRef.left == None):
                        nodeRef.left =node
                        break
                    nodeRef = nodeRef.left

    def search(self,s):
        nodeRef = self.head
        while(nodeRef!=None):
            if(nodeRef.value==s):
                return("Found")
            elif(s>nodeRef.value):
                nodeRef = nodeRef.right
            elif(s<nodeRef.vaue):
                nodeRef = nodeRef.left
        return("Not Found")
