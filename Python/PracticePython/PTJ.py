import random
import time

player_set = []
player_mega_ball = []
winning_set = []
numbers_matched = []

def inputs(style):
    style_options = ['choose', 'random', 'r', 'exit', 'ptj']
    while True:
        try:
            style=str(input("Would you like to choose your numbers or randomly generate them? (choose/random) \n"))
        except ValueError:
            print("\nExiting game. If exit was not desired, try again and select 'choose' or 'random'. ")
            return exit()
            break
        if style.lower() not in style_options:
            print("Please type 'choose', or 'random'. \n")
            continue
        else:
            break
    if style.lower() == 'ptj':
        return ptj('nums', 'mega')
    if style.lower() == 'exit':
        return exit()
    if style.lower() == 'choose':
        while True:
            try:
                num1, num2, num3, num4, num5=[int(x) for x in input("Please pick 5 numbers between 1-70. \n").split()]
                number_choices = num1, num2, num3, num4, num5
            except ValueError:
                print("\n\nExiting game. If exit was not desired, try again and pick exactly 5 numbers. ")
                return exit()
                break
            if 'exit' in number_choices:
                return exit()
                break
            if len(number_choices) != 5:
                print("Please pick only 5 numbers. \n")
                continue
            if len(set(number_choices)) != len(number_choices):
                print("\n\nPlease ensure all 5 numbers are unique. \n")
                continue
            elif int(min(number_choices)) < 1:
                print("\n\nPlease ensure all 5 numbers between 1 and 70. \n")
                continue
            elif int(max(number_choices)) > 70:
                print("Please ensure all 5 numbers between 1 and 70. \n")
                continue
            else:
                break
        while True:
            try:
                mega_ball=int(input("Choose your MEGA Ball! Must be 1-25. \n"))
            except ValueError:
                print("\n\nExiting game. If exit was not desired, try again and pick 1 MEGA Ball between 1 and 25. ")
                return exit()
                break
            if mega_ball < 1:
                print("\n\nPlease ensure MEGA Ball is between 1 and 25. \n")
                continue
            elif mega_ball > 25:
                print("\n\nPlease ensure MEGA Ball is between 1 and 25. \n")
                continue
            else:
                break
        player_set = number_choices
        player_mega_ball.append(mega_ball)
        return game_logic(player_set, player_mega_ball )
    if style.lower() == 'random':
        random_choices=random.sample(range(1,71),5)
        random_mega_ball=random.randint(1,25)
        return game_logic(random_choices, random_mega_ball)
    if style.lower() == 'r':
        random_choices=random.sample(range(1,71),5)
        random_mega_ball=random.randint(1,25)
        return game_logic(random_choices, random_mega_ball)

def ptj(nums, mega):
    start = time.time()
    while True:
        random_choices=random.sample(range(1,71),5)
        random_mega_ball=random.sample(range(1,26),1)
        print("Your numbers:", random_choices)
        print("Your MEGA Ball:", random_mega_ball)
        winning_set=random.sample(range(1,71),5)
        print("Winning numbers:", winning_set)
        winning_mega_ball=random.sample(range(1,26),1)
        print("Winning MEGA Ball", winning_mega_ball)
        for i in random_choices:
             if i in winning_set:
                 numbers_matched.append(i)
        print("You matched:", numbers_matched)
        if len(numbers_matched) != 5:
            numbers_matched.clear()
            random_choices.clear()
            random_mega_ball.clear()
            winning_set.clear()
            winning_mega_ball.clear()
            continue
        elif random_mega_ball != winning_mega_ball:
            numbers_matched.clear()
            player_set.clear()
            player_mega_ball.clear()
            winning_set.clear()
            random_choices.clear()
            continue
        else:
            break
    if random_mega_ball == winning_mega_ball:
        end = time.time()
        print("\nYou matched", len(numbers_matched), "numbers and the MEGA Ball!")
        if len(numbers_matched) == 0:
            print("That is not a winner, better luck next time! ")
        elif len(numbers_matched) == 1:
            print("\n\nYou won $4. Odds--1:89", "\nApproximately", 89/(end-start), "iterations per second", "\nIt took", (end-start), "seconds.")
        elif len(numbers_matched) == 2:
            print("\n\nYou won $10. Odds--1:693", "\nApproximately", 693/(end-start), "iterations per second", "\nIt took", (end-start), "seconds.")
        elif len(numbers_matched) == 3:
            print("\n\nYou won $200. Odds--1:14,547", "\nApproximately", 14457/(end-start), "iterations per second", "\nIt took", (end-start), "seconds.")
        elif len(numbers_matched) == 4:
            print("\n\nYou won $10,000. Odds--1:931,001", "\nApproximately", 931001/(end-start), "iterations per second", "\nIt took", (end-start), "seconds.")
        elif len(numbers_matched) == 5:
            print("JACKPOT!!!"*500)
            print("\n\nYou won $1,000,000,000!!! Odds--1:302,575,350", "\nApproximately", 302575350/(end-start), "iterations per second", (end-start), "seconds.")
    return play_again()

