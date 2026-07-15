print("_____________Multiple valid string syntaxes__________")
print()

str1 = "This is a string"      # double quotes (valid)
print(str1,"[double quotes]")
str2 = 'OxfordUniversity'      # single quotes (valid)
print(str2,"[single quotes]")
str3 = """I am a teacher"""    # triple quotes (valid)
print(str3, "[triple quotes]")
print()

print("_____________Escape sequence________________")
print()

str4 = "Hi, My name is Rose. I am a teacher in a primary school."
print(str4)
# Both sentences are printed on the same line.

str4 = "Hi, My name is Rose.\nI am a teacher in a primary school."
print(str4)
print()
# Both sentences are printed on different lines.
# \n is used to move to the next line.

print("_____________Basic string operations___________")
print()

first_str  = "Hello"           
second_str = "World"
third_str  = first_str + second_str             # concatenation
print("Concatenated string = ", third_str)
#print("Concatenated string =", first_string + second_string)
print()

length = len(third_str)
print("Length of string is :", length)          # Length of string
# print(len(third_str))
print()

a = "Mount"
b = "Everest"
c = a + " " + b    # adding space
print("String :",c)
print("Length of string :", len(c))  # space will be counted


