#!/usr/bin/env python
# coding: utf-8

# IF ELSE
# 

# In[6]:


a=int(input("enter any number"))
b=int(input("enter 2nd number"))
if(a>b):
    print("a is greater number")
else:
    print("b is greater number")
    


# In[9]:


#if else
a=int(input("enter your age"))
if(a>18):
      print("eligible to vote")
        
else:
      print("not eligible to vote")
left=18-a
print(left,"years to left to vote")


# In[2]:


a=int(input("enter any number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if(a>b and a>c):
    print(a," is greater")

elif(b>a and b>c):
    print(b,"is greater")

else:
    print(c,"is greater")
    


# In[1]:


#nested if 
a=int(input("enter any number"))
if(a<=10):
    print("range between 0 to 10")
if(a>=10 and a<20):
    print("range is between 10 to 20")

if(a>=20 and a<30):
    print("range is btween 20 to 30") 

if(a>30):
    print("range is infinity")
    


# In[8]:


# nestedif else 
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter thye third number"))
if(num1>num2):
         if(num1>num3):
             print(num1,"is largest")
         else:
             print(num3," is largest number")
elif(num2>num3):
    print(num2,"largest number")
else:
    print("all number are equal")



    


# In[10]:


#while loop
i=0
while(i<=10):
    print(i)
    i=i+1


# In[6]:


# write a program to find year is lear year or not 
a=int(input("enter year"))
if(a%4==0):
    print(a,"is  a leap year")

else:
    print(a,"not a leap year")


# In[ ]:




