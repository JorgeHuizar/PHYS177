"""
Prob 2.4
Jorge Huizar
"""

import numpy as np
from IntFunct import trapInt
def f(x):
    return (np.sin(np.sqrt(100 * x))**2)
    
#Here I have the actual values of the integration and the x values we will be
#integrating to and from. The number of bins we start at is 10 and we double it
#to increase the accuracy of our integration.


actual = .4558325
a = 0.
b = 1.
N = 10

#I set the value of the error high to start cutting it down.
#I also set the integration value to 0

error = 1.
Integration1 = 0.

#While our error is more than the desired value, our function will increase
#the number of bins to make the integration more accurate.

while error > .000001:
    Integration1 = trapInt(f,a,b,N)
    N = N * 2
    error = np.abs((actual - Integration1)/3)
    

print "Actual integration value: ", actual
print "My Integration: ",Integration1
print "Number of slices used: ", N
