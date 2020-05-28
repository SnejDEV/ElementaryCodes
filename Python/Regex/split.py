#this code splits the strings according to to the delimiter defined in the form of regex
import re

s="I am 17. I am a dumbfuck"
result=re.split(r"\d+",s)
print(result)
