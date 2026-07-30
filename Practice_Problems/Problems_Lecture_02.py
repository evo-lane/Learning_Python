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

# Problem 2.6: String Counting Operations
# Statement: Ask the user to enter a sentence.
# Calculate and display:
# Total characters using len()
# Number of spaces using count()
# Characters without spaces (Total - spaces)
# Number of vowels (count 'a' + count 'e' + count 'i' + count 'o' + count 'u')
# Number of words (spaces + 1)
# Display all results with proper labels
# Concepts used: len(), count(), Arithmetic Operators, Input

# Solution:-

print("____________________________(Problem 2.6)_______________________")
print()

# Taking input from user

statement = input("Enter a sentence :")
print()

# Displaying Total characters
print("Total characters in string :", len(statement))
print()

# Displaying Number of spaces
print("Number of spaces :", statement.count(" "))
print()

# Displaying characters without spaces
char_without_space = len(statement) - statement.count(" ")
print("Characters without spaces :", char_without_space)
print()

# Displaying Number of vowels
vowels = (statement.count("a")+
statement.count("e")+
statement.count("i")+
statement.count("o")+
statement.count("u"))
print("Total number of vowels :", vowels)
print()

# Displaying Number of words
num_of_words = statement.count(" ") + 1
print("Number of words :", num_of_words)
print()

# Problem 2.7: Nested if - Login System
# Statement: Create a program that:
# Ask the user for username (assume correct username = "admin")
# If username is correct:
# Ask for password (assume correct password = "1234")
# If password is correct → display "Login Successful"
# Else → display "Invalid Password"
# Else → display "Invalid Username"
# If login is successful, ask for withdrawal amount (balance = 10000)
# If amount <= balance → display "Remaining balance: [amount]"
# Else → display "Insufficient balance"
# Concepts used: Nesting, if-elif-else, Comparison Operators

# Solution:-

print("____________________________(Problem 2.7)_______________________")
print()

# Taking input from user

user_name = input("Enter user name :") 
print()

# Checking

if user_name == "admin":                        # correct user name = admin
    password = input("Enter password :")     # asking for password
    if password == "1234":                         # correct password = 1234
        print("Login Successful")               # displaying login successful
        balance = 10000
        withdrawal_amount = int(input("Enter withdrawal amount :")) # asking for withdrawal amount
        if withdrawal_amount <= balance:
            remaining_balance = balance - withdrawal_amount
            print("Remaining balance :", remaining_balance)
        else:
            print("Insufficient balance")
    else:
        print("Invalid Passowrd")
else:
    print("Invalid Username")
print()
    
# Problem 2.8: Grade Calculator with Nested if
# Statement: Ask the user for marks in three subjects (out of 100 each). 
# Calculate the average.
# Using if-elif-else, assign grade:
# Average >= 90: Grade A+
# Average >= 80: Grade A
# Average >= 70: Grade B
# Average >= 60: Grade C
# Average >= 50: Grade D
# Average < 50: Grade F
# Using nested if:
# If grade is A+ or A → display "Excellent Performance"
# Else if grade is B or C → display "Good Performance"
# Else → display "Needs Improvement"
# Check if student passed (average >= 50) using logical operators
# Concepts used: if-elif-else, Nested if, Logical Operators (and, or), Comparison Operators

# Solution:-

print("____________________________(Problem 2.8)_______________________")
print()

# Taking input from user

marks1 = int(input("Enter marks of 1st subject :"))
marks2 = int(input("Enter marks of 2nd subject :"))
marks3 = int(input("Enter marks of 3rd subject :"))
print()

# Validating marks

if (marks1 >= 0 and marks1 <= 100) and (marks2 >= 0 and marks2 <= 100) and (marks3 >= 0 and marks3 <= 100):

    # calculating average
    
    total = marks1 + marks2 + marks3
    average = total/3
    print("Average :", average)

    # checking condition

    if average >= 80:
        if average >= 90:
            print("Grade A+")
        else:
            print("Grade A")
        print("Excellent Performance") # This statement is inside outer-if and outside inner-if

    elif average >= 60:
        if average >= 70:
            print("Grade B")
        else:
            print("Grade C")
        print("Good Performance")

    else:
        if average >= 50:
            print("Grade D")
        else:
            print("Grade F")
        print("Improvement Needed")

    # Checking Pass/Fail

    if average >= 50 and average <= 100:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid Marks! Please enter marks between 0 and 100")
print()

