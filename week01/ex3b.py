import numpy as np
import matplotlib.pyplot as plt



#Range we are measuring
vmin = input("Enter minimum velocity: ")
vmin = float(vmin)
vmax = input("Enter maximum velocity: ")
vmax = float(vmax)

#height of the tower and constant of gravity
d = 800.
g = 9.81

dv = (vmax-vmin)/10
v_init = vmin + np.arange(10) * dv + dv/2.

t = (v_init + (v_init**2 - (2 * g * d)**(0.5)))/g


plt.plot(v_init, t,'o-',color = 'blue')
plt.show()

print t
np.savetxt('Times.txt',t)
