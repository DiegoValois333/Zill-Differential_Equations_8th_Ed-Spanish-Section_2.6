# Zill 8th Ed (Spanish) - Section. 2.6
# Problem 5, pp 77.
# Euler's Method for Initial Value Problem
# y' = x*(y**2.0) - y/x,
# y(1) = 1, y(1.5)


import numpy as np 
import matplotlib.pyplot as plt

dx = 0.05
x0 = 0.0
y0 = 0.5
xf = 0.5
N = int((xf-x0)/dx)

x = np.zeros(N+2)
y = np.zeros(N+2)

x[0] = x0
y[0] = y0
    

def f(y):
    return y - y**2.0


def Euler(x0, y0, dx, N):
    print('\n--------SOLUTION--------')
    print('--------------------------')
    print('x0 \t y0 \t')
    print('--------------------------')
    
    for n in range(N+1):
        print('%.4f \t %.4f \t '% (x[n],y[n]))
        print('--------------------------')
        x[n+1] = x[n] + dx
        y[n+1] = y[n] + dx*f(y[n])    
    
# Call Function
Euler(x0, y0, dx, N)

# Graphic
plt.plot(x,y,'ro')
plt.show()

