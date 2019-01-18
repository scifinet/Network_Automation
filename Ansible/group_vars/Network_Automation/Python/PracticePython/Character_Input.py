#!/usr/bin/env python
#"""TODO:Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will
#turn 100 years old."""


def main():
    name = input("What is your name? ")
    age = input("How old are you? ")
    year = 2018 + int(100 - int(age))
    print(name + ", you will turn 100 in year", str(year) + "!")

if __name__ == '__main__':
    main()
