try:
     f=open("sj.txt","r")
     a,b=[int(x) for x in input("Enter 2 numbers: ").split()]
     c=a/b
except ZeroDivisionError:
     print("Division by 0 is not possible :( ");
finally:
     f.close()
     print("File Closed")

print(c)
