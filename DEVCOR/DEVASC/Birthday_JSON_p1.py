#### Creat Dictionary of people's birthdays and write a program that asks a user who's birthday they would like to look up ###

### CREATE DICTIONARY ###
birthday_dict = {
    "Taylor":"04/15/1987",
    "Justin":"04/13/1990",
    "Ryan":"04/07/1990",
    "Nathan":"11/06/1991"
}

def main():
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for name in birthday_dict:
        print(name)
    bday = input("Who's birthday would you like to look up?\n")
    print(bday +"'s birthday is " + birthday_dict.get(bday))

if __name__ == '__main__':
    main()
