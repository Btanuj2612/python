#!/usr/bin/env python
# coding: utf-8

# DICTIONARY

# In[31]:


dict={"1": "icecream", '2': '100', '3':'vanilla'}
print(dict['1'])
dict2={1: "hii","name":"tanuj",1.5:("yes","very much"),9:[3,6,9,5]}
print(dict2)
print(dict2[1.5])
dict2['name']='kartik'
print(dict2)
dict2['5']='pune'
print(dict2)
dict2['6']='mumbai'
print(dict2['name'])
dict3=dict2.copy()
print(dict3)
keys=dict2.keys()
print(keys)
seq=('python','cpp')
dict4=(dict3.fromkeys(seq,100))
print(dict4)
dict5={1:'python',2:'php',3:'javascript'}
dict6={4:'cpp',5:'c'}
dict5.update(dict6)
print(dict5)
dict7={1:1,2:4,3:9,4:5,5:25}
print(1 in dict7)
print(2 not in dict7)





# In[ ]:





# In[ ]:




