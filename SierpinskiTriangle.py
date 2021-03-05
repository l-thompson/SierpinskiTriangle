import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
<<<<<<< HEAD
from random import randint                               
=======
from numpy import sqrt
from random import randint
>>>>>>> 79b93162120531fb69ace82afd5df1f18cbe7092

#Here's what happens:
#	1. Start in the middle of the triangle.
#	2. Measure half the distance to a randomly chosen corner.
#	3. Plot the point.
#	4. Repeat from 2.

#When prompted:
#        Enter a natural number for the number of points.
#        Enter an N or Y to choose an animationd or static plot.

# the points are (0,0),(1,0),(0.5,1)
xc = [0,0.5,0.25]
yc = [0,0,0.5]
res = [] # list of lists, each one a point [x,y]
    
if __name__ == "__main__":
    
    def animate(k):
        ax.scatter(x[k],y[k],1,"r","+")
    
    # Initial conditions
    x = 0.25
    y = 0.25
    try: i = int(input("How many points? "))
    except: i = 50000
    try: a = str(input("Would you like it animated? (Y/N) "))
    except: a = "N"
    if (a.strip() != "Y") and (a.strip() != "N"): a = "N"
    else: pass
    
    # Add point to list. Select random corner. Cut the distance in half. Repeat. 
    for p in range(i):
        res.append([x,y])
        n = randint(0,2)
        x = (x+xc[n])/2
        y = (y+yc[n])/2
    
    # Separate out list of lists "res" into x and y lists
    x = [i[0] for i in res]
    y = [j[1] for j in res]
    
    # Set up the plot
    fig,ax = plt.subplots(figsize=(10,10))
    ax.set_xlim(min(x),max(x))
    ax.set_ylim(min(y),max(y))
    if a == "Y": ani = FuncAnimation(fig, animate, frames=len(x))
    elif a == "N": ax.scatter(x,y,1,"r","+")
    else: print("Whatever, man.")
    plt.show()
