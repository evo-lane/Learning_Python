print("___________________string functions____________________")
print()

# endswith()

print("-----endswith function-----")
print()

str1 = "I am studying Python from ApnaCollege"
print("Does string ends with 'ege' :",str1.endswith("ege"))
print("Does string ends with 'pna' :",str1.endswith("pna"))
print()

# capitalize() => capitalize first letter

print("-----capitalize function-----")
print()

str2 = "i am a programmer"                
print("Capitalizing first letter :", str2.capitalize()) 
# if we want to modify original string :
str2 = str2.capitalize()
print("Capitalizing original string :", str2)
print()

# replace() => replace old character/word with new one

print("-----replace function-----")
print()


str3 = "I like books"                    
print("Original sentence :", str3)
print("Modified sentence :", str3.replace("books" , "games"))
str4 = "There is a new bakery near my house"
print("Original sentence : ", str4)
print("Replacing 'e' with 'o' :", str4.replace("e" , "o"))
print()

# find() => find index of first occurrence of character

print("-----find function-----")
print()

str5 = "I am graduate"                                
print("Index of first occurrence of 'a' :", str5.find("a"))
print("Index of first occurrence of 'graduate' :", str5.find("graduate"))
print("Index of value that doesn't exist :", str5.find("code"))
print()

# count() => counts the number of occurrences

print("-----count function-----")
print()

str6 = "We are sure they are the ones who are coming."
print("Times of occurrence of 'are' :", str6.count("are"))
print("Times of occurence of 'e' :", str6.count("e"))