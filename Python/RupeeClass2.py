from random import choice

class Rupee:

    def __init__(self,rare=False):
        self.rare=rare
        self.value = 1.25 if(self.rare==True) else 1.00
        
        #self.value = 1.00
        self.colour = "Silver"
        self.num_edges = 1
        self.diameter = 25
        self.thickness = 1.45
        self.heads = True
        self.tails = False

    def rust(self):
        self.colour="Brown"

    def clean(self):
        self.colour="Silver"

    def flip(self):
        self.heads = choice([True,False])
        self.tails = False if(self.heads==True) else True

    def __del__(self):
        print("Coin spent")
        
'''  Syntax      
coin1 = Rupee(True)
coin1.rust()
coin1.clean()
coin1.flip()
del coin
'''
