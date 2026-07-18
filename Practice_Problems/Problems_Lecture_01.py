# Lecture_01 Problems

print("_____________________(Problem 1.1)_________________")
print()

# Problem 1.1: Student Info Card
# Write a program that asks the user for their name (string), age (integer), GPA (float), and whether 
# they are enrolled (boolean - True/False). Then display all this information in a formatted output.
# Also display the data type of each variable using type().

# Solution :-

# Taking input from the user :

name = input("Enter your name :")          # name variable stores a string value
age = int(input("Enter your age :"))       # age variable stores an integer value
GPA = float(input("Enter your GPA :"))     # GPA variable stores a float value
is_enrolled = True                         # is_enrolled variable stores a boolean value
print()

# Displaying all the information in formatted output :

print("__________________Your Information_______________")
print()

print("Your name is :", name)
print("Your age is :", age)
print("Your GPA is :", GPA)
print("Are you enrolled :", is_enrolled)
print()

# Displaying data type of each variable using type()

print("______________Data type of variables____________")
print()

print("Data type of variable 'name' is :",type(name))
print("Data type of variable 'age' is :",type(age))
print("Data type of variable 'GPA' is :",type(GPA))
print("Data type of variable 'is_enrolled' is :",type(is_enrolled))
print()

# Concepts used in problem 1.1 :
# Variables, Data Types (String, Integer, Float, Boolean), Input, Output, type()

print("_____________________(Problem 1.2)_________________")
print()

# Problem 1.2: Temperature Converter
# Ask the user to enter temperature in Celsius (as a string). Convert it to float, then calculate
# Fahrenheit using the formula: F = (C × 9/5) + 32. Display both Celsius and Fahrenheit values.
# Also display the data type before and after conversion.

# Solution :-

# Taking input from the user :

temp = input("Enter the temperature in celsius :")                   # temp variable stores value as string
print()
print("Data type of temp variable before conversion :",type(temp))   # Printing data type of temp before conversion
temp = float(temp)                                                   # value of temp variable is converted into float
print("Data type of temp variable after conversion :",type(temp))    # printing data type of temp after conversion
fahren = (temp*9/5)+32                                               # calculating fahrenheit using formula
print()

# Displaying values

print("Temperature in celsius is :", temp)
print("Temperature in Fahrenheit is :", fahren)
print()

# Concepts used in problem 1.2: Input, Type Conversion, Type Casting, Arithmetic Operators, type()

print("_____________________(Problem 1.3)_________________")
print()

# Problem 1.3: Area and Perimeter of Rectangle
# Ask the user for the length and width of a rectangle. Calculate and display the area (length × width)
# and perimeter (2 × (length + width)). Use appropriate variable names and add comments to explain each 
# step.

# Solution :-

# Taking input from the user :

length = int(input("Enter length of rectangle : "))
width = int(input("Enter width of rectangle : "))
print()

# calculating and displaying the area of rectangle

area = length * width
print("Area of rectangle :", area)
print()

# calculating and displaying the perimeter of rectangle

perimeter = 2*(length + width)
print("Perimeter of rectangle :", perimeter)
print()

# Concepts used in problem 1.3: Concepts used: Variables, Arithmetic Operators, Input, Type Conversion, 
# Comments and Output

print("_____________________(Problem 1.4)_________________")
print()

# Problem 1.4: Even or Odd Checker
# Statement: Ask the user for a number. Check if the number is even or odd using the modulo operator (%).
# Display "Even" if the number is divisible by 2, otherwise display "Odd".

# Solution :-

# Taking input from the user :

num = int(input("Enter a number :"))
print()

# Checking if the num is even or odd using '%' operator

if num%2 == 0:
    print("Even")
else:
    print("Odd")
print()

# Concepts used in problem 1.4: Arithmetic Operators (%), Comparison Operators (==), Input, Type Conversion,
# and Output

print("_____________________(Problem 1.5)_________________")
print()

# Problem 1.5: Age Validator
# Statement: Ask the user for their age. Check if the age is greater than or equal to 18 using comparison
# operators. Display "You are an adult" if true, otherwise display "You are a minor".

# Solution :-

# Taking input from the user :

age = int(input("Enter your age :"))
print()

# Checking condition

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
print()

# Concepts used in problem 1.5: Comparison Operators (>=), Input, Type Conversion, Output

print("_____________________(Problem 1.6)_________________")
print()

# Problem 1.6: Swap Two Numbers
# Statement: Ask the user for two numbers (a and b). Swap their values using a temporary variable. Display
# the values before and after swapping. Add comments explaining the swapping logic.

# Solution :-

