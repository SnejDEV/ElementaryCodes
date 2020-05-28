a=[x for x in range(0,1000)]

def b(a):
    print(a[0])                 #O[1]--Op1
    print(a[1])                 #O[1]--Op2
b(a)                            '''O[2]--op1+op1(total no. of operations remain
                                              2 whatever the number of inputs is
                                              so IT IS CONSTANT TIME)
                                              WE WRITE CONSTANT AS O(1)'''
