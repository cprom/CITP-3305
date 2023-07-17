import math
# Create Function to perform 5 tricks (Task 5)
# Function moved to different file and imported by main function (Task 7)
def count_vowels(string):
    count = 0
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    print("Okay, counting Vowels Now!\n")
    for char in string:
        if (char in vowels):
           count += 1
    return count
    
def find_hypotenuse(long_side, short_side): # Keyword Arguments
    print("I am finding the hypotenuse of the triagle now.\n")
    hypotenuse = math.sqrt(long_side ** 2 + short_side ** 2)
    return hypotenuse

def sum_range_of_num(num):
    print(f"Okay, I will sum the numbers from 1 to {num}.\n")
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum

def convert_to_fahrenheit(degree_celcius = 100): #default value
    print(f"Let me the temperature of {degree_celcius} degree celcius to Fahrenheit for you.\n")
    degree_f = (degree_celcius * 1.8) + 32
    return degree_f

def palindrome_check(phrase):
    print(f"Checking if the phrase \"{phrase}\" is a Palindrome.\n")
    if(phrase == phrase[::-1]):
        return True
    else:
        return False