# Taking input from the user :

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
print()

# Displaying values before swapping

print("The value of first number before swapping :", a)
print("The value of second number before swapping :", b)
print()

# Swapping values using temporary variable

c = a   # c = 2 
a = b   # a = 7
b = c   # b = 2 => a gets b's value directly, but b gets a's value indirectly through c.
print("The value of first number after swapping :", a)
print("The value of second number after swapping :", b)
print()

# Points to ponder:
# Whenever you are going to overwrite a value that you still need later, save it somewhere first.
# That's exactly why the temporary variable c exists.
# To understand the concept of swapping, remember => Backup → Replace → Restore

# Concepts used in problem 1.6: Variables, Assignment Operators, Input, Type Conversion, Comments, Output

print("_____________________(Problem 1.7)_________________")
print()

# Problem 1.7:
# The following code is intended to swap two numbers.
# A = 10
# B = 20
# C = B => C = 20
# A = C => A = 20
# B = C => B = 20
# 1. Predict the final values of A, B, and C without running the code.
# 2. Does this code swap the values correctly?
# 3. If not, explain exactly where the logic goes wrong.
# 4. Correct the code without changing the idea of using a temporary variable.

# Solution :-

print("The final value of A, B and C will be 20 because the value of B is assigned to C "
"\n which is 20 and then the value of C (which is 20) is assigned to both A and B.")
print()
print(" No, the above code will not swap the values correctly")
print()
print("The logic goes wrong because after storing the value of B, B's value was not overwritten rather\n" \
"than that the value of A was overwritten by the value of C without storing it somewhere because this\n" \
"value of A is to be assigned to B. Now after  A = C the value of A is gone and that's why the swapping\n" \
"will not be successful")
print()

A = 10
B = 20 
C = B  # B's value is stored in C and it can be now over written with the value of A without any error
B = A  # The value of B became 10 now.
A = C  # Now value of A became 20 as A is assigned the stored value of B indirectly with the help of variable C.
print("Value of A :", A)
print("Value of B :", B)
print()

# Concepts used in problem 1.7: Variables, Assignment Operator (=) Variable Assignment, 
# Temporary Variable Variable Reassignment (Overwriting Values)

print("_____________________(Problem 1.8)_________________")
print()

# Problem 1.8: Simple Calculator
# Statement: Ask the user for two numbers and perform all arithmetic operations (addition, subtraction,
# multiplication, division, and Modulo. Display all results with proper labels.

# Solution :-

# Taking input from the user :

x = int(input("Enter 1st num :"))
y = int(input("Enter 2nd num :"))

# Arithmetic operations

print("Addition x+y =", x+y)
print("Subtraction x-y =", x-y)
print("Multiplication x*y =", x*y)
print("Division x/y =", x/y)
print("Modulo x%y =", x%y)
print()

# Concepts used in Problem 1.8: Arithmetic Operators (+, -, *, /, %), Variables, Input, Type Conversion

print("_____________________(Problem 1.9)_________________")
print()

# Problem 1.9: BMI Calculator
# Statement: Ask the user for their weight in kilograms and height in meters. Calculate BMI using the
# formula: BMI = weight / (height × height). Display the BMI value. Also check if the BMI is greater
# than 25 (overweight) using comparison operators.

# Solution :-

# Taking input from the user :

weight_in_kg = float(input("Enter your weight in kilograms :"))
height_in_m = float(input("Enter your height in meters :"))
print()

# Calculating BMI

BMI = weight_in_kg / (height_in_m * height_in_m)
print("BMI value = ", BMI)

# Checking condition

if BMI > 25:
    print("Overweight")
print()

# Concepts used in problem 1.9: Arithmetic Operators, Comparison Operators, Variables, Input,
# Type Conversion, Output

print("_____________________(Problem 1.10)_________________")
print()

# Problem 1.10: Celcius to Kelvin Converter
# Statement: Ask the user to enter temperature in Celsius. Convert it to Kelvin using the 
# formula: K = C + 273.15. Display both Celsius and Kelvin values. Display the data types of all variables.

# Solution :-

# Taking input from the user :

temp_in_celsius = int(input("Enter temperature in Celsius :"))
temp_in_kelvin = temp_in_celsius + 273.15
print()

# Displaying values

print("Temperature in Celsius :", temp_in_celsius)
print("Temperature in Kelvin:", temp_in_kelvin)
print()

# Displaying data types

print("Data type of variable 'temp_in_celsius' = ", type(temp_in_celsius))
print("Data type of variable 'temp_in_kelvin' = ", type(temp_in_kelvin))
print()

