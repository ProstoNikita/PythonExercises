#!/usr/bin/env python
# coding: utf-8

a = st1 = input()
i, a = 0, 1
while i != (len(st1) - 1):
    if st1[i] == st1[i+1]:
        a += 1
    if st1[i] != st1[i+1]:
        st2 = st1[i] + str(a)
    i += 1
print(st2)
