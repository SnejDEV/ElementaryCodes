'''a=1
for i in range(0,5):
    a=a+1
print(a)  '''

a=1
while(a==1):
    print("while entry")
    for x in range(0,10):
        print(x)
        if(x==4):
            continue
    a+=1
