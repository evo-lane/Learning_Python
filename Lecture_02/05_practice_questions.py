print("_________________practice questions______________")
print()

# Question (1)
# Write a program to input user's first name and print its length

name = input("Enter your name :")
print("Length of your name is :", len(name))
print()

# Question (2)
# Write a program to find the occurrence of '$' in a string

str1 = "Hi, I am $ symbol. I worth 89$."
print("Occurrence of '$' :", str1.count("$"))
print()

# Question (3)
# Write a program that grade students based on marks
# marks >= 90, grade ="A"
# 90 > marks >= 80, grade ="B"
# 80 > marks >= 70, grade ="C"
# 70 > marks, grade ="D"

marks = int(input("Enter your marks :"))

if (marks >= 90):
    print("grade A")
elif(marks < 90 and marks >= 80):
    print("grade B")
elif(marks < 80 and marks >= 70):
    print("grade C")
else:
    print("grade D")
print()

# Question (4)
# Write a program to check if a number entered by the user is odd or even. 
 
num = int(input("Enter a number :"))
if (num %2 == 0):
    print("You entered an even number")
else:
    print("You entered an odd number")
print()

# Question (5)
# Write a program to find the greatest of three numbers entered by the user.

a = int(input("Enter first num :")) 
b = int(input("Enter second num :")) 
c = int(input("Enter third num :")) 
if (a > b and a > c):
    print("First num is greatest :", a)
elif (b > a and b > c):
    print("Second num is greatest :", b)
else:
    print("Third num is greatest :", c)
print()

# Question (6)
# Write a program to check if a number is multiple of seven or not.

num1 = int(input("Enter a number :"))
if (num1 %7 == 0):
    print("This number is Multiple of 7")
else:
    print("This number is not Multiple of 7")
    
    