#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    def __init__(self):
        pass
    
    def fib(self,N):
        a = 0
        b = 1
        for i in range(2, N+1):
            c = a+b
            a = b
            b = c
        return c

    def check(self,N,M):
        
        results=[]
        Nth = self.fib(N)
        a = 0
        b = 1
        c =0
        while c < Nth:
            if c % M == 0:
                results.append(c)

            c = a+b
            a = b
            b = c
        return results

N = eval(input("value for N: "))
M = eval(input("value for M: "))

blah = Fibonacci()
print(blah.fib(N))
print(blah.check(N,M))

