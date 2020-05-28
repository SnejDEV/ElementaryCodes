a=10

def man():
    a=5         #locVar creation
    print(a)

print(a)

def man1():
    global a    #global access
    a=5         
    print(a)

man()
man1()
print(a)    
