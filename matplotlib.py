#!/usr/bin/env python
# coding: utf-8

# In[45]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 
# 
# 

# In[47]:


x=[0,1,2,3,4]
y=[0,2,4,6,8]


#select color , fontsize , label and title 
plt.plot(x, y, "r.--", label= "2x")
plt.title('GRAPH' , fontdict={"fontsize":20})

#graph 2 
x2=np.arange(0,4.5,0.5)

#seprate a graph 
plt.plot(x2[:6] , x2[:6]**2 , "g" , label="x2")
#remainder of the same graph 
plt.plot(x2[5:] , x2[5:]**2 ,"g--")

plt.xlabel('x axis')
plt.ylabel("y axis")
#ticks of the graph 
plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8,10])


#legend
plt.legend()
plt.show()


#  bar charts

# In[48]:


lables =["A", "B", "C"]
values = [1,2,3]

plt.bar(values,lables)


# line graph
# 

# In[ ]:




