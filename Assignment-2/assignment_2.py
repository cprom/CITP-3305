#!/usr/bin/env python3

# Initialize variable to store user's name
user = "Chen"

# Initialize variables to store assistant's name task(1)
variableNameOfYourChoice = "Kaylibell"
# Use print function to display introduction of the assistant to the screen
print("Hello {}, this is {}, your digital assistant.  Welcome back.".format(user, variableNameOfYourChoice))

# Initialize variables to store assistant's response task(2)
singleVariable = "The Software (or System) Development Life Cycle (SDLC) is a systematic approach that breaks the software process into phases--planning, analysis, design, implementation and maintenance."
# Use print function to display response about Systems Analysis and Design stored in a variable
print(singleVariable)

# Add new line this will print out a black line task(3)
print("\n")
# Initialize variable
diffrentVariable = "Planning requires knowing what is needed for the computer system. This planning can be done in different ways such as interviewing users, using questionnaires, observing (people, events, and object), software (Joint Application Development), and feasibility studies."
# Print diffrentVariable to screen
print(diffrentVariable)

# Print out message without variable Task(4)
print("Well, that is enough about SDLC! Let's talk more about me! I am so happy you have come back!!")

# Create an empty list to hold favorite songs Task (5)
favorite_songs = []
# Append 5 songs to the list
favorite_songs.append("Hotel California")
favorite_songs.append("Free Bird")
favorite_songs.append("Wish You Were Here")
favorite_songs.append("Bohemian Rhapsody")
favorite_songs.append("My Heart Will Go On")
# Print out a message that list out the list
print("It's great to hear from you again.  Did you know that my favorite songs are: {}. Ooops, I think I'm having second thoughts about that last song.".format(favorite_songs))

# Delete the last song using the pop method Task(6)
favorite_songs.pop()
# Print out message with new list
print("That was a joke, here is my real list:")
for item in favorite_songs:
    print(item)

# Create an empty list to store favorite things to do Task(7)
favorite_things_to_do =  []
favorite_things_to_do.append("Filing yearly taxes.")
favorite_things_to_do.append("Jury duty.")
favorite_things_to_do.append("People watching at the airport.")
favorite_things_to_do.append("Finding bugs in my Code.")
favorite_things_to_do.append("Taking long walks on the beach.")
# Print out favorite_things_to_do list to screen
print("My most favorite things to do are the following:")
for item in favorite_things_to_do:
    print(item)

# Create If statements to determine what personality type based on task list Task(8)
# Use for loop to loop through favorite_things_to_do list and use if statements to print out different personality statements.
for task in favorite_things_to_do:
    if task == "Filing yearly taxes.":
        print("I am eccentric.")
    if task == "Jury duty.":
        print("I am patriotic.")
    if task == "People watching at the airport.":
        print("I am observant.")
    if task == "Finding bugs in my Code.":
        print("I am insane.")
    if task == "Taking long walks on the beach.":
        print("I am sensitive.")

# Make program say it final goodbye Task(9)
print("Thanks again for stopping by to speak with me.  My top 3 favorite songs are: ")
print(favorite_songs[:3])
print("and my top 3 things to do are the following: ")
print(favorite_things_to_do[:3])
print("I hope you come back soon {}, {} is at your service.  Goodbye".format(user, variableNameOfYourChoice))