#!/usr/bin/env python3

# Declare a function that read and print out to the sceen the contents of cats.txt and dogs.txt (Task a)
def read_txt_file():
    # Open cats.txt file
    with open('cats.txt') as name:
         # Read cats.txt file
         cat_name = name.read()
         #prints content of cats.txt file
         print(cat_name)
    # Open dogs.txt file
    with open('dogs.txt') as name:
         # Read dogs.txt file
         dog_name = name.read()
         # Print content of dogs.txt file
         print(dog_name)

# Declare a function that copies cats.txt and dogs.txt into animals.txt (Task b)
def copy_file_to_file():
    # Creating a list of filenames
    filenames = ['cats.txt', 'dogs.txt']
    # Open file3 in write mode
    with open('animals.txt', 'w') as outfile:
        # Iterate through list
        for names in filenames:
            # Open each file in read mode
            with open(names) as infile:
                # read the data from cats.txt and
                # dogs.txt and write it in animals.txt
                outfile.write(infile.read())
            # Add '\n' to enter data of dogs.txt
            # from next line
            outfile.write("\n")

# Call functions
read_txt_file()
copy_file_to_file()
