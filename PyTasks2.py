#!/usr/bin/env python
# coding: utf-8

#st1 = input() + "."
#i, a = 0, 1
#st2 = ""
#while i != (len(st1) - 1):
#    if st1[i] == st1[i+1]:
#        a += 1
#    else:
#        st2 += st1[i] + str(a)
#        a = 1
#    i += 1
#print(st2)

#for student in students:
#    print ("Hello, " + student + "!")

#students = ['Ivan', 'Masha', 'Sasha']
#students += ['Olga']
#students += 'Olga'
#print((students))

#students = ['Ivan', 'Masha', 'Sasha']
#students.remove('Sasha')
#del students[0]
#print(students)

#students = ['Sasha', 'Ivan', 'Masha']
#students = sorted(students)
#print(students)

#a = [1, 2, 3]
#b = a
#a = [5, 6]
#print(b)

#a = [int(i) for i in input().split()]
#b = 0
#for i in a:
#    b += i
#print(b)

a = [int(i) for i in input().split()]
b = [0 for i in range(len(a))]
c = 0
if len(a) == 1:
    print(a[0])
else:
    for i in a:
        if c == 0:
            b[c] = a[1] + a[len(a) - 1]
        elif c == len(a) - 1:
            b[c] = a[len(a)-2] + a[0]
       else:
           b[c] = a[c - 1] + a[c + 1]
        c += 1
    for i in b:
        print(i, end=' ')




