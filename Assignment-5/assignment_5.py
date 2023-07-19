#!/usr/bin/env python3
import math

# Create class (Task 1)
class DigitalAssistant:
    def __init__(self, name, greeting1, greeting2):
        # Initialize attributes to describe the digital assistant
        self.name = name
        self.greeting1 = greeting1
        self.greeting2 = greeting2

        #print(greeting1)
        #print(greeting2)

    def alive_statement(self):
        """Display a greeting."""
        print(f"\nGreetings Professor {self.name}, shall we play a game?\n")
    # add menu() and trick functions as method for DigitalAssistant class Task 3
    def menu(self):
        """Display 5 functions user can choose and have assistant run"""
        # Use print() to display message 
        print("Well, that is enough about SDLC! I am so happy you have come back!! I've got some new tricks I want to show you.\n")
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

            def count_vowels(string):
                """count vowels in a string"""
                count = 0
                vowels = {'a','e','i','o','u','A','E','I','O','U'}
                print("\nOkay, counting Vowels Now!\n")
                for char in string:
                    if (char in vowels):
                        count += 1
                return count
            
            def find_hypotenuse(long_side, short_side): # Keyword Arguments
                """given 2 sides calculate the hypotenuse of a triangle"""
                print("\nI am finding the hypotenuse of the triagle now.\n")
                hypotenuse = math.sqrt(long_side ** 2 + short_side ** 2)
                return hypotenuse

            def sum_range_of_num(num):
                """sum all numbers from 1 to a number value"""
                print(f"\nOkay, I will sum the numbers from 1 to {num}.\n")
                sum = 0
                for i in range(1, num + 1):
                    sum += i
                return sum

            def convert_to_fahrenheit(degree_celcius = 100): #default value
                """convert temperature from celcius to fahrenheit"""
                print(f"\nLet me the temperature of {degree_celcius} degree celcius to Fahrenheit for you.\n")
                degree_f = (degree_celcius * 1.8) + 32
                return degree_f

            def palindrome_check(phrase):
                """check to see if a phrase is a palindrome"""
                print(f"\nChecking if the phrase \"{phrase}\" is a Palindrome.\n")
                if(phrase == phrase[::-1]):
                    return True
                else:
                    return False   
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
                print("\nHmm I don't know that one, please pick a trick from the list.\n")

            # Use to repeat the program until 'n' is typed 
            repeat = input("\nWould you like to see another trick? (y/n)") #Repeats the menu() function if answer is not 'n'
            if repeat == 'n':   # Use to exit the program (Task 8)
                polling_active = False
                print("\nIt was a pleasure speaking with you today.  Goodbye!\n")


