"""
Jorge Huizar
PHYS 177 Prof. L. Sales
Final Project
"""
import numpy as np
import matplotlib.pyplot as plt

###
#This is function describes the second order differential equation given in the
#book. It takes in arrays of the positions of each star, the masses of the two
#stars whos position is not being calculated, and returns the acceleration as
#a vector of direction X and Y.
####

def vDot(r,a,b,massA,massB):
    G = 1.
    
    rDoubleDotX = G*massA*(a[0]-r[0])/((a[0]-r[0])**2+(a[1]-r[1])**2)**(3/2)
    + G*massB*(b[0]-r[0])/((b[0]-r[0])**2+(b[1]-r[1])**2)**(3/2)
    
    rDoubleDotY = G*massA*(a[1]-r[1])/((a[0]-r[0])**2+(a[1]-r[1])**2)**(3/2)
    + G*massB*(b[1]-r[1])/((a[0]-r[0])**2+(b[1]-r[1])**2)**(3/2)

    return np.array([rDoubleDotX,rDoubleDotY],float)

###
#These are the initial conditions I used to begin the calculations
###

m1 = 150.
m2 = 200.
m3 = 250.
r1 = np.array([3.,1.],float)
r2 = np.array([-1.,-2.],float)
r3 = np.array([-1.,1.],float)
r1velocity = np.array([0,0],float)
r2velocity = np.array([0,0],float)
r3velocity = np.array([0,0],float)

a = 0.0
b = 2.0
N = 10000
h = (b-a)/N


tpoints = np.linspace(a,b,N)
r1posX = []
r1posY = []
r2posX = []
r2posY = []
r3posY = []
r3posX = []

###
#My Runge-Kutta calculations gave back a vector of velcity which I used to
#calculate the position of the stars.
###
for t in tpoints:
    r1posX.append(r1[0])
    r1posY.append(r1[1])
    
    r2posX.append(r2[0])
    r2posY.append(r2[1]) 

    r3posX.append(r3[0])
    r3posY.append(r3[1])
    
    k1 = h*vDot(r1,r2,r3,m2,m3)
    k2 = h*vDot(r1+0.5*k1,r2,r3,m2,m3)
    k3 = h*vDot(r1+0.5*k2,r2,r3,m2,m3)
    k4 = h*vDot(r1+k3,r2,r3,m2,m3)
    r1+= h*r1velocity
    r1velocity += (k1+2*k2+2*k3+k4)/6
    
    l1 = h*vDot(r2,r1,r3,m1,m3)
    l2 = h*vDot(r2+0.5*l1,r1,r3,m1,m3)
    l3 = h*vDot(r2+0.5*l2,r1,r3,m1,m3)
    l4 = h*vDot(r2+l3,r1,r3,m1,m3)
    r2+= h*r2velocity
    r2velocity += (l1+2*l2+2*l3+l4)/6    
     
    j1 = h*vDot(r3,r1,r2,m1,m2)
    j2 = h*vDot(r3+0.5*j1,r1,r2,m1,m2)
    j3 = h*vDot(r3+0.5*j2,r1,r2,m1,m2)
    j4 = h*vDot(r3+j3,r1,r2,m1,m2)
    r3+= h*r3velocity
    r3velocity += (j1+2*j2+2*j3+j4)/6

###
#Plot of the positions of the stars
###

plt.plot(r1posX,r1posY)
plt.plot(r2posX,r2posY)
plt.plot(r3posX,r3posY)
plt.show()
