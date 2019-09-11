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

#a = [int(i) for i in input().split()]
#b = [0 for i in range(len(a))]
#c = 0
#if len(a) == 1:
#    print(a[0])
#else:
#    for i in a:
#        if c == 0:
#            b[c] = a[1] + a[len(a) - 1]
#       elif c == len(a) - 1:
#            b[c] = a[len(a)-2] + a[0]
#       else:
#           b[c] = a[c - 1] + a[c + 1]
#        c += 1
#    for i in b:
#        print(i, end=' ')

#a = [int(i) for i in input().split()]
#a.sort()
#a.append(0.1)
#for i in range(len(a)):
#    if a[i - 1] != a[i] and a[i - 2] == a[i - 1]:
#        print(a[i - 1], end=" ")


#if a[len(a) - 2] != a[len(a) - 1] and a[len(a) - 3] == a[len(a) - 2]:
#    print("Right")


#n, m, k = (int(i) for i in input().split())  # чтение размеров поля и числа мин
#a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
#for i in range(k):
#    row, col = (int(i) - 1 for i in input().split())
#    a[row][col] = -1  # расставляем мины
#for i in range(n):
#    for j in range(m):
#        if a[i][j] == 0:  # в этой клетке мины нет, поэтому считаем число мин вокруг
#            for di in range(-1, 2):
#               for dj in range(-1, 2):
#                    ai = i + di
#                    aj = j + dj
#                    # (ai, aj)
#                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                        a[i][j] += 1
# вывод результата
#for i in range(n):
#    for j in range(m):
#        if a[i][j] == -1:
#            print('*', end='')
#        elif a[i][j] == 0:
#            print('.', end='')
#        else:
#            print(a[i][j], end='')
#    print()

#i = 0
#a = []
#s = 0
#while True:
#    a.append(int(input()))
#    for c in a:
#       s += c
#    if s == 0:
#        break
#    s = 0
#
#for b in a:
#    s += b*b
#
#print(s)

#n = int(input())
#i = 1
#s = 0
#l = 0
#while True:
#        while s != i:
#            if l == n: break
#           l += 1
#            print(i, end=" ")
#            s += 1
#        if l == n: break
#        s = 0
#        i += 1

#a = [int(i) for i in input().split()]
#b = int(input())
#d = 0
#i = 0
#for c in a:
#    if (c == b):
#        d += 1
#        print(i, end=' ')
#    i += 1
#if d == 0:
#   print("Отсутствует")


