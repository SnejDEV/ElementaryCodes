import logging

a = int(input("Enter an even number: "))
logging.basicConfig(filename="assertLog.log", level = logging.DEBUG)
try:
     assert a%2==0,"Invalid Input, maybe an odd number is entered"
except AssertionError as obj:
     logging.error(obj)
     print(obj)
else:
     print("a+2="+str(a+2))
finally:
     logging.info("addition succesful")
     
     
