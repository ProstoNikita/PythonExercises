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


# In[8]:


i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2
print(i)


# In[9]:


i = 0
p = 0
while i <= 10:
    p += 1
    i = i + 1
    if i > 7:
        i = i + 2
print(p)


# In[3]:


i = 1
str = "*"
while i <= 6:
    print(str)
    i += 1
    str += '*'
    


# In[5]:


p = 0
i = 0
while i < 5:
    print('*')
    p += 1
    if i % 2 == 0:
        print('**')
        p += 2
    if i > 2:
        print('***')
        p += 3
    i = i + 1
print(p)


# In[25]:


a = int(input())
b = int(input())
s = 0


if (a < b):
    while a <= b:
        s += a
        a += 1
    print(s)
else:
    print("Число а больше или равно числу b")


# In[ ]:


a = int(input())
s = 0

while a != 0:
    s += a
    a = int(input())
    
print(s)


# In[20]:


a = int(input())
b = int(input())
ex = 1

while (ex % a != 0) or (ex % b != 0):
    ex += 1

print(ex)


# In[21]:


a = 0
while True:
    a += 1
    if a == 5:
        break
print(a)


# In[23]:


i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        break
    i = i + 1
print(i, s)


# In[1]:


i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        continue
    i = i + 1
print(i, s)


# In[2]:


while True:
    i = int(input())
    if (i < 10):
        continue
    if (i > 100):
        break
    print(i)
    


# In[2]:


n = int(input())
for i in range(n):
    print('*' * n)


# In[34]:


a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

print ("\t", end='')
for i2 in range(a2, b2 + 1):
    if i2 != b2:
        print(i2, "\t", end="")
    else:
        print(i2)
    
for i1 in range(a1, b1 + 1):
    print (i1, "\t", end='')
    for i2 in range(a2, b2 + 1):
        if i2 != b2:
            print(i1*i2, "\t", end="")
        else:
            print(i1*i2)
    


# In[ ]:





# In[ ]:




