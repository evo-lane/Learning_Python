# Lecture_03 Practice Problems

# ____________List Practice Problems____________ :

print("____________List Practice Problems____________")
print()

# ___________(Question 1)__________

# You are given the marks of 6 students:
# marks = [72, 58, 91, 64, 83, 47]
# The teacher discovers that the student who originally received 47 actually scored 57.
# Write a program that:
# 1. Displays the original list.
# 2. Corrects the marks.
# 3. Adds the marks of a new student, 88, to the list.
# 4. Displays the updated list.

# Solution:-

print("___________(Question 1)__________")
print()

# Displaying the original list

marks = [72, 58, 91, 64, 83, 47]
print("Original Marks:",marks)

# Correcting the marks

marks[-1] = 57
print("After correction:",marks)

# Adding marks of new student

marks.append(88)

# Displaying the updated list

print("Updated list :", marks)
print()

# ___________(Question 2)__________

# A student has prepared this shopping list:
# shopping = ["Notebook", "Pen", "USB", "Folder"]
# Before going to the shop, she realizes that:
# - "Pencil" should be inserted after "Pen".
# - "USB" is no longer needed.
# - She also wants to add "Highlighter" at the end.
# Modify the list accordingly and display the final shopping list.

# Solution:-

print("___________(Question 2)__________")
print()

# Inserting Pencil after Pen 

shopping = ["Notebook", "Pen", "USB", "Folder"]
shopping.insert(2,'Pencil')
print('Adding Pencil:',shopping)

# Removing USB from list

shopping.remove('USB')
print('Removing USB:',shopping)

# Adding highlighter at the end 

shopping.append('Highlighter')
print('Adding Highlighter:',shopping)

# Displaying the final list

print('Shopping List:', shopping)
print()

#  ___________(Question 3)__________

# A teacher has recorded scores in the order in which students submitted their work:
# scores = [45, 78, 62, 91, 56, 84]
# The teacher now wants to see:
# 1. The scores from highest to lowest.
# 2. The scores from lowest to highest.
# 3. The original order again.
# Write a program that performs these operations.

# Solution:-

print("___________(Question 3)__________")
print()

scores = [45, 78, 62, 91, 56, 84]
original_scores = scores.copy()

# Scores from highest to lowest

scores.sort(reverse=True)
print('highest to lowest:', scores)

# Scores from lowest to highest

scores.sort()
print("lowest to highest:", scores)

# Displaying the original order

print("Original order:", original_scores)
print()

#  ___________(Question 4)__________

# A student keeps the marks of her five most recent assignments:
# assignments = [76, 81, 69, 88, 92]
# She wants to review only the first three assignment results and separately review the last two results.
# Display both portions without changing the original list.

# Solution:-

print("___________(Question 4)__________")
print()

assignments = [76, 81, 69, 88, 92]

# Reviewing the first three

print(assignments[:3])

# Reviewing the last two

print(assignments[-2:])

# Original list

print('Original List:', assignments)
print()

#  ___________(Question 5)__________

# A university department records the roll numbers of students:
# roll_numbers = [101, 102, 103, 104, 105, 106, 107, 108]
# The teacher wants to work with only the students whose roll numbers are from 103 through 106.
# Create a separate portion containing those students and display it.
# Then display the original list to verify that it has not changed.

# Solution:-

print("___________(Question 5)__________")
print()

roll_numbers = [101, 102, 103, 104, 105, 106, 107, 108]

# Creating Separate portion

print("Selected Students:", roll_numbers[2:6])

# Displaying original list

print("Original List:", roll_numbers)
print()

#  ___________(Question 6)__________

# Create a list representing the basic information of a student:
# - name
# - age
# - semester
# - GPA
# - whether the student is currently enrolled
# Use appropriate Python values for each piece of information.
# Then:
# 1. Access the student's name.
# 2. Access the GPA.
# 3. Change the semester.
# 4. Change the enrollment status.
# 5. Display the complete updated list.

# Solution:-

