#!/usr/bin/env python
#"""TODO: Ask the user for a string and print out whether this string is a
#palindrome or not. (A palindrome is a string that reads the same forwards and
#backwards.)"""

def palindrome_check():
    test_word=input("Can you think of a word that is a palindrome? ")
    if test_word == test_word[::-1]:
        print("Whoa,", '"' + test_word +'"', "is the same forwards and backwards! ")
    else:
        print(test_word, "is not a palindorme, try again! ")

palindrome_check()
