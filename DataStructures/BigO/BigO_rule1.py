a=["nemo","kaamu","laamu","raamu","jaamu"]

def findNemo(array):
    for x in array:
        if(x=="nemo"):
            print("Found NEMO!")
            break

findNemo(a)                         #BIG-O IS NOT O(1) JUST BCOZ nemo is @a[0]
                                    #ACCORDING TO RULE 1 WE TAKE IT AS O(n) BCOZ IN THE WORSTEST OF CONDITIONS NEMO MIGHT BE @a[4] as it is the iNpUt