print("___________(Question 6)__________")
print()

# Basic information of a student

name = 'Tim'
age = 22
semester = 8
GPA = 3.4
enrolled = True

# Creating a List

student = [name, age, semester, GPA, enrolled]

# Accessing the name

print("Name: ", student[0])

# Accessing the GPA

print("GPA: ", student[3])

# Changing the semester

student[2] = 7
print("Semester: ", student[2])

# Changing the enrollment status

student[4] = False 
print("Enrollment status: ", student[4])

# Displaying the updated list

print("Updated list:", student)
print()

#  ___________(Question 7)__________

# You are given:
# numbers = [5, 8, 5, 12, 7, 5]
# The program should remove only the first occurrence of 5.
# Then display the list.
# After that, insert 20 at index 2 and display the updated list.

# Solution:-

print("___________(Question 7)__________")
print()

numbers = [5, 8, 5, 12, 7, 5]

# Removing first occurrence of 5

numbers.remove(5)

# Displaying the list

print("Numbers: ",numbers)

# Inserting 20 

numbers.insert(2,20)

# Displaying the updated list

print("Updated Numbers: ",numbers)
print()

#  ___________(Question 8)__________

# A student's weekly study hours are stored as:
# hours = [2, 4, 3, 5, 6, 1, 4]
# She wants to inspect only the hours from the third day through the sixth day.
# After obtaining that portion, she wants to sort the obtained portion from highest to lowest.
# Finally, display both the portion and the original list.

# Solution:-

print("___________(Question 8)__________")
print()

hours = [2, 4, 3, 5, 6, 1, 4]

# Hours from 3rd day to 6th day

portion = hours[2:6]

# Sorting obtained portion

portion.sort(reverse = True)
print("Sorted Portion: ", portion)

# Displaying the original list

print("Original List:", hours)
print()

#  ___________(Question 9)__________

# A small study application keeps track of topics the student has completed:
# topics = ["Variables", "Strings", "Lists"]
# During the study session:
# - "Tuples" is completed and should be added.
# - "Strings" is reviewed again but should remain in the list.
# - "Variables" needs to be removed because the student decides to restart that topic later.
# - "Loops" is then added.
# Write the program and display the final list.

# Solution:-

print("___________(Question 9)__________")
print()

topics = ["Variables", "Strings", "Lists"]

# Adding Tuple

topics.append("Tuples")
print(topics)

# Removing Variables

topics.remove("Variables")
print(topics)

# Adding Loops

topics.append('Loops')

# Displaying the final list

print("Final List:", topics)
print()

#  ___________(Question 10)__________

# A student is maintaining a record of her Python learning:
# python_progress = ["Variables",85,"Strings",True,72]
# Perform the following tasks:
# 1. Display the student's current progress record.
# 2. Access the first topic.
# 3. Access the score 72.
# 4. Change 72 to 80.
# 5. Add "Lists" to the end.
# 6. Insert 90 before "Lists".
# 7. Remove "Strings".
# 8. Create a slice containing the last three elements.
# 9. Reverse the original list.
# 10. Finally, display the original list and the sliced portion.

# Solution:-

print("___________(Question 10)__________")
print()

python_progress = ["Variables",85,"Strings",True,72]

# Displaying student's current record

print("Student record: ", python_progress)

# Accessing the first topic

print("First Topic:", python_progress[0])

# Accessing the score 72

print("Score :", python_progress[4])

# Changing 72 to 80

python_progress[4] = 80
print("Changing 72 to 80:", python_progress)

# Adding "Lists" to the end

python_progress.append("Lists")
print("Adding 'List' :",python_progress)

# Inserting 90 before "Lists"

python_progress.insert(5,90)
print("Inserting 90: ",python_progress)

# Removing "Strings"

python_progress.remove("Strings")
print("Removing 'Strings' :",python_progress)

# Creating a slice containing the last three elements

sliced_portion = python_progress[-3:]

# Reversing the original list

python_progress.reverse()
print("Reversed List: ",python_progress)

