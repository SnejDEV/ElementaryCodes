import logging

logging.basicConfig(filename="sjlog.log",level=logging.DEBUG)
try:
     f=open("E:\Python_Bible\Advanced_Python\ExceptionHandling\sj.txt","r")
     logging.info("sj.txt opened")
     a,b=[int(x) for x in input("Enter 2 numbers: ").split()]
     c=a/b
     logging.info("Division in process")
except ZeroDivisionError:
     print("Division by 0 is not possible :( ");
     logging.error("Attempt to divide by 0")
else:
     print("b was non-zero")
finally:
     f.close()
     print("File Closed")
     logging.info("sj.txt closed")

#print(c)
