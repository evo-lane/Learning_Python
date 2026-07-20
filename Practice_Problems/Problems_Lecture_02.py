# Lecture_02 Practice Problems

# Problem 2.1: String Operations Suite 
# (Covers: len(), endswith(), capitalize(), replace(), find(), count())

# Statement: Ask the user to enter a sentence. Perform these operations:
# Display length using len()
# Check if it ends with "." using endswith()
# Capitalize first letter using capitalize()
# Replace all spaces with "_" using replace()
# Find position of "Python" using find()
# Count letter 'e' using count()
# Display all results

# Solution:-

print("____________________________(Problem 2.1)_______________________")
print()

# Taking input from user

sentence = input("Enter a sentence :")
print()

# Performing operations

print("length of string :", len(sentence))
print("Does string ends with '.' :", sentence.endswith("."))
print("Capitalizing 1st letter of string :", sentence.capitalize())
print("Replacing spaces with '_' :", sentence.replace(" ","_"))
print("Position of 'Python' :", sentence.find("Python"))
print("Counting letter 'e' in string :", sentence.count("e"))
print()

# Problem 2.2: String Indexing and Slicing
# Statement: Ask the user to enter a word with at least 8 characters. Display:
# The first character using positive indexing
# The last character using negative indexing
# Characters from index 2 to 5 using slicing
# Display all results with proper labels

# Solution:-

print("____________________________(Problem 2.2)_______________________")
print()

# Taking input from user

word = input("Enter a word with at least 8 characters :")
print()

# Displaying

print("First character :", word[0])                  # positive indexing
print("Last character :", word[-1])                  # negative indexing
print("Characters from index 2 to 5 :", word[2:6])   # slicing
print()

# Concepts used: Positive Indexing, Negative Indexing, Slicing, len(), Input

# Problem 2.3: String Concatenation and Length Check
# Statement: Ask the user for their first name and last name.
# Concatenate them to create a full name
# Create an email ID: firstname.lastname@university.edu
# Display the length of the full name using len()
# Check if the length is greater than 15
# If length > 15, display "Long name"
# Else, display "Short name"

# Solution:-

print("____________________________(Problem 2.3)_______________________")
print()

# Taking input from user

first_name = input("Enter your first name :")
last_name = input("Enter your last name :")
print()

# Concatenation

full_name = first_name +" "+ last_name         # concatenating strings
print("Your full name is :", full_name)        # printing full name
length = len(full_name)
print("Length of full name :", length)         # printing length of full name
print()
email = first_name + "." + last_name + "@university.edu"
print("Email ID :", email)

# checking

if length > 15:
    print("Long name")
else:
    print("Short name")
print()

# Concepts used: String Concatenation, len(), if-else, Comparison Operators

# Problem 2.4: Escape Sequences Display
# Statement: Write a program that displays this exact output using escape sequences (DO NOT use multiple
# print statements):
# text
# Hello "Student"!
# Age: 20	City: Lahore
# This is backslash: \
# Line 1
# Line 2
# HelloWorld
# Note: For the last line, use \b to remove a character
# Concepts used: Escape Sequences (\n, \t, \, ', \b)

# Solution:-

print("____________________________(Problem 2.4)_______________________")
print()

# Printing statement using escape sequence

print('text\nHello "Student"!\nAge: 20\tCity: Lahore\nThis is backslash: \\\nLine 1\nLine 2\nHelloWorld \b')
print()

# Concepts used: Escape Sequences (\n, \t, \, ', \b)

# Problem 2.5: Conditional String Analysis
# Statement: Ask the user to enter a sentence.
# Using if-elif-else:
# If the sentence is empty (length = 0) → display "Empty sentence"
# Else if the sentence ends with "?" → display "It's a question"
# Else if the sentence ends with "!" → display "It's an exclamation"
# Else if the sentence contains "Python" → display "Python found!"
# Else → display "Regular sentence"
# Always capitalize the first letter using capitalize() and display it.
# Concepts used: if-elif-else, len(), endswith(), find(), capitalize()

# Solution:-

print("____________________________(Problem 2.5)_______________________")
print()

# Taking input from user as string

text = input("Enter a statement :")
length = len(text)
print("Sentence :",text.capitalize())
print()

# Checking

if length == 0:
    print("Empty sentence")
elif text.endswith("?"):
    print("It's a question")
elif text.endswith("!"):
    print("It's an exclamation")
elif "Python" in text:
    print("Python found!")
else:
    print( "Regular sentence")
print()