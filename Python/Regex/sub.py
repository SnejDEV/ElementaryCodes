import re

s="Indha number 1 number 2 ella paapa veliyaata, I'm the only 1, the super 1"
result = re.sub(r'1','one',s)
result = re.sub(r'2','two',result)
print(result)
