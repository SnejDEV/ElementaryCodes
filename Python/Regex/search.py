# A code which returns the substrings which starts with o nd is followed by another char
import re
import logging

logging.basicConfig(filename="logs.log",level = logging.DEBUG)

s="I am Snehal Jayachander popularly known to be the biggest dumbhead"
result=re.search(r'o\w',s)
try:
     print(result.group())                        #group() is used since search() returns an object
except AttributeError as obj:
     logging.error(obj)
     print(str(obj))
