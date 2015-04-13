"""
Functions for integrating using the Trapezoidal rule and Simpson's Rule
"""

def trapInt(f,a,b,N):
    
    #Trapezoidal Rule
    
    h = (b - a)/float(N)
    
    Itrap = 0.5 * f(a) + 0.5 * f(b)
    
    for k in range(1,N):
        Itrap = Itrap + f(a + k*h)
    
    I = Itrap * h
    return I



def simpsonInt(f,a,b,N):
    
    #Simpson's Rule
    
    h = (b - a)/float(N)
    
    I = f(a) + f(b)
    
    I1 = 0.0
    for k in range(1,N,2):
        I1 = I1 + f(a + k * h)
    
    
    I2 = 0.0
    for k in range(2,N,2):
        I2 = I2 + f(a + k * h)
    
    
    I = (I + 4.* I1+ 2.*I2) * (h/3.)
    return I
