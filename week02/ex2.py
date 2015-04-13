import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

######
#I could not get my own functions to input x and y values
#I did the next best thing to provide an integration of the given values
#from the velocities.txt file provided.
######


x,y = np.loadtxt('C:/users/Jorge Huizar/Dropbox/177/Lab 2/velocities.txt',unpack=True)


Isimp = integrate.simps(y,x)
Itrap = integrate.trapz(y,x)

print Isimp
print Itrap

plt.plot(x,y)
plt.title('Time vs. Velocity')
plt.xlabel('Time in seconds')
plt.ylabel('Measured Velocity')
plt.show()
