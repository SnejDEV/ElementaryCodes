import re

s="Its amazing to have Sunny Leone as my beloved wife, the desire and passion cannot be explained through words, but deeds may"
w=[r'I\D+',r'S\w*',r'S\w?',r'S\D{11}',r'S\w{1,11}']

for x in range(0,5):
     result = re.findall(w[x],s)
     print(result)

