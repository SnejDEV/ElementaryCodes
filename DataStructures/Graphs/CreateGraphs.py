class Graph:
     def __init__(self):
          self.graph = {}
          self.length = 0

     def addNode(self,node):
          self.graph[node] = []
          self.length+=1

     def addEdge(self,node1,node2):
          self.graph[node1].append(node2)
          self.graph[node2].append(node1)
          
