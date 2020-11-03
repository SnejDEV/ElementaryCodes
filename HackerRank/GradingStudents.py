n = input()
a = []

for x in range(0,int(n)):
    i = input()
    i.strip()
    l = len(i)
    
    if(int(i)<38):
        a.append(int(i))
    else:
        ldigit = int(i[l-1])
        if(ldigit<5 and 5-int(ldigit)<3):
            a.append(int(i)+(5-int(ldigit)))
        elif(ldigit>5 and 10-int(ldigit)<3):
            a.append(int(i)+(10-int(ldigit)))
        else:
            a.append(int(i))
print(*a,sep = "\n")
