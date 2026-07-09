# Topic: Operators in Python

# Arithmetic Operators

a = 10
b = 5

add = a + b
print("Sum:", add)     # Addition +
sub = a - b
print("Sub:", sub)     # Subtraction -
mul = a * b
print("Mul:", mul)     # Multiplication *
div = a / b
print("Div:", div)     # Division /
mod = a % b
print("Mod:", mod)     # Modulus %
pow = a ** b
print("Pow:", pow)     # Power **

# Comparison/Relational Operators

c = 67
d = 45

print("Equal to:", c == d)                  # Equal ==
print("Not equal to:", c != d)              # Not equal !=
print("Greater than:", c > d)               # Greater than >
print("Less than:", c < d)                  # Less than <
print("Greater than or equal to:", c >= d)  # Greater than or equal to >=
print("Less than or equal to:", c <= d)     # Less than or equal to <=
                                          
# Answer will be a boolean value (True or False)

# Logical Operators

age = 32
if age > 18 and age < 65:
    print("Eligible to work")               # Logical AND
age = 70 
if age < 18 or age > 65:
    print("Not Eligible to work")           # Logical OR
print(not(age > 18 and age < 65))           # Logical NOT

# Assignment Operators

a = 87
b = 54

a += b
print("add =", a)    # a = a + b
a -= b
print("sub =", a)    # a = a - b
a *= b
print("mul =", a)    # a = a * b
a /= b
print("div =", a)    # a = a / b
a %= b
print("mod =", a)    # a = a % b
a **= b
print("pow =", a)    # a = a ** b
