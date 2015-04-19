"""
Problem 2.3
Jorge Huizar
"""
import numpy as np
from scipy import integrate
from IntFunct import trapInt, simpsonInt

#We have our function so we can integrate using this
def f(x):
   return x**4 - 2 * x + 1
    
#The integration is done from x=0 to x=2 with 20 slices
a = 0.
b = 2.
N = 20

#Our values of x and y are evaluated at the intervals which x is an integer
x = np.array([0,1,2])
y = f(x)

#Call up our own functions and the scipy integrated functions to compute the
#integrals.
I1 = trapInt(f,a,b,N)
I2 = simpsonInt(f,a,b,N)

I3 = integrate.simps(y,x)
I4 = integrate.trapz(y,x)

print "My own Trapezoidal Integration: ",I1
print "My own Simpsons Integration: ", I2
print "Scipy Trapezoidal Integration: ", I3
print "Scipy Simpson Integration: ", I4
print "Actual Integration: ", 4.4

#Error between the scipy functions and mine
Error1 = (I4 - I2)/15
Error2 = (I3 - I1)/3
print "Simpson's Error: ", Error1
print "Trapezoidal Error: ", Error2
