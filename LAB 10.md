```python

f1= open('pcu898991.txt', 'w')
for x in range(10):
    f1.write("pcu pune\n")
f1.close()

f1=open('pcu898991.txt', 'r')

content = f1.read()
for x in range(10):
    print(content)



# In[26]:


#write a program to create new file and add 10 lines of text in file by using "w" mode
f =open("pcu10991.txt","w")
f.write("hello \n")
f.write("world\n")
f.write("pcu\n")
f.write("maval\n")
f.write("pune\n")
f.write("maharashtra\n")
f.write("india\n")
f.write("asia\n")
f.write("sate\n")
f.write("vadgoan\n")
f.close()
f=open("pcu10991.txt","r")
content=f.read()
print(content)


# In[35]:


f1= open('pcu8989991.txt', 'x')
for x in range(10):
    f1.write("pcu pune\n")
f1.close()

f1=open('pcu8989991.txt', 'r')

content = f1.read()

print(content)
#write a program to generate and handle division by zero error by using try except block
def aby(a, b):
    try:
        c = (a + b) / (a - b)
    except ZeroDivisionError:  
        print("Division by zero occurred!")
    else:
        print("The result is:", c)

aby(1, 11)  
aby(4, 2)  







```

    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    
    hello 
    world
    pcu
    maval
    pune
    maharashtra
    india
    asia
    sate
    vadgoan
    
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    pcu pune
    
    The result is: -1.2
    The result is: 3.0
    


```python

```