"""
Jorge Huizar
SID: 861063727
Lab 5 Ex 1
"""

import numpy as np
import matplotlib.pyplot as plt



#Define the polynomial
def pol(x):
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1
    
#For the plot we use x and y values. Our x values are chosen to be between
#0-1 by 100 divisions of .01. Y values are evaluated at those points.

x = np.arange(0,1,.01)
y = np.zeros(len(x))
y[:]=pol(x[:])

#Plotting x and y
plt.plot(x,y)
plt.show()
plt.savefig("PolynomialPlot.png")

#Here I uesd an array to select my guesses for the root values.
guess = np.array([0.0341,0.1694,0.3807,0.6192,0.8306,0.9658])
h=.000001


for k in range(len(guess)):
    
    #I set the error and the accuracy to begin my while loop.
    error = 1
    accuracy = 10e-10
    x = guess[k]
    
    while error > accuracy:
        pol_deriv = (pol(x+h)-pol(x-h))/(2*h)
        x = x - pol(x)/pol_deriv
        error = abs(pol(x)/pol_deriv)
    print "Root Value: ", x
    print "Error Value: ", error
