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

    def __str__(self):
        return("{} rupee coin".format(int(self.value)))
        

class One_Rupee(coin):
    def __init__(self):
        d={ "value" : 1.00,
            "origC" : "Silver",
            "rustC" : "Brown",
            "num_edges" : 1,
            "diameter" : 25,
            "thickness" : 1.45,
            "heads" : True,
            "rare":False
            #"clean":False
          }
        super().__init__(**d)

class Ten_Rupee(coin):
    def __init__(self):
        d={ "value" : 10.00,
            "origC" : "Silver",
            "rustC" : "Brown",
            "num_edges" : 1,
            "diameter" : 25,
            "thickness" : 1.45,
            "heads" : True,
            "rare":False
            #"clean":False
          }
        super().__init__(**d)

class Ten_RupeeP(coin):
    def __init__(self):
        d={ "value" : 10.00,
            "form"  : "Paper",
            "origC"  : "Brown",
            "num_edges" : 1,
            "diameter" : "Gomma u except notes to have dia va?",
            "thickness" : 0.2,
            #"heads" : True,
            "rare":False
            #"clean":False
          }
        super().__init__(**d)
        
    '''************Overiding Methods************'''
    def rust(self):
        print("Papers dont rust")

    def clean(self):
        print("Rupee note cleaned")

    def flip(self):
        print("Papers dont flip")

    def __str__(self):
        return("{} rupee".format(int(self.value)))
    '''************Overiding Methods************'''

l = [One_Rupee(),Ten_Rupee(),Ten_RupeeP()]
for coin in l:
    arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness,
                           coin.num_edges]

    string = "{} - Colour: {}, value:{}, diameter(mm):{}, thickness(mm):{}, number of edges:{}".format(*arguments)
    print(string)
