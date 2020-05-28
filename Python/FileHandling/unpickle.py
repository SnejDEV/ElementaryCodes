import pickle,saapadu
import logging

logging.basicConfig(filename="logs.log",level=logging.DEBUG)

try:
     f=open("objects.dat",'rb')
     obj=pickle.load(f)
except FileNotFoundError:
     print("File not found")
     logging.error("File not found")
except EOFError as e:
     print(e)
     logging.error(e)
     f.close()
else:
     print(obj)
     f.close()
     logging.info("Successful")

