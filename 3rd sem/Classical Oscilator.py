import matplotlib.pyplot as plt 
import numpy as np

def f(m,k,k1,t,x1,v1,x2,v2):
    velocity_1 = v1
    acceleration_1 = k1*x2/m - (k+k1)*x1/m
    velocity_2 = v2
    acceleration_2 = k*x1/m - (k+k1)*x2/m
    
    return velocity_1 , acceleration_1 , velocity_2 , acceleration_2

def sol_ode(k1,state0 , step_no , end_time , f):
    n = step_no 
    tf = end_time
    h = (tf-t0)/(n-1)
    tt = np.linspace(t0,tf,n)

    x_1 = np.zeros_like(tt)
    x_2 = np.zeros_like(tt)
    v_1 = np.zeros_like(tt)
    v_2 = np.zeros_like(tt)
    x_1[0] , x_2[0] , v_1[0] , v_2[0] = state0
    
    for i in range(n-1):
        velocity_1 , acceleration_1 , velocity_2 , acceleration_2 = f(m,k,k1,tt[i],x_1[i],v_1[i],x_2[i],v_2[i])

        v_1_temp = v_1[i] + h*acceleration_1
        v_2_temp = v_2[i] + h*acceleration_2
        x_1_temp = v_1[i] + h*velocity_1
        x_2_temp = v_2[i] + h*velocity_2

        velocity_1_next , acceleration_1_next , velocity_2_next , acceleration_2_next = f(m,k,k1,tt[i+1],x_1_temp,v_1_temp,x_2_temp,v_2_temp)

        v_1[i+1] = v_1[i] + h*0.5*(acceleration_1 + acceleration_1_next)
        v_2[i+1] = v_2[i] + h*0.5*(acceleration_2 + acceleration_2_next)
        x_1[i+1] = x_1[i] + h*0.5*(velocity_1 + velocity_1_next)
        x_2[i+1] = x_2[i] + h*0.5*(velocity_2 + velocity_2_next)

    return tt , x_1 , v_1 , x_2 , v_2

step_no = 1000
t0 = 0
end_time = 60
m = 1
k = 0.3
xx0_1 = np.array([1,1,1])
xx0_2 = np.array([0,-1,1])
vv0_1 = np.array([0,0,0])
vv0_2 = np.array([0,0,0])

for j in range(len(xx0_1)):
    fig, ax = plt.subplots(2, 1, figsize=(10, 8), constrained_layout=True)
    state0 = xx0_1[j], xx0_2[j], vv0_1[j], vv0_2[j]
    kk1 = np.arange(0,1, 0.2)
    line_styles = ['-', '--', '-.', ':','-']
    
    for idx,k1 in enumerate(kk1):
        alpha_value = 0.3 + k1 * 0.7  # Gradual increase in alpha for different shades
        line_style = line_styles[idx]
        tt, x_1, v_1, x_2, v_2 = sol_ode(k1, state0, step_no, end_time, f)
        
        ax[0].plot(tt, x_1, label=f'k1={k1:.1f}', color='black',linestyle = line_style, alpha = alpha_value)
        ax[1].plot(tt, x_2, label=f'k1={k1:.1f}', color='black',linestyle = line_style, alpha = alpha_value)

    # Add horizontal lines at x=0 and t=0
    ax[0].axhline(y=0, color='gray', linestyle='--')
    ax[0].axvline(x=0, color='gray', linestyle='--')
    ax[1].axhline(y=0, color='gray', linestyle='--')
    ax[1].axvline(x=0, color='gray', linestyle='--')

    # Set titles and grid
    ax[0].set_title(f'Position x_1 vs Time for x_1_0 = {xx0_1[j]}, x_2_0 = {xx0_2[j]}, v_1_0 = {vv0_1[j]}, v_2_0 = {vv0_2[j]}')
    ax[1].set_title(f'Position x_2 vs Time for x_1_0 = {xx0_1[j]}, x_2_0 = {xx0_2[j]}, v_1_0 = {vv0_1[j]}, v_2_0 = {vv0_2[j]}')
    ax[0].set_ylabel("$X_1$ $\\rightarrow$")
    ax[0].set_xlabel("Time $\\rightarrow$")
    ax[1].set_ylabel("$X_2$ $\\rightarrow$")
    ax[1].set_xlabel("Time $\\rightarrow$")
    ax[0].grid(True)
    ax[1].grid(True)

    # Add legends
    ax[0].legend()
    ax[1].legend()

plt.show()