from random import choice

class coin:
    def __init__(self,clean=True,**kwargs):
        for keys,values in kwargs.items():
            setattr(self,keys,values)
        
        self.rare=self.rare
        self.value = ((25/100)*self.value)+self.value if(self.rare==True) else self.value
        self.colour=self.origC if clean==True else self.rustC
        
    def rust(self):
        self.colour=self.rustC

    def clean(self):
        self.colour=self.origC

    def flip(self):
        self.heads = choice([True,False])
        self.tails = False if(self.heads==True) else True

    def __del__(self):
        print("Coin spent")

class Rupee(coin):
    def __init__(self):
        d={ "value" : 1.00,
            "origC" : "Silver",
            "rustC" : "Brown",
            "num_edges" : 1,
            "diameter" : 25,
            "thickness" : 1.45,
            "heads" : True,
            "rare":True,
            #"clean":False
          }
        super().__init__(**d)
c=Rupee()

        
