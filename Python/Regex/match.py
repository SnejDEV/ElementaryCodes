import re

s="Gomma vainko"
result = re.match(r'\w\w',s)                 
print(result.group())              #group() is used since match() returns an object
     
