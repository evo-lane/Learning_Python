# Lecture_03 Practice Problems

# ____________List Practice Problems____________ :

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

print("Question 1:")
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

print("Question 2:")
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

print("Question 3:")
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

print("Question 4:")
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

print("Question 5:")
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

print("Question 6:")
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

print("Question 7:")
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

print("Question 8:")
print()

hours = [2, 4, 3, 5, 6, 1, 4]
original_hours = hours.copy()

# Hours from 3rd day to 6th day

print("Obtained Portion:" ,hours[2:6])

# Sorting obtained portion

portion = hours[2:6]
portion.sort(reverse = True)
print("Sorted Portion: ", portion)

# Displaying the original list

print("Original List:", original_hours)
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

print("Question 9:")
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

print("Question 10:")
print()

python_progress = ["Variables",85,"Strings",True,72]
original_list = python_progress.copy()

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

print("Original List:", original_list)

# Displaying the sliced portion

print("Sliced Portion :", sliced_portion)
print()