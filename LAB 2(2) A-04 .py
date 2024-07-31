#!/usr/bin/env python
# coding: utf-8

# In[2]:


print('DICTIONARY')
dict = {"item":"pen","price":"100"}
print(dict['item'])
print(dict['price'])
print(dict)


# HERON FORMULA

# In[11]:


a=float(input("enter the 1st side of triangle"))
b=float(input("enter the 2nd side of triangle"))
c=float(input("enter the 3rd side of triangle"))
print("a=",a)
print("b=",b)
print("c=",c)
s=(a+b+c)/2
print("s=",s)
area=((s*(s-a)*(s-b)*(s-c))**0.5)
print("area of triangle=",area)


# Write a program to calculate distance between two point using euclidean distance
# 

# In[15]:


x1=3
x2=5
y1=3
y2=6
distance=((((x2-x1)**2+(y2-y1)**2)**0.5))
print("distance=:",distance)


# AREA OF CIRCLE

# In[16]:


a=float(input("enter the radius "))
print("a=",a)
area=3.14*a*a
print("area of circle is=",area)


# DIGIT OF ONES PLACE

# In[19]:


num=int(input("enter a number "))
digit= num%10
print("digit of ones place=",digit)


# ASCII

# In[26]:


a=input('enter a character')
print("ASCII value is :",ord(a))


# TYPE CODE

# In[30]:


A=input("enter a")
b=int(A)
print(type(b))


# In[32]:


print("LIST")
List=['a','bc','bg','yhy','try']
List1=['34','345', '367','3456','435']
print(List1)
print(List[1:3])
print(List[2:3])
print(List[4:])
print (List*2)
print(List+List1)
print("length of list")
print(len(List))


# In[ ]:




