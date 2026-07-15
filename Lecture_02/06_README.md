# Lecture 02 – Strings & Conditional Statements

## 1. Introduction to Strings

### What is a string?
 1. A string is a sequence of characters.
 2. Anything written between quotation marks can be referred to as a string whether it is a single
    character, special symbol, space, or a sentence.
 3. Strings are immutable. They cannot be changed by indexing.
 4. Strings can contain letters, numbers, spaces, and symbols.

### Creating Strings
 1. Strings can be created by writing characters enclosed in quotation marks.
 2. There are three valid ways to write strings: single quotes (' '), double quotes
    (" ") and triple quotes (""" """)
    Example: 'Hello' "Hello" """Hello"""
 3. The most commonly used string style is double quotes.

 ### Why are there three ways to write a string?
 1. To improve readability and convenience.
 2. Single and double quotes are used to write short text
 3. Triple quotes are mainly used to write multi-line strings.
 4. If you want to write (He said, "Hello") in a string you have to use single quotes. Double quotes
    cannot be used directly here because Python will think the string ends at the second double quote.
 5. Example:
    str1 =  " He said, "Hello" " 
    In the above example Python will consider (He said,) as a string and remaining text will cause error
    so instead we can write it as
    str1 = ' He said, "Hello" '
 
 ## 2. Escape Sequence
  1. Escape sequences are special character combinations that start with a backslash (\) and are used for 
     formatting text.
  2. There are multiple escape sequences that are used for different formatting styles.
  3. Some escape sequences are given below:
     => '\n' is used to move to the next line
     example:
     ```python
     print("Hello\nWorld")
     ```
     => '\t' is used to add a tab space 
     ```python
     print("My\tBook")
     ``` 
     => '\\' is used to print a single backslash
     ```python
     print("MainFolder\\SubFolder\\MyData")
     ```
     => \' is used to print a single quote
     ```python
      print("I\'m having a good day today")
     ```
     => '\b' is used to print backspace which moves one position backward (backspace)
     ```python
     print("MyNamee\b")
     ```
## 3. Basic String Operations

###  Concatenation (+)
  1. Concatenation simply means joining two or more strings together using the
    (+) operator.
  2. Example: 
  ```python
  str1 = "Ox"
  str2 = "ford"
  str3 = str1 + str2
  print(str3)
  ```

### len()
 1. len() or length function is used to find the length of a string.
 2. Finding the length of a string means counting all the characters of a string including the letters,
    spaces and special symbols.
 
 3. Example:
 ```python
  name = "Baba Yaga"     # total characters in name including space are 9 so the length will be 9
  print(len(name))
  ``` 
## 4. Indexing

### What is an index?
 1. Index means the position of the character in a string
 2. In Python, indexing starts from 0 instead of 1.
 3. Special symbols, spaces also have indexes.
 4. There are two types of indexing 
 => Positive indexing:
    It starts from the beginning and the numbering starts from 0 onwards. All numbers or positions
    assigned are in positive numbers.
 => Negative indexing:
    It starts from the end of a string and negative indexing begins with -1 and so on. All numbers assigned
    are negative.
 5. In indexing we normally use positive indexing.
 6. Through indexing we can access desired characters or indexing allows us to access individual
    characters in a string.
    Example:
    ```python
    str2 = "My school"
    print(str2[3])
    ```
 7. Suppose a string a = "Ali", then indexing will be like 
    a[0] = "A"
    a[1] = "l"
    a[2] = "i"
 8. Item assignment is probihited for strings.
 9. using strings characters can be accessed but cannot be manipulated

## 5. Slicing

### What is slicing?
  1. Slicing means breaking the string into parts.
  2. Through slicing we can access the desired part of a string.
  3. Slicing is an important concept and is widely used in Python programming.

### Syntax
   string[starting index : ending index]

 1. While slicing, the ending index is excluded. It means the character on ending index is not included.
 2. If we leave the starting index empty python will automatically consider that we want to start from the 
    beginning (from 0)
 3. If we leave the ending index empty python will automatically consider that we want to go till the end
    of the string
 4. len(str) returns the total number of characters in a string.
 5. Example:
    ```python
    str3 = "My coding book"       # both print() are valid and gives the same output result
     print(str3[0:14])
     print(str3[0:len(str3)])
     ```
