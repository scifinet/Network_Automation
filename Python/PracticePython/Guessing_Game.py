#!/usr/bin/env python
#"""TODO: Generate a random number between 1 and 9 (including 1 and 9). Ask the
#user to guess the number, then tell them whether they guessed too low, too
#high, or exactly right."""

import random

rand_num = random.randint(1, 9)
tries = 0

def compare(user, random):
    count = 0
    while user != random:
        count += 1
        if user != random:
            print("Nice Try, please try again")
            print(count)
            new = guess()
        else:
            print("Correct, after,",len(z),"attempts.")
    #if user != random:
            #print("Nice Try, please try again")
            #wrong = guess()
            #return wrong
    #elif tries == 1:
        #print("Wow, first try, impressive! ")
    #elif tries in range(2,6):
        #print(tries,"attempts....pretty good, but I've seen better... ")
    #else:
        #print("Wow.....",tries,"attempts, that took a while... ")

def validate(selection):
    if selection not in range(1,10):
        new_num=input("Please pick a whole number between 1 and 9. ")
        if new_num.lower() == "exit":
            print("Thanks for playing! ")
            return exit(1)
        else:
            new_num = int(new_num)
        check = compare(new_num, rand_num)
    else:
        check = compare(selection, rand_num)
    return check

def guess():
    usr_num=input("What number would you like? ")
    if usr_num.lower() == "exit":
        print("Thanks for playing! ")
        return exit(1)
    else:
        usr_num = int(usr_num)
    result = validate(usr_num)
    return result

def main():
    print("\n\nWelcome to The Guessing Game!\n\nBet you can't guess the number I'm thinking off! Hint: 1-9")
    print(rand_num)
    play = guess()
    return play

if __name__ == '__main__':
    main()
