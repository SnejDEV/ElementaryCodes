import matplotlib.pyplot as plt

x = [0,1,2,3]
y = [0,1,2,3]

plt.plot(x,y)

#plt.title("LTS\nThere you go")
plt.title("LTS{}There you go".format("\n"))

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()
