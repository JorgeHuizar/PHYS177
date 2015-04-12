from math import sqrt


d = 800.
g = 9.81

#vi is the velocity at which the ball is thrown downward
vi = input("Enter the initial velocity (positive for downward, netagive for upward): ")
v = float(vi)


#t1 = time it take for the ball to reach the ground
t1 = (-vi + sqrt(vi**2. - (2. * g * -d)))/g


print t1
