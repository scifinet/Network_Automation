#!/usr/bin/env python
#"""TODO: Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that
#are common between the lists (without duplicates). Make sure your program works on
#two lists of different sizes."""

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = random.sample(range(1,20),3)
d = random.sample(range(1,20),6)

def compare():
    x = []
    for i in a:
        if i in b:
            x.append(i)
    print(set(x))

def comparerand():
    y = []
    for i in c:
        if i in d:
            y.append(i)
            print(set(y))
        else:
            print("No duplicates found")


print(a)
print(b)
compare()

print(c)
print(d)
comparerand()
