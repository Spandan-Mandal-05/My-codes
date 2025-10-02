import numpy as np
import matplotlib.pyplot as plt

def dvdt( ):
    return

Vi=10
R= 1000
C= 100e-6
t=0
vc=0
tf=10
n=10000
h=(tf-t)/(n-1)
t
for i in range(n):
    t=t+h
    vc=vc+dvdt()*h


