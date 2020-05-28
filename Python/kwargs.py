dic={}

def pr(male,female,custom):                                  #** used for packing data(** used along with parameters)
    #for keys,values in kwargs.items():
        print("{}:{}:{}".format(male,female,custom))

print("Enter keys and respective values")
while True:

    c=(input("Enter key if u want to continue, else enter (N/n)")).strip()

    if(c=='n' or c=='N'):
        #print(pr(**dic))                          # ** used for unpacking data(used along with args)----{packing ** unpacked data with **<variable>}this wont
                                                   #   work as it doesnt pass the key value and it passes oly value to the function
                                                   #   INSTEAD PASS VALS IN THE SYNTAX <var>=<value>
        dic={"male":"Snehal","female":"Hemal","custom":"Richooths"}    
        pr(**dic)
        #pr(male="Snehal",female="Hemal",custom="Richooths")                                           
        break
    else:
        dic[c]=input("Enter value") 
        print(dic)
    #else: print("invalid text entered")

        
#refer self-made docs for concepts
