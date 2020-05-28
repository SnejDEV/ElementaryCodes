try:
     f=open("sj.txt","r")
     a,b=[int(x) for x in input("Enter 2 numbers: ").split()]
     c=a/b
except ZeroDivisionError as obj:
     print("Division by 0 is not possible :( ");
     print(obj)
else:
     print("b was non-zero")
finally:
     f.close()
     print("File Closed")

#print(c)
