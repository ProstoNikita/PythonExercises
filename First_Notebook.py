#!/usr/bin/env python
# coding: utf-8

# In[7]:


a = int(input())
print(int(a / 60))
print(int(a % 60))


# In[8]:


X = int(input())
H = int(input())
M = int(input())
X += H * 60 + M
print (int(X / 60))
print (int(X % 60))


# In[2]:


a = True
b = False
a and b or not a and not b


# In[1]:


x = 5
y = 10
y > x * x or y >= 2 * x and x < y


# In[5]:


a = int(input())
b = int(input())
h = int(input())

if h < a:
    print('Недосып')
elif h > b:
    print('Пересып')
else: 
    print('Это нормально')


# In[7]:


a = int(input())
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('Високосный')
else:
    print('Обычный')


# In[9]:


"239" < "30" and 239 > 30


# In[10]:


"123" + "42"


# In[ ]:




