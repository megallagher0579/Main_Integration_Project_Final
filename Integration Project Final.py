__author__ = "Megan Gallagher"
"""Integration Project: COP 1500"""
"""This is a collection and demonstration of all I have learned in Intro to
Computer Science.
The program will be an interactive (and hopefully entertaining) narrative
of an alien communicating through a device (the shell) to collect data of
the person who "found" this device from his planet."""

# Introductions and initial confirmation to continue:


def main():
    species = input("Greetings, space-being! What do you call your species? ")
    print("Ah, our first " + species + ", yet!")
    print("Let me introduce myself. I am Plurgy from Planet 626.")
    name = input('What might be your birth name? ')
    print("It is very exceptional to meet your acquaintance, " + name + "!")
    print("I must apologize if any of my speech sounds awkward to you.")
    print("My pod translator has never encountered your language before, ")
    print("and could be damaged from travel.")

    print("Say, would you care to help me with something?")

    initial_confirmation = True
    while initial_confirmation:
        print("Please enter the number correlating to your answer: ")
        print("1. Sure! ")
        print("2. Sure, but I am unsure of how sure I am.")
        print("3. Maybe another time.")
        print("Or enter any other integer to force quit.")
        choice_initial = int(input())
        if choice_initial == 1:
            print("Thanks, " + name + "!")
            break
        elif choice_initial == 2:
            print("I'm glad you're along for the ride!")
            break
        elif choice_initial == 3:
            print("I promise it will be done in a jiffy!")
            break
        else:
            print("Terminating program and communication.")
            initial_confirmation = False
            exit()


main()
# Explanation:
print(" You may be wondering what is going on. Allow me to explain.")
print(" You must have stumbled upon one of my planet's surveyor pods.")
print(" We launch them periodically in locations where we suppose life may"
      " be.")
print(" Planet 626 is the galaxy's leader in collection and cataloging of +"
      "planets and their inhabitants.")

# Confirmation to survey:
nick_name = str(input("If you have a nickname, or a preference of what to be"
                      "called, please enter it: "))
continue_response = input("Is it alright if I collect some data from you, "
                          + nick_name + "?" +
                          " Please enter yes or no: ")
if continue_response == "yes":
    print("Great! Let's get started.")
elif continue_response == "no":
    print("I thought we were going to be great friends... guess I was wrong.")
    print("Terminating program and communication.")
    exit()
else:
    print("Invalid input. Next time, please enter yes or no.")
    print("Auto-continuing program.")


# Beginning of survey questions:
age = int(input("How many orbits have you completed around your sun? "))
print("Oh, how adorable. >,< You would be", age / 5, "orbits on my planet.")
print("I am", age * 10, "orbits old!")
print("Which is still considered young on my planet, as the average life "
      "expectancy is", age * 20, "orbits.")

"""The purpose of this function (screen_area) is to estimate the user's screen 
area based on an input of width and height. It assumes the screen shape is a 
rectangle and uses the area formula for rectangles: width times height."""


def screen_area(a, b):
    return print(a * b)


width = int(input("Enter the approximate width, in inches, of this device's "
                  "monitor: "))
height = int(input("Now enter the approximate height: "))

screen_area(a=width, b=height)
print("inches is the approximate area of the screen. Formatting will now be "
      "optimized accordingly.")

job = input("What is your day to day occupancy? Or, your 'job' as I believe "
            "your species call it. ")
if job == "student":
    print("Very neat, I am also considered a student on my planet! I study "
          "how species communicate with each other.")
else:
    print("I see, a very important occupancy I can only assume. You seem like"
          " a fairly advanced individual.")

print("If you have not pursued higher education, please enter 0.")
print("However, if you have attended a university, how many orbits did you "
      "attend for, ")
college_year = int(input("or what number are you on currently? "))
if college_year >= 1:
    print("It takes the average student on Planet 626 a total of ",
          college_year - 1, "to", college_year + 4, " orbits to complete "
                                                    "their education.")

siblings_input = int(input("Please enter the number of siblings you have: "))
print("Very interesting! Let's see, I have")
for siblings_input in range(1, 10):
    if siblings_input % 5 == 0:
        break
    print(siblings_input)
print("siblings.")

hair_color = True
while hair_color:
    print("What color hair do you have?")
    print("Please enter the number correlating to your answer: ")
    print("1. Blond ")
    print("2. Brown")
    print("3. Black")
    print("4. Red/Orange")
    print("5. Grey/White")
    print("6. Other")
    hair_color_input = int(input())
    if hair_color_input == 1:
        print("Neat, I do as well.")
        break
    elif hair_color_input == 2:
        print("My maternal figure has brown hair, too!")
        break
    elif hair_color_input == 3:
        print("My paternal figure has black hair, too!")
        break
    elif hair_color_input == 4:
        print("My younger sibling has red/orange hair, too!")
        break
    elif hair_color_input == 5:
        print("I had white hair in my adolescence. ")
        break
    else:
        print("How interesting! I will make sure this is recorded. ")
        hair_color = False

# Final message and terminating program:
print("Well, I think those are all the questions I will pester you"
      " with for today.")
print("Thanks a bunch for your participation!")
print("Have a nice day ", nick_name, " !")

exit()
