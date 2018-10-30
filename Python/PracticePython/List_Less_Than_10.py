#!/usr/bin/env python
#"""TODO:Take a list, say for example this one:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less
#than 5."""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def less_10(list):
    x = []
    number= int(input("Please enter a number between 0 and 100: "))
    for i in list:
        if i <= number:
            x.append(i)
    print(x)

less_10(a)ASdz
