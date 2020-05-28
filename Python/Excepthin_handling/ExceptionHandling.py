c=0
try:
     a,b = [int(x) for x in input("Enter 2 numbers: ").split()]
     c=a/b
     print(c)
except ZeroDivisionError:
     print("Zero division is impossible da dumbfuck")
print("<Code>")