# Displaying the original list

print("Modified original List:", python_progress)

# Displaying the sliced portion

print("Sliced Portion :", sliced_portion)
print()

# ____________Tuple Practice Problems____________ :

print("____________Tuple Practice Problems____________")
print()

#  ___________(Question 1)__________

# A point on a screen is represented by:
# point = (120, 250)
# Write a program that:
# 1. Displays the complete point.
# 2. Displays the x-coordinate.
# 3. Displays the y-coordinate.
# Then try to change the x-coordinate to 150.

# Solution:-

print("___________(Question 1)__________")
print()

point = (120, 250)
print("Point: ", point)           # Displaying the complete point
print("x-coordinate: ", point[0]) # Displaying the x-coordinate
print("y-coordinate: ", point[1]) # Displaying the y-coordinate
# point[0] = 150 is invalid because tuple does not support item assignment
# The concept of immutability is used here
print()

#  ___________(Question 2)__________

# Create a tuple containing:
# - student's name
# - age
# - semester
# - department
# Then access each piece of information individually using indexing.
# Finally, display the complete tuple.

# Solution:-

print("___________(Question 2)__________")
print()

student_tup = ("Jasmine", 23, 8, "IT")           # Creating a tuple

print("Name:                ", student_tup[0])   # Accessing name
print("Age:                 ", student_tup[1])   # Accessing age
print("Semester:            ", student_tup[2])   # Accessing semester
print("Department:          ", student_tup[3])   # Accessing department
print("Student Information: ", student_tup)
print()

#  ___________(Question 3)__________

# Represent the fixed parts of an address using a tuple:
# Country → Province → City
# Create your own example and then:
# 1. Display the complete tuple.
# 2. Access the country.
# 3. Access the city.
# 4. Display the portion containing the province and city.

# Solution:-

print("___________(Question 3)__________")
print()

address = ('Pakistan', 'Sindh', 'Karachi') # Representing address using tuple

print("Address:         ", address)        # Displaying complete address/tuple
print("Country:         ", address[0])     # Accessing country
print("City:            ", address[2])     # Accessing city
print("Province & City: ", address[1:])   # Displaying province and city portion
print()

#  ___________(Question 4)__________

# You have:
# numbers = (10, 20, 30, 40, 50, 60)
# Create a new tuple containing:
# 30, 40, 50
# Then display:
# 1. The new tuple.
# 2. The original tuple.

# Solution:-

print("___________(Question 4)__________")
print()

numbers = (10, 20, 30, 40, 50, 60)      # Given Tuple
new_numbers = numbers[2:5]              # New Tuple
print("New numbers:      ",new_numbers) # Displaying new Tuple
print("Original numbers: ", numbers)    # Displaying original Tuple
print()

#  ___________(Question 5)__________

# Given:
# data = (4, 7, 4, 9, 4, 2)
# Find:
# 1. The index of the first occurrence of 4.
# 2. How many times 4 occurs in the tuple.

# Solution:-

print("___________(Question 5)__________")
print()

data = (4, 7, 4, 9, 4, 2)
print("First occurrence of 4:  ", data.index(4))
print("Total occurrences of 4: ", data.count(4))
print()

#  ___________(Question 6)__________

# You need to store one fixed value, "Python", as a tuple.
# Create the tuple correctly.
# Then print:
# 1. Its value.
# 2. Its type.
# After that, create another variable containing "Python" 
# without making it a tuple and compare the two.

# Solution:-

print("___________(Question 6)__________")
print()

python_tuple = ("Python",)                      # Creating a tuple
print("My tuple:         ", python_tuple)       # Printing the value of tuple
print("Type of tuple:    ", type(python_tuple)) # Printing the type of tuple
my_var = "Python"                         # Creating a variable
print("My Variable:      ", my_var)       # Printing the value of variable
print("Type of Variable: ", type(my_var)) # Printing the type of variable
print()

#  ___________(Question 7)__________

