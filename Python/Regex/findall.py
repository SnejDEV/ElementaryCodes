import re

s="Gomma vainko"
result = re.findall(r'\w\w',s)
print(result)                      #findall() returns list, so neednt use group(), group() is used when an object is returned
