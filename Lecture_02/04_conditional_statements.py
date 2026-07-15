print("____________________conditional statements________________")
print()

# if condition

print("---if condition---")
print()

age = 21     
if (age >= 18):                             # if(True)                         
    print("You can apply for license")      # print() will execute when if returns True
print()

# elif condition

print("---elif condition---")               # else-if
print()

light = "Green"                             # elif executes when if gives False
if (light == "Red"):
    print("Stop")
elif (light == "Green"):
    print("Go")
elif (light == "Yellow"):
    print("Ready/Wait")
print()

# difference between if & elif

print("---if vs elif---")         #else-if
print()

num = 5 

if (num > 2):                        # if will be executed multiple times
    print("Num is greater than 2")
if (num > 3):
    print("Num is greater than 3")
print()

num1 = 7

if (num1 > 8):                        # elif will be executed only when if became False
    print("Num is greater than 8")
elif (num1 < 8):
    print("Num is less than 8")
print()

num2 = 10

if (num2 > 8):                        # elif will not be executed when if gives True
    print("Num is greater than 8")
elif (num2 < 8):
    print("Num is less than 8")
print()

# else

print("---else condition---")         
print()

light = "Blue"                        # else will be executed when all if and elif became False

if (light == "Red"):
    print("Stop")
elif (light == "Green"):
    print("Go")
elif (light == "Yellow"):
    print("Ready/Wait")
else:
    print("Error")
print()

# if-else

print("---if-else---")       
print()

age1 = 14

if (age1 >= 18):
    print("Eligible")
else:
    print("Not Eligible")
print()

# nesting

print("--------nesting--------")
print()

print("---nested if---")
print()

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login Successful")
print()

print("---nested if else---")
print()

age = 16

if age >= 18:
    print("Adult")
else:
    if age >= 13:
        print("Teenager")
print()

print("---nested if elif---")
print()

age = 15

if age >= 18:
    print("Adult")
elif age >= 13:
    if age >= 15:
        print("Middle Teen")
else:
    print("Child")