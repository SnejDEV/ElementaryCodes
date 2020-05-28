class Account:
    def __init__(self,name,dep,minB):
        """accepts vals"""
        self.r=0
        self.minB=minB
        self.dep=dep
        self.name=name
        self.type="Current Account" if(self.minB==-1000) else "Savings Account"
    def deposit(self,amt):
        self.dep+=amt
    def withdraw(self,amt):
        l=[self.dep-amt,print("Withdrawal successful")] if((self.dep-amt)>=self.minB) else [self.dep,print("Insufficient Funds")]  #l[1]Stores None val which print()returns
        self.dep = l[0]
    def statement(self):
        print(self.name+"'s Balance = "+str(self.dep))
    def __str__(self):
        return("Account Name : {}\nAccount Type : {}\nAccount Balance : {}".format(self.name,self.type,self.dep))
    def __del__(self):
        print("Account Name : {}\nAccount Type : {}\nAccount Status : {}".format(self.name,self.type,"Deleted"))
        
            
class Current(Account):
    def __init__(self,name,dep):
        super().__init__(name,dep,-1000)

class Savings(Account):
    def __init__(self,name,dep):
        super().__init__(name,dep,0)

    
