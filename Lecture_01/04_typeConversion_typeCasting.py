# Topic: Type Conversion and Type Casting in Python

a = 15                
b = 15.45            
c = a + b                     # int value + float value = float value
print("Total = ", c)  

# Type conversion is done automatically by python. Integer data is converted into superior float data type.

value1 = "15"        
value2 = 10
value3 = int(value1) + value2   # string value is converted into integer value
print("Total = ", value3)

# Type casting is done manually by programmer. String data is converted into integer data type using int() function.

# a = "ali"
# b =  10
# c =  a + b
# "Ali" cannot be converted to an integer.
# Therefore type casting is not possible in this case.
