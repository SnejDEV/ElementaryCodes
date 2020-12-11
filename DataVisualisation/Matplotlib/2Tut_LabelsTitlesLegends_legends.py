import matplotlib.pyplot as plt

n = ""
xq1 = []
yq1 = []
xq2 = []
yq2 = []

def UI():
    global n,xq1,yq1,xq2,yq2
    
    plt_setup(input("Enter Graph title: "),input("Enter xlabel: "),input("Enter ylabel: "))
        
    while(n!="fuckoff"):
        x = int(input("Enter x value: "))
        y = int(input("Enter y value: "))

        #quadrants 1 and 2
        if(x>0):
            xq1.append(x)
            yq1.append(y)
        elif(x<0):
            xq2.append(x)
            yq2.append(y)
        elif(x==0):
            xq1.append(x)
            yq1.append(y)
            xq2.append(x)
            yq2.append(y)

        n = input("Enter fuckoff to exit, else put something random: ")
 
    plot(xq1,yq1,xq2,yq2)


def plot(xq1co,yq1co,xq2co,yq2co):
    plt.plot(xq1co,yq1co,label = "Line1")
    plt.plot(xq2co,yq2co,label = "Line2")
    plt.legend()
    plt.show()

def plt_setup(title,xlabel,ylabel):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

if(__name__=="__main__"):
    UI()
