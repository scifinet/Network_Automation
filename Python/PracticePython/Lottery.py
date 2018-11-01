#!/usr/bin/env python
#"""TODO: Make a game that simulates the lottery. Allow the user to pick 5
# numbers between 1 and 70 and 1 Mega Ball number betwen 1 and 25. Allow the
# user to randomize the selection if desired. See if these numbers match 6
# randomly generated numbers with the same stipulations. Set winning prizes
# based on the Mega Millions prize chart."""


 player_set = []
 winning_set = []
 open_game = inputs("\nWould you like to play the lottery?\n ")

def inputs():
    game_options = ['yes', 'no', 'exit']
    while True:
        open_game=str(input("\nWould you like to play the lottery?\n "))
        if open_game.lower() not in game_options:
            print("\n\nPlease type 'yes', 'no', or 'exit'. ")
            continue
        else:
            break
    if open_game.lower() in ['no', 'exit']:
        print("\n\nCome back to play the lottery anytime! \n")
    elif open_game.lower() == 'yes':
        print("Lets play! \n")
    style_options = ['choose', 'random']
    while True:
        style=str(input("Would you like to choose your numbers or randomly generate them? (choose/random) \n"))
        if style.lower() not in style_options:
            print("Please type 'choose', or 'random'. \n")
            continue
        else:
            break
    if style.lower() == 'choose':
        while True:
            num1, num2, num3, num4, num5 = [int(x) for x in input("Please pick 5 numbers between 1-70. \n").split()]
            number_choices = [num1, num2, num3, num4, num5]
            if len(set(number_choices)) != len(number_choices):
                print("\nPlease ensure all 5 numbers are unique. ")
                continue
            for i in number_choices:
                if i in range(1,71):
                    continue
                continue
            else:
                break






 def main():
     print("\nWelcome to the Mega Millions game!")
     inputs()
