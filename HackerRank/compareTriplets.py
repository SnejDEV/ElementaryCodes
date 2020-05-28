def accept():
    a=[]
    while(len(a)!=3):
        a=input()#.split(' ')
    return a

def compare():
    global l
    for x in range(0,3):
        alice[x],bob[x]=int(alice[x]),int(bob[x])
        l=[l[0]+1,l[1]] if alice[x]>bob[x] else ([l[0],l[1]] if(alice[x]==bob[x]) else [l[0],l[1]+1])

l=[0,0]
alice = accept()
bob=accept()
compare()
print(l[0],l[1])
