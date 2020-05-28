class Stack():

     def __init__(self):
          self.value = []
          self.length = 0

     def push(self,value):
          self.value.append(value)

     def pop(self):
          self.length-=1
          return(self.value.pop())

     def peek(self):
          return(self.value[self.length-1])
