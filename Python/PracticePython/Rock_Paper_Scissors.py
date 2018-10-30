#!/usr/bin/env python
#"""TODO: Make a two-player Rock-Paper-Scissors game.)"""

options = ['rock', 'paper', 'scissors', 'nuke']

def RPS(pick_1, pick_2):
    if pick_1.lower() == pick_2.lower():
        print("Draw!")
    elif pick_1.lower() == "nuke":
        print("Player 2 was nuked! Get rekt, son! ")
    elif pick_2.lower() == "nuke":
        print("Player 1 was nuked! Nice try, scrub! ")
    else:
        while pick_1.lower() == "rock":
            if pick_2.lower() == "scissors":
                print("Player 1 crushes player 2!")
                break
            elif pick_2.lower() == "paper":
                print("Player 2 wins!")
                break
        while pick_1.lower() == "paper":
            if pick_2.lower() == "rock":
                print("Player 1 wins!")
                break
            elif pick_2.lower() == "scissors":
                print("Player 1 gets shredded")
                break
        while pick_1.lower() == "scissors":
            if pick_2.lower() == "paper":
                print("Player 1 shreds player 2!")
                break
            elif pick_2.lower() == "rock":
                print("Player 2 smashes player 1!")
                break

def validate(sel_1, sel_2):
    while sel_1.lower() not in options:
        print("{} is not a valid option, try again! ".format(sel_1))
        sel_1=input("Choose your option!\n-Rock\n-Paper\n-Scissors\n")
    while sel_2.lower() not in options:
        print("{} is not a valid option, try again! ".format(sel_2))
        sel_2=input("Choose your option!\n-Rock\n-Paper\n-Scissors\n")
    good_choices = RPS(sel_1, sel_2)
    return(good_choices)

def main():
    print("Let's play Rock-Paper-Scissors! ")
    selection_1=input("Choose your option!\n-Rock\n-Paper\n-Scissors\n\n")
    print('\n' * 100)
    selection_2=input("\n\nChoose your option!\n-Rock\n-Paper\n-Scissors\n\n")
    result = validate(selection_1, selection_2)
    return(result)

if __name__ == '__main__':
    main()
