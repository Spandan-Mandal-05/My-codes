# Monte Carlo Integration
import numpy as np
import matplotlib.pyplot as plt 

def f(x): # def function
    #return np.sin(x)*np.sin(2*x)
    return np.sqrt(1-x**2)
    #return np.sin(x)

def monte_carlo(xi,xf,f):
    n = 10**7  # no of points
    # xi , xf = initial, final 

    # create random points along x & y
    xx_random = np.random.rand(n) * (xf-xi) + xi 

    yy = f(xx_random)
    yi = min(yy) if min(yy) < 0 else 0
    yf = max(yy)

    yy_random = np.random.rand(n) * (yf-yi) + yi
    inside_positive = ((yy >= 0) & (yy_random <= yy) & (yy_random >= 0))       
    inside_negative = ((yy < 0) & (yy_random > yy) & (yy_random < 0))
    inside = inside_positive | inside_negative
    outside = ~(inside)
    
    yy_in_posi = yy_random[inside_positive]
    yy_in_nega = yy_random[inside_negative]

    xx_out = xx_random[outside]
    yy_out = yy_random[outside]
    xx_in = xx_random[inside]
    yy_in = yy_random[inside]

    area = (yf-yi) * (xf-xi)
    integral = ((len(yy_in_posi) - len(yy_in_nega)) / n * area)
    return integral , xx_in , yy_in , xx_out , yy_out

integral_area , xx_in , yy_in , xx_out , yy_out = monte_carlo(-1,1,f)
print (2*integral_area)

plt.scatter(xx_in,yy_in,color = "black", s=5, alpha=1)
plt.scatter(xx_out,yy_out,color = "black", s=5, alpha=0.001)
plt.show()