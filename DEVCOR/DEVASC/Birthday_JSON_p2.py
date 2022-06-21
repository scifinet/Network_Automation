#### Creat Dictionary of people's birthdays and write a program that asks a user who's birthday they would like to look up ###

### CREATE DICTIONARY ###
import json
import re

birthday_dict = {
    "Taylor":"04/15/1987",
    "Justin":"04/13/1990",
    "Ryan":"04/07/1990",
    "Nathan":"11/06/1991"
}

regex = r"(\d{2})/(\d{2})/(\d{4})"

def main():
    with open('git/Network_Automation/DEVCOR/DEVASC/bday.json', 'w') as file:
        load_data = json.dump(birthday_dict, file)
    with open('git/Network_Automation/DEVCOR/DEVASC/bday.json', 'r') as file:
        data = json.load(file)
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for name in data:
        print(name)
    bday = input("Who's birthday would you like to look up?\n")
    if bday not in birthday_dict.keys():
        print("We do not know their birthday")
        return ask()
    else:
        print(bday +"'s birthday is " + birthday_dict.get(bday))
        return ask()

def ask():
    answer = input("Would you like to add someone's birthday to the database?")
    if answer.lower() == "yes":
        added_name = input("Who would you like to add?")
        added_birthday = input("What is their birthday? Please use the format ##/##/####")
        birthday_dict[added_name] = added_birthday
        with open('git/Network_Automation/DEVCOR/DEVASC/bday.json', 'w') as file:
            load_data = json.dump(birthday_dict, file)
    else:
        print("Thanks for using birthday checker")
        # r = re.match(regex, added_birthday)
        # if r = None:
        #     print("Please use the format ##/##/####")
        # try:
        #     date = datetime.strptime(added_birthday, '%m/%d/%Y')
        # except ValueError:
        #     print("Invalid date entered!")


if __name__ == '__main__':
    main()