def game_logic(nums, mega):
    print("Your numbers:", nums)
    print("Your MEGA Ball:", mega)
    winning_set=random.sample(range(1,71),5)
    print("Winning numbers:", winning_set)
    winning_mega_ball=random.randint(1,25)
    print("Winning MEGA Ball", winning_mega_ball)
    for i in nums:
        if i in winning_set:
            numbers_matched.append(i)
    print("You matched:", numbers_matched)
    # while True:
    #   if len(numbers_matched) != 5:
    #     numbers_matched.clear()
    #     player_set.clear()
    #     player_mega_ball.clear()
    #     winning_set.clear()
    #     random_choices=random.sample(range(1,71),5)
    #     random_mega_ball=random.randint(1,25)
    #     return game_logic(random_choices, random_mega_ball)
    #     break
    #   elif mega != winning_mega_ball:
    #     numbers_matched.clear()
    #     player_set.clear()
    #     player_mega_ball.clear()
    #     winning_set.clear()
    #     random_choices=random.sample(range(1,71),5)
    #     random_mega_ball=random.randint(1,25)
    #     return game_logic(random_choices, random_mega_ball)
    #     break
    #   else:
    #     break
    if mega == winning_mega_ball:
        print("\nYou matched", len(numbers_matched), "numbers and the MEGA Ball!")
        if len(numbers_matched) == 0:
            print("That is not a winner, better luck next time! ")
        elif len(numbers_matched) == 1:
            print("\n\nYou won $4. Odds--1:89")
        elif len(numbers_matched) == 2:
            print("\n\nYou won $10. Odds--1:693")
        elif len(numbers_matched) == 3:
            print("\n\nYou won $200. Odds--1:14,547")
        elif len(numbers_matched) == 4:
            print("\n\nYou won $10,000. Odds--1:931,001")
        elif len(numbers_matched) == 5:
            print("JACKPOT!!!"*15)
            print("\n\nYou won $1,000,000,000!!! Odds--1:302,575,350")
    elif mega != winning_mega_ball:
        print("\n\nYou matched", len(numbers_matched), "numbers.")
        if len(numbers_matched) <= 2:
            print("\n\nBetter luck next time!")
        elif len(numbers_matched) == 3:
            print("\n\nYou won $10. Odds--1:606")
        elif len(numbers_matched) == 4:
            print("\n\nYou won $500. Odds--1:38,792")
        elif len(numbers_matched) == 4:
            print("\n\nYou won $1,000,000! Odds--1:12,607,306\n\nSo close to the Jackpot!")
    return play_again()

def play_again():
    game_options = ['yes', 'y', 'no', 'exit']
    while True:
        open_game=str(input("\nWould you like to play again? \n "))
        if open_game.lower() not in game_options:
            print("\n\nPlease type 'yes', 'no', or 'exit'. ")
            continue
        else:
            break
    if open_game.lower() in ['no', 'exit']:
        return exit()
    elif open_game.lower() == 'yes':
        print("Lets play! (Type 'exit' anytime to leave game. )\n")
        numbers_matched.clear()
        return inputs('style')
    elif open_game.lower() == 'y':
        print("Lets play! (Type 'exit' anytime to leave game. )\n")
        numbers_matched.clear()
        player_set.clear()
        player_mega_ball.clear()
        winning_set.clear()
        return inputs('style')

def exit():
    print("\n\nCome back to play the lottery anytime! \n")

def main():
    print("\nWelcome to the Mega Millions game!")
    game_options = ['yes', 'y', 'no', 'exit']
    while True:
        open_game=str(input("\nWould you like to play the lottery?\n "))
        if open_game.lower() not in game_options:
            print("\n\nPlease type 'yes', 'no', or 'exit'. ")
            continue
        else:
            break
    if open_game.lower() in ['no', 'exit']:
        return exit()
    elif open_game.lower() == 'yes':
        print("\n\nLets play! (Type 'exit' anytime to leave game. )\n")
        return inputs('yes')
    elif open_game.lower() == 'y':
        print("\n\nLets play! (Type 'exit' anytime to leave game. )\n")
        return inputs('yes')

if __name__ == '__main__':
    main()
