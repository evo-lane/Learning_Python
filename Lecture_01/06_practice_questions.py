# Topic: Practice Questions (Lecture_01)

# 01_variables practice questions
 
# Question (1)
# Store the details of a book:
# title
# author
# price
# Print them in a neat format.

print("_____________variable practice question # 01_____________ ")
print()

title  = "Harry Potter"          # storing values in variables
author = "J. K. Rowling"
price  = 500

print("________Book Information________")
print()

print("Book name   :", title) 
print("Book author :", author)
print("Book price  :", price)    # printing the values
print()

# Question (2)
# Create a variable temp and initialize it.
# Update the variable.
# Decrease the new value by 7.
# Print the new and old values

print("_____________variable practice question # 02_____________ ")
print()

temp = 40                         # initializing variable
print("temp =", temp)

temp = 35                         # updating variable 
print("new temp =", temp)

temp -= 7
print("Decreased value =", temp) # decreasing value of temp
print()

# Question (3)
# Create three variables:
# length
# width
# unit
# Then print the following output:
# The rectangle has a length of 15 cm and a width of 8 cm.

print("_____________variable practice question # 03_____________ ")
print()

length = 15         # creating variables             
width = 8
unit = "cm"

print("The rectangle has a length of", length, unit, "and a width of", width, unit)
print()

# 02_Data type practice questions
 
# Question (1)
# Create variables to store:
# your university name
# your semester number
# your CGPA (or expected CGPA)
# whether you are hostelite (True/False)
# an unassigned value
# Print each value and its data type.

print("_____________Data type practice question # 01_____________")
print()      

uni_name = "Harvard University"                         # creating variables to store values
sem_num  =  8
CGPA     =  3.6
hostelite = True
unassigned_value =  None

print("My university name is :",uni_name)               # printing values
print("My semester is        : ", sem_num,"th")
print("My CGPA is            :", CGPA)
print("I am hostelite        :", hostelite)
print("unassigned_value      :", unassigned_value)
print()

print("___Data types of variables are :___")
print()
print(type(uni_name))                                   # printing data types of values
print(type(sem_num))
print(type(CGPA))
print(type(hostelite))
print(type(unassigned_value))
print()

# Question (2)
# Create five variables of different data types
# use only one print() statement to display all of them.

print("_____________Data type practice question # 02_____________")
print() 
 
full_name = "Ben James"      # string 
age       =  36              # integer
height    =  5.5             # float
married   =  True            # boolean
hobby     =  None            # None

print("My name is ",full_name,".",
    "\nI am ",age, "years old.",
    "\nMy height is ", height,"ft.", 
    "\nI am married and this is",married,
    "\nMy number of hobbies : ",hobby)
print()

# 03_Operators practice questions

# Question (1)
# A student scored:
# Physics = 81
# Chemistry = 75
# Math = 92
# Find:
# Total Marks
# Average Marks

print("_____________Operator practice question # 01_____________")
print()

Physics      = 81
Chemistry    = 75
Math         = 92

totalMarks   = Physics + Chemistry + Math         # calculating total marks
averageMarks = (Physics + Chemistry + Math)/3     # calculating average marks

print("Total marks   = ", totalMarks)             
print("Average marks = ", averageMarks)           
print()

# Question (2)
# Store two numbers and check whether they are exactly equal.

print("_____________Operator practice question # 02_____________")
print()

a = 12
b = 56

if a == b:
    print("Equal")
else:
    print("Not Equal")
print()

# Question (3)
#Check whether 81 is divisible by 9 or not.

print("_____________Operator practice question # 03_____________")
print()

x = 81
y = 9

if x%9 == 0:
    print("Divisible")
else:
    print("Not Divisible")
print()

# Question (4)
# A student is eligible for admission only if:
# Marks are at least 60
# Age is less than 22
# Use logical operators.

print("_____________Operator practice question # 04_____________")
print()

marks = 85
age   = 18

if marks >= 60 and age < 22 :
    print("You are eligible")
else:
    print("You are not eligible")
print()

# Question (5)
# A website allows login if the user is an Admin OR a Moderator.
# Create suitable Boolean variables and check the result.

print("_____________Operator practice question # 05_____________")
print()

user = "student"

if user == "Admin":
    print("login successful")
elif user == "Moderator":
    print("login successful")
else:
    print("login failed")
print()

# Question (6)
# Reverse the result of this condition using not:
# marks >= 40

print("_____________Operator practice question # 06_____________")
print()

marks >= 40
print("If marks >= 40 is True, then it's reverse will be : ")
print(not(marks >= 40))
print()

# Question (7)
# Start with:
# balance = 1000
# Perform:
# Deposit 500
# Withdraw 200
# Double the balance
# Divide it equally into 2 parts
# using assignment operators.

print("_____________Operator practice question # 07_____________")
print()

balance  =  1000
print("Initial balance :", balance)
balance += 500                               # deposit
print("After deposit balance :", balance)
balance -= 200                               # withdraw
print("After withdraw balance :", balance)
balance *= 2                                 # double
print("After doubling balance :", balance)
balance /= 2                                 # divide
print("After dividing balance :", balance)
print()

# 04_Type Conversion & Type Casting practice questions

# Question (1)
# Convert the integer 25 into a float and print both value and type.

print("_____________Type conversion/casting practice question # 01_____________")
print()

a = 25                              # integer
a = float(25)                       # converting integer into float

print("Integer => float :", a)      
print(type(a))                      # latest data type of a
print()

# Question (2)
# Convert "150" into an integer and subtract 30.

print("_____________Type conversion/casting practice question # 02_____________")
print()

num = "150"                  # string
num = int("150")             # converting string into integer
num -= 30                    # subtracting 30 from int 150

print("Final ans :", num)
print()

# Question (3)
# Convert "45.8" into a float and calculate half of it.

print("_____________Type conversion/casting practice question # 03_____________")
print()

x = "45.8"                            # string
x = float("45.8")                     # converting string into float
print("The value of x =", x)          # printing float value of x
x /= 2                                # calculating half of x
print("The half of x = ", x)          # printing half value of x
print(type(x))                        # printing data type of x
print()

# 05_input practice questions

# Question (1)
# Take the user's first name and last name separately and print the full name.

print("_____________input practice question # 01_____________")
print()

first_name = input("Enter your first name : ")
last_name  = input("Enter your last name  : ",)

print("Your Full name is :",first_name,last_name)
print()

# Question (2)
#Take the user's birth year and calculate their approximate age.

print("_____________input practice question # 02_____________")
print()

birth_year = int(input("Enter your birth year :"))     # Taking birth year as integer
current_year = 2026
approx_age = current_year - birth_year
print("Your age is :", approx_age)
print()

# Question (3)
# Take the side of a square as input and calculate its perimeter.

print("_____________input practice question # 03_____________")
print()

side = int(input("Enter side of square :"))   # Taking side of square as integer
perimeter = 4*side
print("The perimeter of square is :", perimeter)
print()

print("_______________________________END_________________________________")