# This code can be used for ploting shape functions of linear element in 1D. 

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 11)

def basisf(x,i):
    
    n = len(x) - 1
    phi = np.zeros((n+1,1))
    
    if i == 0: 
        phi[0] = 1      
    elif i == n:
        phi[n] = 1
    else:
        for j in range(n):
            if i-1 < j <= i:
                phi[j] = (x[j] - x[i-1])/(x[i] - x[i-1])
            elif i < j < i+1:
                phi[j] = (x[j] - x[i])/(x[i+1] - x[i])
            else:
                phi[j] = 0
    return phi


for i in range(len(x)):
    plt.plot(x,basisf(x,i))

plt.xlabel('x')
plt.ylabel('$\phi_i (x)$')
plt.title('Linear shape functions in 1D')
plt.grid()
plt.show()
