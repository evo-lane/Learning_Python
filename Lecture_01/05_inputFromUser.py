# Topic: input in Python

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city name: ")

print("Your name is :", name)               # print(type(name)) = <class 'str'>
print("Your age is :", age)                 # print(type(age)) = <class 'str'>
print("You live in :", city)                # print(type(city)) = <class 'str'>

# By default, input() function takes input as string data type.
# If we want to take input as integer or float data type, we have to convert it using int() or float() function.

age2 = int(input("Enter your age: "))
print("Your age is :", age2)                 # print(type(age2)) = <class 'int'>
