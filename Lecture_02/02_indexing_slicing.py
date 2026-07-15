print("_____________indexing___________")
print()

continent = "Asian Continent"                        # accessing desired characters using str[] 
print("Character on the 3rd index :", continent[3]) 
str1 = "My name is charlie"
str2 = str1[6]            
print("Character on the 6th index :", str2)
print("Character on the 0th index :", str1[0])
print("Character on the 7th index :",str1[7], "(space)")
print()
              
print("_____________slicing___________")
print()

text = "Asian Continent"
sliced_str = text [6 : 10]                  # syntax => string name [starting index : ending index]
print("Sliced string 1 : ", [sliced_str])   # ending index will not be included
sliced_str = text [0 : 5] 
print("Sliced string 2 : ", [sliced_str])
sliced_str = text [6 : 15]                  # text[6 : len(text)] is valid because len(text) = 15
print("Sliced string 3 : ", [sliced_str])
print()
print("Leaving ending index empty : ")
print(text[1:]) #[1:15]                      # Leaving the end index empty means "go till the end".
print()
print("Leaving starting index empty : ")
print(text[:12]) #[0:12]                     # Leaving the start index empty means "start from the beginning".
print()

print("_____________Negative index___________")
print()

# Negative indexing starts from the end of the string.
word = "Apple"
print(word[-3 : -1])
print(word[: len(word)])
print(word[-6 : ])