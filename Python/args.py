l=[]
total=0

def add(*num):                                  # * used for packing data(cao its used along with parameters)
    print(type(num))
    global total
    for x in num:
        total=total+x
    return(total)
#print(add([1,2,3]))

print("Enter numbers")
while True:

    c=(input("Enter number if u want to continue, else enter (N/n)")).strip()

    if(c=='n' or c=='N'):
        print(add(*l))                          # * used for packing data(used along with args)
        break
    elif(c.isdigit()):
        l.append(float(c))
        print(l)
    else: print("invalid text entered")

        
#refer self-made docs for concepts