## 6. Negative indexing
 1. Negative indexing is used mainly in slicing rather than in indexing
 2. It starts from the end of the string from -1 onwards.
 3. Negative indexing lets you access or slice a string from the end instead of the beginning.
 4. Negative indexing is useful when we don't know the length of the string.
    For Example if i want to access the last character of the string:

   ```python
   text = "Python"
   print(text[-1])
   ``` 
    We easily accessed the last character of the string using negative indexing. Without negative indexing
    we have to do something like

   ```python
   text = "Python"
   print(text[5]) 
   ``` 
   This only works if we already know the length of the string
 5. Negative indexing is useful when you want characters from the end or when you don't know the string's
    length. It often makes the code shorter and easier to read. 

## 7. String Functions
   1. These are built in functions that are used to perform specific task.
   2. There are many string functions. Some of them are given below

### endswith()
 1. This function helps to check with which character our string ends
 2. The answer of endswith() function will be a boolean value ie., True/False
 3. The syntax of endswith() function is 
    string name.endswith("character you want to check")

 4. Example:
   ```python
   name = "Daniel Markon"
   print(name.endswith("kon"))   # Result will be True because our strings ends with 'kon'
   ```
### replace()
 1. Using this function we can replace old character or set of characters with new ones.
 2. The syntax of replace function is 
    string name.replace("old character" : "new character")

 3. Example:
    ```python
    name = "I like to eat apples"
    print(name.replace("apples" : "pears"))
    ```

### capitalize()
  1. This function of string capitalize the first character of the string
  2. The syntax is
     string name.capitalize()

  3. Example:
    ```python
    name = "i am Jasper"
    print(name.capitalize())
    ```

### find()
  1. This function is used to find the initial index of the first appearence of character in string
  2. It means at which index the character came for the very first time
  3. Syntax of find() function is:
     string name.find("the character whose first index you want to find")

  4. Example:
  ```python
  text = "I am Silva from Paris"
  print(text.find("m"))
  ```

### count()
  1. This function counts the occurrences of a character in a string
  2. It means it counts how many times the character came in a string
  3. The syntax is
     string name.count("The character whose occurrence you want to count")
  
  4. Example:
    ```python
    text1 = "I belong to African continent"   # o came three times in text1
    print(text1.count("o"))
    ```
   
## Conditional statements
   1. Conditional statements are used to check different conditions and to make decisions based on those
      conditions
   2. There are three types of conditions
   => if
   => elif
   => else
   ### if condition
      1. 'if' will execute only when the given condition is True
      2. If the condition is False 'if' will not be executed
      3. Multiple 'if' conditions can be used and all of them will be checked one by one
      4. 'if' is used for simple conditions
      5. Syntax :
          if (condition):
               statement
      
      6. Example:
        ```python
        is_swimming = True
        if(is_swimming):
             print("You can go near the river")
         ```
   ### elif condition (else-if)
      1. elif will be executed only when 'if' became False
      2. It is used where multiple conditions are used
      3. syntax: 
          elif (condition):
              statement

      4. Example:
        ```python
        is_student = False
        is_teacher = True
        if (is_student):
             print("You can enter the office")
        elif(is_teacher):
             print("You cannot enter the office")
         ```

   ### else condition
      1. else is executed when all the other conditions became False.
      2. else has a simple syntax
           else:
               statement

      3. Example:

         For instance you can access the system if your numeric password is correct or if your alphabetic
         password is correct but what is both passwords entered are wrong. In that case else will be executed

         ```python
           numeric_password = 799
           alphabetical_password = "bhi"
           if  numeric_password == 1234 :
                print("Access granted")
           elif alphabetical_password == "abcd" :
                print("Access granted")
            else:
                print("Access failed")
         ```
## Nesting conditions
   1. Nesting means condition within a condition
   2. It is used when there appears a condition within another condition
   3. There are various possible combinations to use a condition within another condition
   4. Syntax
      if condition1:
        Runs if condition1 is True
          if condition2:
            Runs if both condition1 and condition2 are True
          else:
            Runs if condition1 is True but condition2 is False
      else:
        Runs if condition1 is False

   5. Example:
      ```python
       age = 20
       has_id = True
       if age >= 18:
          if has_id:
             print("Entry allowed")
          else:
            print("ID required")
       else:
         print("You are underage")
      ```
      