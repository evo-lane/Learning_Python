# Topic : Lists in Python

# Method to store values 

marks1 = 20.1
marks2 = 34.5
marks3 = 67.9
marks4 = 95.2
marks5 = 89.0

print("_________________________________Lists____________________________________")
print()

# Alternate method to store multiple values at once 

marks = [20.1, 34.5, 67.9, 95.2, 89.0]  # List is a built-in data type that can store multiple values of different data types.
print("marks :", marks)
print("Type of marks :", type(marks))   # we can print type of our list
print("Length of marks :", len(marks))  # we can print length of our list
print()

# Lists can store values of different data types

student = ["Jasper", 56.9, 100, True, None]  # List contains values of type: str, float, int, bool and NoneType

print("student :", student)
print("Data type of list 'student' :", type(student))
print("Data type of value at 0th index :", type(student[0]))
print("Data type of value at 1st index :", type(student[1]))
print("Data type of value at 2nd index :", type(student[2]))
print("Data type of value at 3rd index :", type(student[3]))
print("Data type of value at 4th index :", type(student[4]))
print()

# Indexing in lists

print("_____________________________Indexing in Lists________________________________")
print()

std_marks = [87, 64, 33, 95, 76]
print("Marks at first index :", std_marks[0])   # value at 0th index
print("Marks at second index :", std_marks[1])  # value at 1st index
print("Marks at third index :", std_marks[2])   # value at 2nd index
print()

print("_____________________________Mutation in Lists________________________________")
print()

# Lists are mutable. They can be modified.

student = ["Jasper", 56.9, 100, True, None]
print("student list before mutation :", student)
student[0] = "James"                               # assigning new value to each index
student[1] = 45.8
student[2] = 50
student[3] = False                 
print("student list after mutation :", student)
print()

print("_____________________________Lists Slicing________________________________")
print()

# Positive indexing => accessing/mutating marks with positive index

marksNew = [67, 17, 34, 100, 78]
print(marksNew [1:4])        # ending is not included
print(marksNew [:4])         # same as marksNew [0:4]
print(marksNew [1:])         # same as marksNew [1:4] or marksNew [1:len(marksNew)]

# Negative indexing => accessing/mutating marks with negative index

print(marksNew[-3:-1])       # Negative indexing follows left-to-right slicing.
print()

print("_____________________________Lists Method________________________________")
print()

my_list = [2, 1, 3]

# append() => adds one element at the end of the list

print("append :")

my_list.append(4)        
print(my_list)

new_list = ['a','f','h','j','k','e']
new_list.append('x')
print(new_list)
print()

# sort() =># sort values in ascending order

print("Ascending order :")

my_list.sort()         
print(my_list)

new_list = ['a','f','h','j','k','e']
new_list.sort()
print(new_list)
print()

# list.sort(reverse = True) => # sort values in descending order

print("Descending order :")

my_list.sort(reverse = True) 
print(my_list)

new_list = ['a','f','h','j','k','e']
new_list.sort(reverse = True)
print(new_list)
print()

# reverse() => reverses the order of the list

print("Reverse of 'my_list' :")

my_list.reverse()
print(my_list)

new_list = ['a','f','h','j','k','e']
new_list.reverse()
print(new_list)
print()

# insert() => add value at a particular index in list

print("Inserting :")
my_list.insert(0,12)
print(my_list)

new_list.insert(3,100)
print(new_list)

new_list.insert(4,"yellow")
print(new_list)
print()

# remove() => erase first occurrence of a value in a list

print("Removing :")
num = [2, 3, 4, 3, 5]
num.remove(3)
print(num)
print()

# pop()

print("Popping :")
num = [2, 3, 4, 3, 5]
num.pop(4)
print(num)