# Problem 2.9: Difference between if and elif
# Statement: Ask the user for a number. Check if the number is divisible by 3, 5, or both.
# Part A: Write using multiple separate if statements (without elif)
# Part B: Write using if-elif-else statements 
# Part C: In comments, explain:
# Why elif is better for mutually exclusive conditions
# What happens in Part A if number is 15 (both conditions true)
# Concepts used: if-elif-else, Difference between if and elif, Arithmetic Operators (%),
# Logical Operators (and, or), Comments

# Solution:-

print("____________________________(Problem 2.9)_______________________")
print()

# Taking input from user

num = int(input("Enter a number :"))
print()

# Checking if the number is divisible by 3, 5, or both 

# _______(Part-A)_______  

if num%3 == 0 and num%5 == 0:
    print("Divisible by 3 and 5 both")
if num%3 == 0:
    print("Divisible by 3")
if num%5 == 0:
    print("Divisible by 5")
print()

# _______(Part-B)_______ 


if num%3 == 0 and num%5 == 0:
    print("Divisible by 3 and 5 both")
elif num%3 == 0:
    print("Divisible by 3")
elif num%5 == 0:
    print("Divisible by 5")
else:
    print("Number is neither divisible by 3 nor by 5")
print()

# _______(Part-C)_______

# Question: Why elif is better for mutually exclusive conditions?
# Answer: 
# elif is better because once one condition becomes True,
# Python skips all remaining conditions.
# This prevents repeated outputs.

# Question: What happens in Part A if number is 15 (both conditions true)?
# Answer: 
# If the number is 15, all three if conditions become True.
# Therefore, Python executes all three if statements
# and prints all three messages.
#______________________________________________________________________________________________

# Problem 2.10: COMPLETE INTEGRATION (ALL Concepts)
# Statement: Create a program that uses ALL Lecture 2 concepts:
# Strings & Input: Ask the user for their full name
# len(): Display the length of the name
# Positive & Negative Indexing:
# Display first character using positive indexing
# Display last character using negative indexing
# Slicing: Display first 3 characters of the name
# String Concatenation: Create "Hello [Name]!" message
# String Functions:
# capitalize() the name
# endswith() check if name ends with 'a'
# find() the position of 'a'
# replace() all 'a' with '@'
# count() how many 'a's are in the name
# Escape Sequences: Display output using \n and \t
# if-elif-else: Check name length:
# < 5: "Short name"
# 5 to 10: "Medium name"
# 10: "Long name"
# Nested if: If length > 5, check if it contains 'a'
# Comparison & Logical Operators: Use >=, <, and, or
# Comments: Add comments explaining each section
# Concepts used: ALL Lecture 2 concepts (Strings, Creating strings, Quotes, Escape Sequences,
# String Concatenation, len(), Positive Indexing, Negative Indexing, Slicing,
# String Functions - endswith(), capitalize(), replace(), find(), count(),
# Conditional Statements - if, elif, else, Difference between if and elif, Nesting)

# Solution:-

print("____________________________(Problem 2.10)_______________________")
print()

# Strings and Input

name = input("Enter your full name :")
print()

# Displaying Length of name

length = len(name)
print("Length of name :", length)

# Displaying first character using positive indexing

print("First character :", name[0])

# Displaying last character using negative indexing

print("Last character :", name[-1])

# Displaying first 3 characters of the name

print("First three characters :", name[0:3])

# Creating "Hello [Name]!" message

str1 = "Hello"
str2 = name
str3 = str1 +" "+ str2 + "!"
print("Concatenated message :", str3)

# capitalizing the name

print("Capitalized string :", name.capitalize())

# checking if name ends with 'a'

print("Name ends with :", name.endswith("a"))

# finding the position of 'a'

print("Position of 'a' :", name.find("a"))

# replacing all 'a' with '@'

print(" Replacing 'a' with '@' :", name.replace('a','@'))

# counting 'a's in the name

print("Number of times 'a' occur in string :", name.count("a"))

# Displaying output using \n and \t

print("\t Your name is \n:", name)

# Checking condition

if length < 5:
    print("Short Name")
elif length >= 5 and length < 10:
    print("Medium name")
    if name.find("a") != -1:
        print("Letter 'a' found at position :", name.find('a'))
    else:
        print("Letter 'a' not found")
else:
    print("Long name")
    if name.find("a") != -1:
        print("Letter 'a' found at position :", name.find('a'))
    else:
        print("Letter 'a' not found")
print()

print("_______________________________END___________________________________")