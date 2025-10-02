import numpy as np
import matplotlib.pyplot as plt 

def f(x): # def function
    return np.sin(x)*np.sin(x)

n = 10**5  # no of points
xi , xf = -np.pi, np.pi # initial, final points

# create random points along x & y
xx_random = np.random.rand(n) * (xf-xi) + xi 

yy = f(xx_random)
yi = min(yy) if min(yy) < 0 else 0
yf = max(yy)

yy_random = np.random.rand(n) * (yf-yi) + yi



#print(np.round(xx_random,2))
#print(np.round(yy_random,2))
#print(np.round(xx_rand_sort,2))
#print(np.round(yy_rand_sort,2))
"""
xx_out , yy_out , xx_in , yy_in = [],[],[],[]
for i in range (n):
    if yy[i] >= 0:
        if yy_rand_sort[i] <= yy[i] and yy_rand_sort[i] >= 0 :
            xx_in.append(xx_rand_sort[i]) , yy_in.append(yy_rand_sort[i])    
        else:
            xx_out.append(xx_rand_sort[i]) , yy_out.append(yy_rand_sort[i])
    elif yy[i] < 0:
        if yy_rand_sort[i] >= yy[i] and yy_rand_sort[i] <= 0 :
            xx_in.append(xx_rand_sort[i]) , yy_in.append(yy_rand_sort[i])    
        else:
            xx_out.append(xx_rand_sort[i]) , yy_out.append(yy_rand_sort[i])      """

inside_mask = ((yy >= 0) & (yy_random <= yy) & (yy_random >= 0)) | \
              ((yy < 0) & (yy_random > yy) & (yy_random < 0))
xx_in = xx_random[inside_mask]
yy_in = yy_random[inside_mask]
xx_out = xx_random[~inside_mask]
yy_out = yy_random[~inside_mask]

area = (yf-yi) * (xf-xi)
print(len(yy_in) / n * area)

plt.scatter(xx_in,yy_in,color = "black", s=5, alpha=1)
plt.scatter(xx_out,yy_out,color = "black", s=5, alpha=0.05)
plt.show()