# Concepts used in problem 1.10: Variables, Arithmetic Operators, Type Conversion, type(), Input, Output

print("_____________________(Problem 1.11)_________________")
print()

# Problem 1.11: Number Comparison
# Statement: Ask the user for three numbers. Check which number is the greatest using comparison
# operators (>, <, >=, <=). Display the greatest number.

# Solution :-

# Taking input from the user :

num1 = int(input("Enter 1st num :"))
num2 = int(input("Enter 2nd num :"))
num3 = int(input("Enter 3rd num :"))
print()

# Checking the greatest number
 
if num1>num2 and num1>num3:
    print("The greatest number is :", num1)
elif num2>num1 and num2>num3:
    print("The greatest number is :", num2)
else:
   print("The greatest number is :", num3)
print()
 
# Concepts used: Comparison Operators, Variables, Input, Type Conversion, Output

print("_____________________(Problem 1.12)_________________")
print()

# Problem 1.12: Discount Calculator
# Statement: Ask the user for the original price of an item. If the price is greater than 1000, 
# apply a 15% discount. If the price is between 500 and 1000, apply a 10% discount. Otherwise,
# no discount. Calculate and display the final price.

# Solution :-

# Taking input from the user :

price = int(input("Enter price of an item :"))
print()

# Checking conditions to find discount amount and final amount

if price > 1000:
    print("You got 15% Discount!")
    discount_amount = (15/100)*price
    print("Your Discount Amount is :", discount_amount)
    final_amount = price - discount_amount
    print("Your final amount now is :", final_amount)
elif price >= 500 and price <= 1000:
    print("You got 10% Discount!")
    discount_amount = (10/100)*price
    print("Your Discount Amount is :", discount_amount)
    final_amount = price - discount_amount
    print("Your final amount now is :", final_amount)
else:
    print("You got no Discount!")
print()

# The formula for calculating discount is: 
# Discount Amount = (Discount percentage/100)*original price
# The formula for calculating final amount after discount is:
# Final Amount = Original Price - Discount Amount
# Concepts used in problem 1.12: Comparison Operators, Arithmetic Operators, Variables, Input, Type
# Conversion, Output

print("_____________________(Problem 1.13)_________________")
print()

# Problem 1.13: Profit or Loss Calculator
# Statement: Ask the user for cost price and selling price. Calculate the profit or loss. If selling
# price is greater than cost price, it's a profit. If cost price is greater, it's a loss. Display the
# amount and whether it's profit or loss.

# Solution:-

# Taking input from user:

cost_price = int(input("Enter cost price :"))
selling_price = int(input("Enter selling price :"))
print()

# Condition to check profit and loss

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit! = ", profit,"rs.")
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss! =", loss,"rs.")
else:
    print("No profit & No loss")
print()

# Concepts used in problem 1.13: Comparison Operators, Arithmetic Operators, Variables, Input, Type
# Conversion, Output

print("_____________________(Problem 1.14)_________________")
print()

# Problem 1.14: Multi-Condition Validator
# Statement: Ask the user for their age. Check if the age is between 18 and 60 (inclusive) using logical
# operators (and, or). Display "Valid age" if true, otherwise display "Invalid age".

# Solution:-

# Taking input from user:

age = int(input("Enter your age :"))

# Applying condition

if age <= 60 and age >= 18 :
    print("Valid age")
elif age > 60 or age < 18 :
    print("Invalid age")
print()

# Concepts used in problem 1.14: Logical Operators (and), Comparison Operators, Input, Type Conversion

print("_____________________(Problem 1.15)_________________")
print()

# Problem 1.15: Grade Calculator
# Statement: Ask the user for their marks (out of 100). If marks are greater than or equal to 90,
# display "A Grade". If marks are between 75 and 89, display "B Grade". If marks are between 60 and 74,
# display "C Grade". If marks are less than 60, display "D Grade".

# Solution:-

# Taking input from user:

marks = int(input("Enter your marks :"))

# Checking conditions

if marks >= 90:
    print("A Grade")
elif marks <= 89 and marks >= 75:
    print("B Grade")
elif marks <= 74 and marks >= 60:
    print("C Grade")
elif marks < 60:
    print("D Grade")
print()

# Concepts used in problem 1.15 : Comparison Operators, Logical Operators, Input, Type Conversion, Output

print("_____________________(Problem 1.16)_________________")
print()

# Problem 1.16: Voting Eligibility
# Statement: Ask the user for their age and nationality. Check if they are eligible to vote using logical
# operators. Conditions: Age must be 18 or above AND nationality must be "Pakistani" (or "Indian" or any
# country of your choice). Display appropriate message.

