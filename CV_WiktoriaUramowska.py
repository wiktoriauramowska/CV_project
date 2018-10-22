"""
Author: Wiktoria Uramowska
Date: 18/10/2018
Description: This program serves as my interactive CV version, which I hope can help me demonstrate to potential
employer my coding abilities, and help me distinguish myself from other students applying for the same position.
"""
import time, sys

# This function slows down the output of the program so that it seems more like someone was typin that in the
# real time.
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

# function responsible for displaying a menu, where user can choose which part of the CV to see first
# def print_menu():
#     print("\tWelcome to Python program which serves as a CV for Wiktoria Uramowska!")
#     print("Please choose one of the following menu options to get to know me and my skills better.")
#     print("\tI hope you like the idea, and it makes me stand out of the crowd :)")
#     print((20 * "-+")+"-", "MY CV MENU", (20 * "-+")+"-")
#     print("1. About me")
#     print("2. Career History")
#     print("3. Education and Courses")
#     print("4. Skills and Languages")
#     print("5. Contact details")
#     print("6. Exit")
#     print(67 * "-")

def cls():
    print((46 * "-+") + "-")
    print("\n" * 10)

def print_menu():
    print_slow("\n\n\tWelcome to Python program which serves as a CV for Wiktoria Uramowska!\n")
    print_slow("Please choose one of the following menu options to get to know me and my skills better.\n")
    print_slow("\t\t\t\t\t\tI hope you like the idea.\n")
    print((20 * "-+")+"-", "MY CV MENU", (20 * "-+")+"-")
    print_slow("1. About me\n")
    print_slow("2. Career History\n")
    print_slow("3. Education and Courses\n")
    print_slow("4. Skills and Languages\n")
    print_slow("5. Contact details\n")
    print_slow("6. Exit\n")
    print((46 * "-+")+"-")

# function that contains basic information about me
# it contains a validation, where user decides when to come back to the main menu
def about_me():
    print_slow("\nThis section is about me\n")
    print_slow("I am a second year undergraduate Computer Science student at Dublin Institute of Technology\n")
    next_section = input("Press y when you are ready to proceed ")
    if next_section == "y" or next_section == "Y":
        cls()
        pass
    else:
        while next_section != 'y' and next_section != 'Y':
            print("There is no option like this")
            next_section = input("Try again ")

# function that contains information about my career history
# it contains a validation, where user decides when to come back to the main menu
def career_history():
    print("This section is about my career history")
    next_section = input("Press y when you are ready to proceed ")
    if next_section == "y" or next_section == "Y":
        cls()
        pass
    else:
        while next_section != 'y' and next_section != 'Y':
            print("There is no option like this")
            next_section = input("Try again ")

# function that contains information about my education
# it contains a validation, where user decides when to come back to the main menu
def education():
    print("This section is about my education")
    next_section = input("Press y when you are ready to proceed ")
    if next_section == "y" or next_section == "Y":
        cls()
        pass
    else:
        while next_section != 'y' and next_section != 'Y':
            print("There is no option like this")
            next_section = input("Try again ")

# function that contains information about my skills
# it contains a validation, where user decides when to come back to the main menu
def skills_languages():
    print("This section is about my skills")
    next_section = input("Press y when you are ready to proceed ")
    if next_section == "y" or next_section == "Y":
        cls()
        pass
    else:
        while next_section != 'y' and next_section != 'Y':
            print("There is no option like this")
            next_section = input("Try again ")

# function that contains my contact details
# it contains a validation, where user decides when to come back to the main menu
def contact_details():
    print("This consists of my contact details")
    next_section = input("Press y when you are ready to proceed ")
    if next_section == "y" or next_section == "Y":
        cls()
        pass
    else:
        while next_section != 'y' and next_section != 'Y':
            print("There is no option like this")
            next_section = input("Try again ")


# function that allows the user to exit the program, after validation process,
# depends on what user thinks about the CV, different options will become available
# after going through both of the loops, the program will finish
# there is also an option to come back to the main menu to discover more of that amazing program
def exit_valid():
    print("This section is an exit validation part")
    next_section = input("Press y if you are sure you want to exit. ")
    if next_section == "y" or next_section == "Y":
        approval = input("Did you like this form of my CV? (y/n) ")
        if approval =='y' or approval == 'Y':
            print_slow("\nI'm glad to hear that."
                       "I have one more question then!\n")
            call_back = input("Are you going to call me for an interview? (y/n)")
            if call_back == 'y' or call_back == 'Y':
                print_slow("\nThat's great, I am excited already. See you soon!")
                loop = False
            elif call_back == 'n' or call_back == 'N':
                print_slow(":("
                           "Thank you anyway for taking time to look through my CV\n"
                           "Hopefully I will have more luck next time!\n"
                           "Have a nice day.")
                loop = False
            else:
                print_slow("I would take it as a no :(\n"
                           "Thank you anyway for taking time to look through my CV\n"
                           "Hopefully I will have more luck next time!\n"
                           "Have a nice day.")
                loop = False
        elif approval == 'n' or approval == 'N':
            print_slow(":("
                       "Thank you anyway for taking time to look through my CV\n"
                       "Hopefully I will have more luck next time!\n"
                       "Have a nice day.")
            loop = False
        else:
            print_slow("I would take it as a no :(\n"
                       "Thank you anyway for taking time to look through my CV\n"
                       "Hopefully I will have more luck next time!\n"
                       "Have a nice day.")
            loop = False
    else:
        cls()
        pass

def integer_valid(question):
    try:
        choice = int(input(question))
    except ValueError:
        print("Not an integer! Try again.")
    else:
        return choice

loop = True

# While loop which will keep going until loop = False
while loop:
    # calling the function that displays the menu
    print_menu()
    # user chooses one of the option, the input validation is included
    # if user enters incorrect input the program will ask the user to try again
    choice = integer_valid("\nEnter your choice using an integer between 1 and 6: ")

    # the program flow is controlled by the if/elif/else loop, and after entering the appropriate statement
    # a function responsible for specific function is called
    if choice == 1:
        print("Menu 1 has been selected")
        about_me()
    elif choice == 2:
        print("Menu 2 has been selected")
        career_history()
    elif choice == 3:
        print("Menu 3 has been selected")
        education()
    elif choice == 4:
        print("Menu 4 has been selected")
        skills_languages()
    elif choice == 5:
        print("Menu 5 has been selected")
        contact_details()
    elif choice == 6:
        print("Menu 6 has been selected")
        exit_valid()
        loop = False  # This will make the while loop to end as not value of loop is set to False
    else:
        # validation part - if user enters something different from the numbers required
        input("Wrong option selection. Enter any key to try again..")
