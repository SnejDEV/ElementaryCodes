a=[1,2,3]

def man():
    a=5        #locVar creation
    print(a)

print(a)

def man1():
    a[0]=5     #py understands user's global access intention       
    print(a)

man()
man1()
print(a)    
