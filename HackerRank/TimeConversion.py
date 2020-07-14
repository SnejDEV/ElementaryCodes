t = input()
sp = t.split(':')
sp.append(sp[2][0:2])
sp.append(sp[2][2:])
del sp[2]

if(sp[0]=='12' and sp[3]=='AM'):
    sp[0] = '00'
elif(int(sp[0])>=1 and sp[0]!='12' and sp[3]=="PM"):
    sp[0] = str(int(sp[0])+12)

print("{}:{}:{}".format(sp[0],sp[1],sp[2]))
