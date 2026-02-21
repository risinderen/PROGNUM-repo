#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math 
#f = ax**2 + bx + c
a = eval(input("enter a: "))
b = eval(input("enter b: "))
c = eval(input("enter c: "))

D = b**2-4*a*c
if (D) > 0:
    x1 = (-b+(b**2-4*a*c)**0.5)/2*a
    x2 = (-b-(b**2-4*a*c)**0.5)/2*a
    print(f"the equation has two real solutions: ")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")

elif (D) == 0:
    x = -b/2*a
    print(f"the equation has one solution: ")
    print(f"x = {x}")

else:
    print("the equation has no real solutions")

