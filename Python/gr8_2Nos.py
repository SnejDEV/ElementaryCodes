#Enter num1 nd num2 vals
num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
num1 = int(num1.strip())
num2 = int(num2.strip())

if(num1>num2):
    print("{0} is greater than {1}".format(num1,num2))
elif(num2>num1):
    print("{1} is greater than {0}".format(num1,num2))
elif(num1==num2):
    print("{0} is equal to {1}".format(num1,num2))
