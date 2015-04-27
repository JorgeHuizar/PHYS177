"""
Jorge Huizar
SID 861063727
"""
import numpy as np
#Voltage Equations [Part a]
#4V1 - V2 - -V3 - V4 = V+
#-V1 + 3V2 - 0V3 - V4 = 0
#-V1 - 0V2 + 3V3 - V4 = V+
#-V1 - V2 - V3 + 4V4 = 0


###
#Here we have the matrix for the Voltage equations [Part b]
###

voltage = np.array(([4,-1,-1,-1],[-1,3,0,-1],[-1,0,3,-1],[-1,-1,-1,4]),dtype=float)

ans = np.array([5,0,5,0],dtype=float)
N = len(ans)

for m in range(N): #This for loop divides the matrix by the diagonal
    div = voltage[m,m]
    voltage[m,:] /= div
    ans[m] /= div
    
    for i in range(m+1,N): #This loop subtracts from the lower rows to be able
                            #to divide again
        mult = voltage[i,m]
        voltage[i,:] -= mult*voltage[m,:]
        ans[i] -= mult*ans[m]

final_ans = np.empty(N,float)

for m in range(N-1,-1,-1): #Here we apply back substitution
    final_ans[m] = ans[m]
    for i in range(m+1,N):
        final_ans[m] -= voltage[m,i]*final_ans[i]

print "V1 - V4 Solutions: "
print "V1: ", final_ans[0]
print "V2: ", final_ans[1]
print "V3: ", final_ans[2]
print "V4: ", final_ans[3]

#This does what is shown above, using the numpy function to calculate the linear
#solutions for our equations. [Part c]
y = np.linalg.solve(voltage,ans)
print "Numpy Function Solutions: ",y
