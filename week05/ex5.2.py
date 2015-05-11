"""
Jorge Huizar
SID 861063717
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy

#Taken from the book and class example
def dft(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c

#Number of points we will use and the time vector for it
N = 1000
t = np.linspace(0, 1,N)

#Arrays to hold the y values of the functions
square_array = np.zeros(N)
sawtooth_array = np.zeros(N)
mod_sin_array = np.zeros(N)

#Functions evaluated at the different time points
for k in range(len(t)):
    square_array[k] = scipy.signal.square(2 * np.pi * t[k])
    sawtooth_array[k] = scipy.signal.sawtooth(2 * np.pi * t[k])
    mod_sin_array[k] = np.sin(np.pi * t[k] / N)* np.sin(20*np.pi*t[k]/N)

#Coefficients of the evaluated arrays
sawtooth_coeff = dft(sawtooth_array)
square_coeff = dft(square_array)
mod_sin_coeff = dft(mod_sin_array)

#Plots
plt.subplot(311)
plt.plot(abs(sawtooth_coeff))
plt.subplot(312)
plt.plot(abs(square_coeff))
plt.subplot(313)
plt.plot(abs(mod_sin_coeff))
plt.xlim(0,1000)
plt.show()
