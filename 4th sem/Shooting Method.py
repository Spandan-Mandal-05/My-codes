#Shooting Method using Linear Interpolation

import matplotlib.pyplot as plt
import numpy as np

#Define Differential Eq
def d2y_dx2(x,y,g):
    return g + 6*y 

#Define Analytical Eq
def f(x):
    return 6/5 * np.exp(-2*x) + 4/5 * np.exp(3*x)

def sol_ode(initial_state , boundary_state):
    n = 10000
    xf = boundary_state
    xi,yi,gi = initial_state
    h = (xf-xi)/(n-1)

    xx = np.linspace(xi,xf+h,n+1)
    yy = f(xx)

    yy_modified = np.zeros_like(xx)
    gg_modified = np.zeros_like(xx)

    yy_modified[0] , gg_modified[0] = yi , gi

    for i in range (n):
        gg_temp = gg_modified[i] + h * d2y_dx2(xx[i],yy_modified[i],gg_modified[i])
        yy_temp = yy_modified[i] + h * gg_temp

        gg_modified[i+1] = gg_modified[i] + h/2 * (d2y_dx2(xx[i+1],yy_temp,gg_temp) + d2y_dx2(xx[i],yy_modified[i],gg_modified[i]))
        yy_modified[i+1] = yy_modified[i] + h/2 * (gg_modified[i] + gg_temp)

    y_boundary = yy_modified[n]
    return xx, yy , yy_modified , y_boundary

xi , xf , yi , yf = 0 , 1 , f(0) , f(1) #Initialize the Boundary Conditions

gg_shoot = np.arange(-2,2,0.002)
yy_boundary = np.zeros_like(gg_shoot)
fig,ax = plt.subplots(figsize=[12,8])

for j in range(len(gg_shoot)):
    initia_states = xi,yi,gg_shoot[j]
    xx, yy , yy_modified , y_boundary = sol_ode(initia_states,xf)
    yy_boundary[j] = y_boundary
    
    if abs(y_boundary - yf) >= 0.5:
        plt.plot(xx,yy_modified, color = "black",alpha= 0.2)
    #if abs(y_boundary - yf) <= 0.01:
        #plt.plot(xx,yy_modified,linestyle="*",color = "black",alpha=0.3) 
    else:
        plt.plot(xx,yy_modified, label=f"{round(y_boundary - yf,3)}, initial slope = {np.round((gg_shoot[j]),3)}")
plt.plot(xx,yy,color="black")
plt.legend()
plt.show()


sorted_indices = np.argsort(abs(yy_boundary - yf))  # Sort indices based on error
gg_shoot = gg_shoot[sorted_indices]  # Rearrange gg_shoot accordingly
yy_boundary = yy_boundary[sorted_indices]  # Keep mapping intact

M = gg_shoot[2] + (yf - yy_boundary[2]) * ( gg_shoot[2] - gg_shoot[1] ) / (yy_boundary[2] - yy_boundary[1])

print(round(M,4))