"""
Author: Wiktoria Uramowska
Date: 18/10/2018
Description: This program serves as my interactive CV version, which I hope can help me demonstrate to potential
employer my coding abilities, and help me distinguish myself from other students applying for the same position.
"""
import time, sys

# This function slows down the output of the program so that it seems more like someone was typing that in the
# real time.
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

# function that allows the display of the content be more appealing
# it introduces more spacing in between the new 'sections' being displayed
def cls():
    print((46 * "-+") + "-")
    print("\n" * 2)

# function responsible for displaying a menu, where user can choose which part of the CV to see first
def print_menu():
    print("\n\nWelcome to Python program which serves as a CV for Wiktoria Uramowska!")
    print("Please choose one of the following menu options to get to know me and my skills better.")
    print("I hope you like the idea.")
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
    print_slow("\n I am a second year undergraduate Computer Science student at Dublin Institute of Technology.\n "
               "While trying to balance work and college, I am using most of my free time on mastering my "
               "programming skills.\n As I am still new to the IT industry, I am looking for an internship in the area,\n"
               " that not only can give me an opportunity to put my programming and problem solving skills into real"
               " life tasks,\n but also can clarify the path that I would like to follow after graduating from college.\n "
               "I am a great team player and very outgoing person, that can work well under the pressure of time.\n"
               " This year I was elected a PR officer by my fellow colleagues in Computer Society.\n "
               "I am always looking for ways to practice my skills, not only in college work, but in various courses"
               " or competitions (for example: Hacker rank, Udacity).\n At the beginning of this year,"
               " together with my friends I took part in Google Hashcode (Coding Snowflakes).\n "
               "There is no better thing, than what you feel when your code works,"
               " and it does exactly what you want it to.\n\n")
    next_section = input("Press y when you are ready to proceed ")
    if next_section == "y" or next_section == "Y":
        cls()
        pass
    else:
        while next_section != 'y' and next_section != 'Y':
            print("\nThere is no option like this")
            next_section = input("Try again ")

# function that contains information about my career history
# it contains a validation, where user decides when to come back to the main menu
def career_history():
    print_slow("\nDespite my lack of professional experience within the industry, "
               "I decided to share my current position,\nwhich is Trainee Assistant Manager in Gourmet Burger Kitchen."
               "While I am not gaining any computer science related skills,\nthis job allows me to work with"
               "customers in day to day basis, what helps me develop my set of soft skills, \nsuch as Team Work, "
               "Verbal and Written Communication, Project Management or Leadership.\n "
               "These are some of my responsibilities:\n "
               "- Assisting in the day to day management of the restaurant, support the management team\n"
               " in operating the restaurant in a smooth and professional manner.\n"
               "- Maintain at all the times good customer relationships, and provide excellent customer service.\n"
               " Able to deal with customer complaints/issues following the company policy.\n"
               "- On a day to day basis, plan, organize and delegate the work of the FOH team in setting up \n"
               "the restaurant to the highest standard and to ensure that they are performing to their best abilities.\n"
               "- Helping to hit key performance indicators (KPIs) and achieving success for the restaurant.\n"
               "- Assisting the management team in developing team members and in providing training\n"
               "- Managing the daily administration records, to ensure that all of the paperwork is complete"
               " according to the company protocols\n"
               "- Preparing weekly rosters and ensuring that the staffing levels are correct on the daily basis.\n\n")
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
    print_slow("\nAs you could see already in the 'About me' section, I am currently pursuing BSc. (Hons.) degree "
               "in Computer Science at Dublin Institute of Technology, I expect to graduate in 2021.\n"
               "Some of the modules that I am learning are: Mathematics, Web Development, Program Design, "
               "Object Oriented Programming.\n\n")
    print_slow("At the beginning of this year I completed Web Development course, that was organized by "
               "Code First: Girls.\nIn that programme, the mentors were teaching how we can utilize Python in developing"
               " a web page.\n\n")
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
    print_slow("\nThose are some of my skills:\n"
               "- Python\n"
               "- C\n"
               "- HTML/CSS\n"
               "- Tableau\n"
               "- MySQL\n"
               "- Algorithm and Data Structures\n"
               "- Spoken language: Polish, English, Spanish \n"
               "- Team Work\n"
               "- Problem Solving\n"
               "- Verbal and Written Communication\n"
               "- Project Management\n"
               "- Attention to detail\n\n")
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

# function which aim is to avoid repetition of the same answer in the exit validation part
def exit_no():
    print_slow("\n:( "
               "Thank you anyway for taking time to look through my CV\n"
               "Hopefully I will have more luck next time!\n"
               "Have a nice day.")

# function which aim is to avoid repetition of the same answer in the exit validation part
def exit_wrong():
    print_slow("\nI would take it as a no :(\n"
               "Thank you anyway for taking time to look through my CV\n"
               "Hopefully I will have more luck next time!\n"
               "Have a nice day.")

# function that allows the user to exit the program, after validation process,
# depends on what user thinks about the CV, different options will become available
# after going through both of the loops, the program will finish
# there is also an option to come back to the main menu to discover more of that amazing program
def exit_valid():
    next_section = input("Press y if you are sure you want to exit. ")
    if next_section == "y" or next_section == "Y":
        approval = input("Did you like this form of my CV? (y/n) \n")
        if approval =='y' or approval == 'Y':
            print_slow("\nI'm glad to hear that."
                       "I have one more question then!\n")
            call_back = input("Are you going to call me for an interview? (y/n)\n")
            if call_back == 'y' or call_back == 'Y':
                print_slow("\nThat's great, I am excited already. See you soon!")
                loop = False # This will make the while loop to end as not value of loop is set to False
            elif call_back == 'n' or call_back == 'N':
                exit_no()
                loop = False # This will make the while loop to end as not value of loop is set to False
            else:
                exit_wrong()
                loop = False # This will make the while loop to end as not value of loop is set to False
        elif approval == 'n' or approval == 'N':
            exit_no()
            loop = False # This will make the while loop to end as not value of loop is set to False
        else:
            exit_wrong()
            loop = False # This will make the while loop to end as not value of loop is set to False
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
        loop = False # This will make the while loop to end as not value of loop is set to False
    else:
        # validation part - if user enters something different from the numbers required
        input("Wrong option selection. Enter any key to try again..")
