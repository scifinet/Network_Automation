#!/usr/bin/env python
#"""TODO: Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that
#are common between the lists (without duplicates). Make sure your program works on
#two lists of different sizes."""

import random

def compare():
    x = []
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(a)
    print(b)
    for i in a:
        if i in b:
            x.append(i)
    print(list(set(x)))

def comparerand():
    y = []
    c = random.sample(range(1,20),3)
    d = random.sample(range(1,20),6)
    print(c)
    print(d)
    for i in c:
        if i in d:
            y.append(i)
    if len(y) == 0:
        print("No duplicates found!")
    else:
        print(y)

compare()
comparerand()