# Imagine you are writing a small program that stores the coordinates of a
# student's classroom: Building number, Floor number, Room number
# Create this information as one tuple.
# Then:
# 1. Access the room number.
# 2. Access the building number.
# 3. Slice the tuple to obtain the floor and room information.
# Do not modify the tuple.

# Solution:-

print("___________(Question 7)__________")
print()

building_num = 17
floor_num = 4
room_num = 102
coordinates = (building_num, floor_num, room_num) # Creating tuple
print("Room Number      :", coordinates[2])       # Accessing room number
print("Building Number  :", coordinates[0])       # Accessing building number
print("Floor & room num :", coordinates[1:3])     # Accessing the floor and room information
print()

#  ___________(Question 8)__________

# A programmer needs to store the following information about a university campus:
# ("BZU", "Multan", "Pakistan")
# The three values belong together and represent one fixed location.
# Create an appropriate Python structure for this information.
# Then explain in your own words why you chose that structure instead of a list.

# Solution:-

print("___________(Question 8)__________")
print()

camp_info = ("BZU", "Multan", "Pakistan")

# I chose a tuple because these three values represent one fixed location and should not be changed.
# Tuples are immutable, so their elements cannot be modified after creation.
print()

#  ___________(Question 9)__________

# A program receives:
# rgb = (255, 255, 255)
# The values represent a fixed RGB color.
# Write a program that:
# 1. Displays the complete tuple.
# 2. Accesses each individual value.
# 3. Creates a slice containing the last two values.
# 4. Displays the original tuple afterward.
# Then answer:
# Why is being unable to modify the tuple not a problem in this situation?

# Solution:-

print("___________(Question 9)__________")
print()

rgb = (255, 255, 255)    # Given tuple
print("Color :", rgb)    # Displaying tuple
print("Red   :", rgb[0]) # Accessing each individual value
print("Green :", rgb[1]) 
print("Blue  :", rgb[2])
last_two = rgb[1:3]            # Accessing last two values
print("Last two       :", last_two)
print("Original color :", rgb) # Displaying the original tuple

# Being unable to modify the tuple is not a problem because the RGB values represent a
# fixed color and we only need to access and display them, not change them.
print()

#  ___________(Question 10)__________

# A university wants to store the fixed identity of a classroom:
# University, Campus, Building, Floor, Room Number
# Create this information as a tuple.
# Your program should then:
# 1. Display the complete tuple.
# 2. Access the university name.
# 3. Access the room number.
# 4. Access the building and floor using a slice.
# 5. Find the index of one value.
# 6. Count how many times a value occurs if you deliberately include one repeated value.
# 7. Create a one-element tuple containing only the room number.
# 8. Try to modify one element and observe what happens.
# 9. Display the original tuple again.
# 10. In 2–3 sentences, explain why a tuple is more appropriate here than a list.

# Solution:-

print("___________(Question 10)__________")
print()

uni = "IUB"    # Information
camp = "Main"
build = 12
floor = 3
room_num = 8

classroom = (uni, camp, build, floor, room_num)            # Creating tuple
original_classroom = classroom                             # Preserving the original tuple

print("Classroom Information :", classroom)                # Displaying the complete tuple
print("University name :", classroom[0])                   # Accessing university name
print("Room number :",classroom[4])                        # Accessing room number
print("Building & Floor no :", classroom[2:4])             # Accessing building and floor number
print("Index of 'build' :", classroom.index(build))        # Finding index of a value
classroom = (uni, camp, build, floor, room_num, floor)     # Adding floor on purpose
print("Occurrences of 'floor' :", classroom.count(floor))  # Counting number of occurrences of 'floor'
one_element_tup = (room_num,)                              # Creating one element tuple 

# classroom[0] = "BZU" (TypeError: 'tuple' object does not support item assignment)
# We cannot modify any element of a tuple because tuples are immutable. If we try to change any element an error will occur

print("Original tuple :", original_classroom)

# Here tuple is more appropriate because we are dealing with the data that should remain unchanged
print()

