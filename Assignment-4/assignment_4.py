#!/usr/bin/env python3
import math
from trick_functions import convert_to_fahrenheit, count_vowels, find_hypotenuse, sum_range_of_num, palindrome_check

# Initialize a variable to store name of assistant (task 1)
assitant_name = "Joshua"
# Use print() statement to dislaay a greeting and assistant's name
# Use f-strings to print variables containing assistant name
print(f"\nHello, my name is {assitant_name}, your digital assistant.\n")

# Initialize a variable to store information for assistant to say (task 2)
assistant_info_01 = "The Software (or System) Development Life Cycle (SDLC) is a systematic approach that breaks the software process into phases--planning, analysis, design, implementation and maintenance.\n"

# Use print() to display string stored in assitan_info_01
print(assistant_info_01)
# Initialize a variable to store information for assistant to say (task 3)
assistant_info_02 = """The design process focus on how the system or software product will be developed. The design phases may provide infrastructure and organizational changes for the new system, 
a data schema (relational schema), metadata (to define tables), a function hierarchy diagram, psuedocode for each module, or a protoype of the new system.\n"""
# create empty line
print(assistant_info_02)

# Use print() to display message (task 4)
print("Well, that is enough about SDLC! I am so happy you have come back!! I've got some new tricks I want to show you.\n")
# Create function to Display 5 new tricks the digital assistant can perform
# user input() to get user's selections of trick to run
def menu():
    polling_active = True #variable use to determine if function should repeat
    while polling_active: # Use while loop to restart menu function if conditions are valid.
        print("================ My Bag of Tricks ==================")
        print("| (1) Counting Vowels                              |")
        print("| (2) Hypotenuse of A Triangle                     |")
        print("| (3) Sum a range of numbers from 1                |")              
        print("| (4) Convert temp to Fahrenheit                   |")
        print("| (5) Determine if the phrase is a palindrome      |")
        print("====================================================")
        selection = (input("Please pick a trick for me to perform: Enter (1-5) or 'q' to exit : "))
    
# Use conditional statment to determine which functions to run based on user's selection      
        if(selection == 'q'):
            return
        elif(selection == '1'):
            res = count_vowels("hello this is me")
            print("Numbers of vowels is : ",res)
        elif(selection == '2'):
            res = find_hypotenuse(short_side=2,long_side=5)
            print("The Hypotenuse is : ", res) 
        elif(selection == '3'):
            res = sum_range_of_num(5)
            print("The sum is : ", res)
        elif(selection == '4'):
            res = convert_to_fahrenheit()
            print("The temp in Fahrenheit is : ",res)
        elif(selection == '5'):
            res = palindrome_check("aba")
            if(res):
                print("Yes, the phrase is a Palindrome.")
            else:
                print("Nope not a Palindrome")
        else:
            print("Hmm I don't know that one, please pick a trick from the list.\n")

# Use to repeat the program until 'n' is typed (Task 6)
        repeat = input("\nWould you like to see another trick? (y/n)") #Repeats the menu() function if answer is not 'n'
        if repeat == 'n':   # Use to exit the program (Task 8)
            polling_active = False
            print("\nFine be that way.  Goodbye!\n")


menu() #call the main function


