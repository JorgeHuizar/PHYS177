from IntFunct import simpsonInt,trapInt

def f(x):
    return x**2 + x

a=0.
b=2.
N=10

print simpsonInt(f,a,b,N)


print trapInt(f,a,b,N)
