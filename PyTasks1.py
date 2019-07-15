#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2 
print((p * (p - a) * (p - b) * (p - c)) ** 0.5)


# In[7]:


a = int(input())
if -15 < a <= 12 or 14 < a < 17 or a >= 19: 
    print(True)
else:
    print(False)


# In[8]:


a = float(input())
b = float(input())
c = input()

if(c == "+"):
    print (a + b)
    
if(c == "-"):
    print (a - b)
    
if(c == "*"):
    print (a * b)
    
if(c == "/"):
    if (b == 0):
        print("Деление на 0!")
    else:
        print(a / b)
        
if(c == "mod"):
    if (b == 0):
        print("Деление на 0!")
    else:
        print(a % b)
        
if(c == "div"):
    if (b == 0):
        print("Деление на 0!")
    else:
        print(a // b)
        
if(c == "pow"):
    print (a ** b)


# In[15]:


str = input()
if (str == "треугольник"):
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2 
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)

if (str == "прямоугольник"):
    a = int(input())
    b = int(input())
    print(float(a * b))
    
if (str == "круг"):
    r = int(input())
    print(3.14 * r * r)
    print("Конец")
    


# In[31]:


a = int(input())
b = int(input())
c = int(input())

minimum = min(a, b, c)
maximum = max(a, b, c)

print(maximum)
print(minimum)

if a == minimum or a == maximum:
    if b == minimum or b == maximum:
        if c == minimum or c == maximum:
            if a == b:
                print(b)
            else:
                print(c)
        else: 
            print(c)
    else:
        print(b)
else: 
    print(a)


# In[49]:


a = int(input())

if (a % 10 == 1 and a % 100 != 11):
    print (a, "программист")
elif (a % 10 == 2 or a % 10 == 3 or a % 10 == 4) and (a % 100 != 12 and a % 100 != 13 and a % 100 != 14):
    print (a, "программиста")
else:
    print (a, "программистов")


# In[60]:


a = int(input())

if ((a // 100000) + (a // 10000 % 10) + (a // 1000 % 10) == (a // 100 % 10) + (a // 10 % 10) + (a % 10)):
    print("Счастливый")
else:
    print("Обычный")


# In[ ]:




