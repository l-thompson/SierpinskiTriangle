import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import sqrt,exp, real, imag
from math import pi
from random import randint

#Here's what happens:
#1. Start in the middle of the polygon.
#2. Measure (1/chosen) the distance to a randomly chosen corner.
#3. Plot that point.
#4. Repeat from 2.

def chaosPolygon(x,y,n,i,f):
    # Draw a circle, and pick n evenly spaced points along the circle
    coord = []
    for v in range(n): coord.append([real(exp(1j*(v/n)*2*pi)), imag(exp(1j*(v/n)*2*pi))])
    # gather vertices
    xc = [i[0] for i in coord]
    yc = [j[1] for j in coord]
    # Add point to list. Select random corner. Cut the distance in half. Repeat.
    res = []
    for k in range(i):
        res.append([x,y])
        v = randint(0,n-1)
        x = (x+xc[v])/f
        y = (y+yc[v])/f
    return res

if __name__ == "__main__":
    # Initial conditions
    x = 0
    y = 0
    try: i = int(input("How many iterations? "))
    except: i = 200000
    try: a = str(input("Would you like it animated? (Y/N) "))
    except: a = "N"
    try: sides = int(input("How many sides? "))
    except: sides = 3
    try: f = int(input("1/(natural number) to next vertex: "))
    except: f = 2
    if (a.strip() != "Y") and (a.strip() != "N"): a = "N"
    else: pass
    
    points = chaosPolygon(x,y,sides,i,f)
    
    # Separate out list of lists into x and y lists
    x = [i[0] for i in points]
    y = [j[1] for j in points]
    
    # Set up the plot
    fig,ax = plt.subplots(figsize=(10,10))
    ax.set_xlim(-1.2,1.2)
    ax.set_ylim(-1.2,1.2)
    
    def animate(k): ax.scatter(x[k],y[k],1,"r","+")
    
    # output control
    if "Y" in a: ani = FuncAnimation(fig, animate, frames=len(x))
    elif "N" in a: ax.scatter(x,y,1,"r","+")
    else: print("Whatever, man.")
    
    plt.show()
