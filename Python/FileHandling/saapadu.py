class Saapadu:
     def __init__(self,name,qty,price):
          self.name = name
          self.qty = qty
          self.price = price
          
     def __str__(self):
          return("{} {} {}".format(self.name,self.qty,self.price))
