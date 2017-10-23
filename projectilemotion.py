import matplotlib.pyplot as plt
from math import *
from numpy import *

numberofgraph=int(input("how many graph?"))

for i in range (0,numberofgraph):
    degree=int(input("degree:"))
    rad=radians(degree)
    v=int(input("velocity:"))

    numx=[]
    numy=[]

    time=((2*v)*sin(rad))/9.8
    xv=cos(rad)*v
    yv=sin(rad)*v


    for t in arange(0.0, 1000, 0.01):

        height=(yv*t)-((9.8*(t**2))*0.5)
        if height > 0:
            numy.append(height)
            numx.append(xv*t)

    plt.plot(numx,numy)
plt.show()