# Solution:-

# Taking input from user:

age = int(input("Enter your age :"))
nationality = input("Enter your nationality :")
print()
# Checking conditions

if age >= 18 and nationality == "Pakistani":
    print("You are eligible to vote")
else:
    print("You are not eligible")
print()

# Concepts used in problem 1.16: Logical Operators (and), Comparison Operators,Input, Type Conversion

print("_____________________(Problem 1.17)_________________")
print()

# Problem 1.17: Leap Year Checker
# Statement: Ask the user for a year. Check if it's a leap year using logical operators. A year is a leap
# year if it's divisible by 4 but not by 100, OR it's divisible by 400. Display appropriate message.

# Solution:-

# Taking input from user:

year = int(input("Enter a year :"))
print()

# Checking condition

if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print("Leap Year")
else:
    print("Not a leap year")
print()

# Concepts used in problem 1.17: Logical Operators (and, or), Arithmetic Operators (%), Comparison
# Operators, Type Conversion

print("_____________________(Problem 1.18)_________________")
print()

# Problem 1.18: Shopping Cart Total
# Statement: Ask the user for the price of 3 items. Calculate the total. If the total is greater than 5000,
# apply a 5% discount and display "Discount applied". Otherwise, display "No discount". Display the final total.

# Solution:-

# Taking input from user:

price1 = int(input("Enter the price of 1st item :"))
price2 = int(input("Enter the price of 2nd item :"))
price3 = int(input("Enter the price of 3rd item :"))
total = price1 + price2 + price3
print()

# Checking conditions

if total > 5000:
    discount_price = (5/100)*total
    print("Discount applied!")
    final_price = total - discount_price
    print("Final price :", final_price)
else:
    print("No discount!")
    final_price = total
    print("Final price :", final_price)
print()

# Concepts used in problem 1.18: Arithmetic Operators, Comparison Operators,Type Conversion, Output

print("_____________________(Problem 1.19)_________________")
print()

# Problem 1.19: Average Calculator
# Statement: Ask the user for 5 numbers. Calculate their sum and average. Display both. Check if the
# average is greater than 50 using comparison operators.

# Solution:-

# Taking input from user:

num1 = int(input("Enter 1st num :"))
num2 = int(input("Enter 2nd num :"))
num3 = int(input("Enter 3rd num :"))
num4 = int(input("Enter 4th num :"))
num5 = int(input("Enter 5th num :"))
print()

# Calculating sum and average

total_sum = num1 + num2 + num3 + num4 + num5
avg = total_sum/5
print("sum = ", total_sum)
print("Average = ", avg)

# Checking conditions

if avg > 50 :
    print("Average is greater than 50 !")
else:
    print("Average is less than 50!")
print()

# Concepts used in problem 1.19: Arithmetic Operators, Comparison Operators, Type Conversion

print("_____________________(Problem 1.20)_________________")
print()

# Problem 1.20: Full Integration Program (Lecture 1)
# Statement: Write a complete program that:
# Asks the user for their name, age, height in meters, and weight in kg
# Calculates BMI using formula
# Checks if they are adult (age >= 18)
# Checks if their BMI is normal (BMI between 18.5 and 24.9)
# Displays all information with proper formatting
# Shows the data type of each variable
# Uses comments to explain each section of code

# Solution:-

# Taking input from user:

name = input("Enter your name :") 
age = int(input("Enter your age :")) 
height_in_meters = float(input("Enter your height in meters :"))
weight_in_kg = float(input("Enter your weight in kilograms :"))
print()

print("---User Information---")
print()

print("Name :", name)
print("Age :", age)
print("Height :", height_in_meters, "meters")
print("Weight :", weight_in_kg, "kg")

# Calculating BMI and checking condition for BMI

print("---BMI calculation---")
print()

BMI = weight_in_kg / (height_in_meters ** 2)
print("Your BMI = ", BMI)

if 18.5 <= BMI <= 24.9:
    print("Your BMI is normal")
else:
    print("Your BMI is not normal")

# Checking conditions

print("---Age check---")
print()

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")
print()

# Displaying data types

print("---Data types---")
print()

print("Data type of variable 'name' :", type(name))
print("Data type of variable 'age' :", type(age))
print("Data type of variable 'height_in_meters' :", type(height_in_meters))
print("Data type of variable 'weight_in_kg' :", type(weight_in_kg))

# Concepts used: ALL Lecture 1 concepts (Variables, Data Types, Input, Output, type(),
# Type Conversion, Type Casting, Arithmetic Operators, Comparison Operators, Logical Operators, Comments

print("_______________________________END__________________________________________")