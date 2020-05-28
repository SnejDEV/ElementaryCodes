data = {"male":[],
        "female":[]}

for a in data.keys():
    #i=0
    b = ((input("do u want to add more members to {0}(y/n): ".format(a)).strip()).lower())
    while(b=='y'):
        data[a].append(input("Enter name"))
        b =((input("do u want to continue?(y/n): ").strip()).lower())
        #i=i+1
    for n in data[a]:
        print(n)
        
print(data)        
