#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from matplotlib import pyplot as plt
import scipy as scp
    
A = eval(input("enter a value for A: "))
x0 = eval(input("enter a value for x0: "))
sigma = eval(input("enter a value for sigma: "))
z0 = eval(input("enter a value for z0: "))
intmin = eval(input("enter a value for the lower boundary of intergration: "))
intmax = eval(input("enter a value for the upper boundary of intergration: "))


x = np.linspace(-10, 10, 200)
def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0       #The function for the gaussian distribution
y = gauss(x,A,x0,sigma,z0)

#integration
quadint_value, quadint_error =  scp.integrate.quad(gauss, intmin, intmax, args=(A, x0, sigma, z0))
print(f"The area from {intmin} to {intmax} is: {quadint_value:.3}")

#plot
xfill = np.linspace(intmin, intmax,200)
yfill = gauss(xfill,A,x0,sigma,z0)
plt.fill_between(xfill,yfill, label=f"Area = {quadint_value:.3}")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Gaussian fuction chosen")


plt.plot(x, y, linestyle='-', color="pink", label="Gauss function")
plt.legend()
plt.show()

