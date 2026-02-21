#!/usr/bin/env python
# coding: utf-8

# In[3]:


Y = eval(input("Enter year of birth: "))
M = eval(input("Enter month of birth: "))
D = eval(input("Enter day of birth: "))

JD = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5 
print(JD)


# In[ ]:




