'''class Graph:
     def __init__(self):
          self.graph = {}
          self.length = 0

     def addNode(self,node):
          self.graph[node] = []
          self.length+=1

     def addEdge(self,node1,node2):
          self.graph[node1].append(node2)
          self.graph[node2].append(node1)
'''

class Node:
    def __init__(self,value):
        self.value = value
        self.edges = []

class Graph():
    def __init__(self):
        self.Graph = {}

    def addNode(self,i,val):
        self.Graph[i]=Node(val)

    def addEdge(self,i1,i2,d):                              #d is direction, 1 is uni nd 2 is bi
        self.Graph[i1].edges.append(self.Graph[i2])
        if(d==2):
            self.Graph[i2].edges.append(self.Graph[i1])
