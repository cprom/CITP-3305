#!/usr/bin/env python3

# Initialize a variable to store name of assistant (task 1)
assitant_name = "Joshua"
# Use print() statement to dislaay a greeting and assistant's name
# Use f-strings to print variables containing assistant name
print(f"Hello, my name is {assitant_name}, your personal assistant.")

# Initialize a variable to store information for assistant to say (task 2)
assistant_info_01 = "The Software (or System) Development Life Cycle (SDLC) is a systematic approach that breaks the software process into phases--planning, analysis, design, implementation and maintenance."
# Use print() to display string stored in assitan_info_01
print(assistant_info_01)

# Initialize a variable to store information for assistant to say (task 3)
assistant_info_02 = "In the Analysis process, tools (data flow diagrams, data dictionary, decision trees, decision tables, structured English, pseudocode) are used to understand the system and its activities in a logical way."
# create empty line
print(f"\n")
print(assistant_info_02)

# Use print() to display message (task 4)
print("Well, that is enough about SDLC! I am so happy you have come back!! I just realized it has been all about me. Let's talk about you now.")
def script(): # Declare a function
    # Initialize a variable to store user's name (task 5)
    # use input() to get the value for user_name variable
    user_name = input("Please enter your name? ")

    # Initialize a list to store store user's favorite songs (task 6)
    user_favorite_songs = []
    # Use input() to get user's favorite songs
    # Use append() method to add user's input into list
    prompt = "Please enter your favorite song name and press enter. Enter 'quit' when done. "
    polling_active = True
    while polling_active: # Use while loop to let user enter inputs until a condition is met.
        song = input(prompt)
        if song != 'quit': # Use if statement to check if the user input is 'quit', if it is use 'break' to stop program.
            user_favorite_songs.append(song)
        else:
            break

    # Display a response to list of songs (task 7)
    # Use if statements to display different messages based on the length of the list
    # Use lent() to get length of user_favorite_songs list and modulus operator (%) to determine if length is even or odd number.
    if len(user_favorite_songs) % 2 == 0:
        print(f"Nice {user_name} you have great taste in music.  Keep being you.")
    else:
        print(f"Wow those song choices are terrible.  I'm pretty sure you're tone deaf, {user_name}.  You might want to get your hearing checked.")

    # Initialize empty list to store user's favorite 5 things to do. (task 8)
    # Initialize counter variable and set to 0, increment counter by 1 everytime user enters a new thing to do.
    # Once counter = 5 prompts stops
    counter = 0
    user_favorite_todo = []
    while counter < 5:
        for x in range(1,6): # use range() to loop from 1 - 5 and use value x in prompt string
            if x == 1:  # conditional statement to only print the initial prompt once
                todo_prompt = f"Let's get to know you better {user_name}.  Please tell me your 5 favorite things to do. "
                todo_prompt += f"\nFavorite things #{x} : "
            else:
                todo_prompt = ""
                todo_prompt += f"Favorite things #{x} : "
            todo = input(todo_prompt)
            user_favorite_todo.append(todo)
            counter += 1

        # Use print() to display a goodbye message and display top 2 songs and activities (task 9)
        print(f"Well it was great getting to know you better, {user_name}.")  
        print(f"Now I know your top favorite songs are.")
        top_song = user_favorite_songs[0:2] # get first 2 value from user_favorite_songs and place into a variable
        for song in top_song:   # Use for loop to print out song value
            print(song)
        print(f"I also know that your top favorite activities includes.")
        top_todo = user_favorite_todo[0:2] # get first 2 value from user_favorite_todo and place into a variable
        for todo in top_todo:   # Use for loop to print out todo value
            print(todo)
    # Create a new prompt that asked the user if there they would like to have someone else add there favorite song and activities (task 10)
    # If they type 'yes' the function will rerun, it user types 'no' or any other string/character the program will say its final goodbye and end the program.
    repeat = str(input("Is there someone else that would like to share their favorite songs and activities? Please Enter 'yes' to continue or 'no' to exit: "))
    if repeat == 'yes':
        script()
    elif repeat == 'no': 
        print(f"Thanks for the great info {user_name}.  Goodbye!!")

script() # Calling the function
