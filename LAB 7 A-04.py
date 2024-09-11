#!/usr/bin/env python
# coding: utf-8

# In[1]:


#write a python code to check to check th version of numpy
import numpy as np
print(np.__version__)


# In[5]:


#WRITE PYTHON PROGRAM TO TEST IF ANY OF ELEMENT OF A GIVEN ARRAY ARE NON ZERO
import numpy as np
x=np.array([1,0,0,0])
print(np.array(x))
print(np.any(x))

x=np.array([0,0,0,0])
print(np.array(x))
print(np.any(x))


# In[7]:


#write python program to test a given array element wise for finiteness (not infinite or not number)
import numpy as np
x=np.array ([1,0,np.nan,np.inf])    #nan is not a number
print(x)                            #inf is infinite
print("test a give element wse for finitness:")
print(np.isfinite(x))


# In[10]:


#write a python program to test element wise positive or negative infinity
import numpy as mnp
x=mnp.array([1,0,-2,mnp.inf,-mnp.inf,3.4,6,7])
result_pos_inf=mnp.isposinf(x)
result_neg_inf=np.isneginf(x)
print(result_pos_inf)
print(result_neg_inf)


# In[13]:


# write a python to create an array of integers from 30 to 70
import numpy as pd
x=pd.arange(30,71)
print(x)


# In[15]:


#WRITE A PYTHON PROGRAM TO CREATE ARRAY OF ALL EVEN INTEGER FROM 30 TO 70
import numpy as pd
x= pd.arange(30,71,2)
print(x)


# In[16]:


# wirte a python code to create 3x3 identity 
import numpy as pd
arr_2d=pd.identity(3)
print(arr_2d)


# In[21]:


#write a python to create a 5x5 zero matrix with element on the main diagonal equal to 1,2,3,4,5
import numpy as pd
arr_2d=pd.diag([1,2,3,4,5,7,8,4,5,6,9,34,5,6,7,8])
print(arr_2d)


# In[29]:


#write a python to generate matrix product of 2 arrays
import numpy as np
x=[[1,0],[1,1]]
y=[[3,1],[2,2]]
print(np.dot(x,y))
#or
print(np.matmul(x,y))


# In[61]:


#Write a python program to generate  of matrix addition of 2 array 
import numpy as np
arr1=np.array([10,11,12,13,15,16,17])
arr2=np.array([23,24,252,62,267,5,7])
print("matrix addition")
newadd=np.add(arr1,arr2)
print(newadd)
print('matrix subtraction')
newsub=np.subtract(arr1,arr2)
print(newsub)


# In[45]:


#write to find mean of 1d array
import numpy as np
arr1=np.array([(10+20+30+40+50)])
me=np.mean(arr1)
print(me)


# In[59]:


#find mean of row
import numpy as np
x=np.array ([[10,30],[20,60]])
print('original array')
print(x)
print('mean of each column')
print(x.mean(axis=0))
print('mean of each row')
print(x.mean(axis=1))


# In[60]:


#to create 1D array in range 0 to9
import numpy as pd
x= pd.arange(0,10)
print(x)


# In[74]:


# to convert 1d to 2d with 2 rows
arr1=np.array([1,2,3,4,5,6,7,8])
y=arr1.reshape(2,4)
print(arr1)
print(y)


# In[ ]:




