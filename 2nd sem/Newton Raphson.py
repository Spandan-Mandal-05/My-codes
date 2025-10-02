import numpy as np
def f(x):
    return (x**3-4)
def fn(x):
    return (f(x+h)-f(x))/h
i=0
x=4
h=1e-8
while abs(f(x)>h):
    x=x-f(x)/fn(x)
    i+=1
print(i,x)