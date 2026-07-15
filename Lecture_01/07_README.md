# Lecture 1 : Introduction to Python

## What is a program?

A program is a set of instructions given to the computer to perform a specific task or to solve a problem.
The program is given as input to the computer to gain desired results in return
Programs are written in different programming languages like C, C++, Java, Python etc.

## What is a programming Language? 

A Programming language enables us to communicate with the computer and give instructions (programs) to it. 
Instructions given in High Level Programming Languages like python are translated into low level language with the help of the respective compiler or interpreter. 
Compiler converts the source code into machine code as a whole while interpreter converts the source code into machine code line by line. 
This feature of interpreter makes it more flexible and easier to debug that's why python uses an interpreter instead of a compiler.

## What is Python?

Python is a High Level programming language developed by a Dutch programmer Guido van Rossum.
It provides a beginner friendly environment to interact with the computer.
It is open-source.
Python is portable. The same python code can run on Windows, macOS and Linux

## Features of Python

1. Easy to learn
2. Closer to English
3. Free resource
4. Widely used and loved language

## Applications of Python

1. Web development
2. AI
3. Machine Learning
4. Data science
5. Game Development
The scope and domain of Python is very vast. It is used through out the world and in tech industry.

## variables in python

A variable is a named memory location in computer.
Variables are identifiers used to store values of different data types.
In simple terms variables can be referred as containers to hold values. 
Values are assigned to variables and these values can be changed or updated as the name variable itself means "changeable". 
In addition to this the value of a variable can be given by the programmer or it can be taken as input from the user.

## Rules for naming variables

1. The name of a variable contains alphabets (A_Z, a_z), digits(0_9) and underscore(_).
2. Special symbols and space is not allowed
3. The name of a variable must start with an underscore or an alphabet
4. Python is a case sensitive language so "age" and "Age" are two different variable names.
5. Keywords/reserved words cannot be used as variable names.
6. Valid variable names are age2, _myName, class_7 etc.
7. 8tiger, home&2, my marks, are invalid variable names.

## Identifiers in python

Identifiers are names you give to something so that python recognize it. Identifiers are the names given to the variables, functions, class and objects so that they can be used in python.
Every variable is an identifier but every identifier is not a variable.
The naming rules of identifier are the same as the naming rules of a variable.
34junaid, &bear, my car are invalid identifiers
myFather, call11, his_watch are valid identifiers

## Keywords/Reserved words in python

Keywords are special built in words in python library which are used to perform specific tasks.
In simple terms we can say that this group of words is booked and exclusively is for python only and the programmer can't use it anywhere except for the purpose the word is made for.
They cannot be used as variable or identifier names.
True, False, if, and, or, not are examples of reserved keywords.

## Character Set in python

In python these following character sets are used 
1. Alphabets A_Z and a_z
2. Digits 0_9
3. All special symbols available on keyboard like !,@,#,$,%,^,&,*
4. Whitespaces like tab, blank space, carriage return, form feed, newline
5. Python can process all ASCII and Unicode characters

## Comments in python

Comments are instructions that are ignored by the python interpreter.
Programmers use comments to explain their code and the logic behind it.
"#" symbol is used to add single line comments
Triple quotes (''' ''' , """ """) can be used to write multi-line text but they are not actual multi-line comments; they are string literals that are ignored by Python when they are not assigned to a variable.

## Data Types in python

Data type means the type of data a value possesses. It can be numeric, decimal, alphabetical etc
There are different types of data in python. 
Different data types require different amounts of memory.
Some basic data types are listed below:

### 1. int data type

Integer data type holds all the values on number line. It holds all positive and negative numbers including zero.
Example: -78, 45, 0

### 2. float data type

Float data type contains all the decimal values whether they are negative or positive.
Example: 34.56, -98.7, 0.0

### 3. str data type

Every value can be referred as a string data type if it is in between inverted commas.
No matter if the value in between the commas is a float, alphabet, integer, character or a special symbol it will be referred as a string data type.
Example: "12", "-89", "56.7", "-5.3", "0", "0.0", "ali", "$dollar", "My favorite book"
strings can be written in single quotes (''), double quotes (" ") and in triple quotes (''' ''') also.

### 4. bool data type

Boolean data type gives True value while the condition is True and it gives False when the condition is False. No matter whether the condition is made using relational operators or using logical operators.
Example: 
```python
a = 7 
print(a<7)
```
output: False

### 5. None data type

None data type is used in variable where the value is not assigned yet or we want to assign the value later
Example: address = None

### type() function

type() function is a built in function that is used to perform a specific task and that specific task is to check the data types of values
Example: Name = "Ali", age = 32, marks = 67.5, address = None
         print(type(Name))      output will be <class str>
         print(type(age))       output will be <class int>
         print(type(marks))     output will be <class float>
         print(type(age>18))    output will be <class bool>
         print(type(address))   output will be <class 'NoneType'>

## Operators in Python

Operators are symbols used between operands to perform functions.
There are total 7 operators in python some of them are given below

### 1. Arithmetic operators

Arithmetic operators are used to perform basic mathematical functions.
  1. (+) Addition operator is used to add values.
  2. (-) Subtraction operator is used to subtract values.
  3. (*) Multiplication operator is used to multiply values.
  4. (/) Division operator is used to divide values.
  5. (%) Modulus operator is used to find remainder of values.
  6. (**) Exponential operator is used to find power of a value.

### 2. Comparison/Relational Operators

Comparison or relational operators are used to compare two values.
 The comparison operators are:
   1. Greater than operator               (>)
   2. Smaller than operator               (<)
   3. Greater than or equal to operator   (>=)
   4. Smaller than or equal to operator   (<=)
   5. Equal to operator                   (==)
   6. Not Equal to operator               (!=)
Values are compared using these different relational operators and answer will be in boolean values depending upon the condition used on the values.

### 3. Logical Operators

Logical operators are used for conditioning and logical analysis.
  1. 'and' logical operator is used between values and gives True when all the conditions are true. It will give False when any of the given condition is false
  2. 'or' logical operator gives True when any of the given condition is true. It gives False when all the given conditions are false.
  ('and' and 'or' works opposite to each other.)
  3. not logical operator is used to give the opposite result of a given condition
  
### 4. Assignment operators

Assignment operators are used to assign values to variables.
The value on the right side is assigned to the left side.
1. (=)  This operator is used to directly assign a value
2. (+=) This operator is used to assign a value after addition
3. (-=) This operator is used to assign a value after subtraction
4. (*=) This operator is used to assign a value after multiplication
5. (/=) This operator is used to assign a value after division
6. (%=) This operator is used to assign a value after finding remainder
7. (**=) This operator is used to assign a value after finding exponent 
8. Firstly the simple arithmetic operation is performed after that the new value is assigned to the  variable.
9. Example: 
   ```python
   a = 5
   a += 4    #(This means a = a + 4)
   print(a)
   ```
   output: 9

## Type Conversion

Type conversion is the process of converting an inferior data type value into a superior data type value when both values are engaged in some sort of calculation process.
The result of adding, subtracting, multiplying an integer with float will always be a float.
This is done automatically by the python interpreter according to the data type hierarchy from the lower data type to the higher data type.
Example: 
```python 
a = 7
b = 7.34
print(a+b)
```
output: 14.43

## Type casting

This process of converting data types of values is done manually by the programmer when two different category data types are encountered with each other.
If we want to add a string num1 = "12" into an integer num2 = 10 we have to convert the data type of "12" which is string into integer data type as following:
```python
num1 = "12"
num2 = 10
num3 = int(num1)+num2
print(num3)
```
or we can do this:
``` python
num1 = int("12")
num2 = 10
num3 = num1 + num2
print(num3)
```
alternating syntax we can do this also:
```python num1 = "12"
num2 = 10
print(int(num1)+num2)
```

There is another case where a string cannot be added to an integer and no manual data conversion is possible.
Example: name = "Ali"
         age = 2
         here 2 cannot be added to Ali 

## input in python

input() function is a built in function in python which is used to take input from the user.
Sometimes the programmer assign values to the variables himself but sometimes we ask the user to enter the value as input.
The resulting value of input() function will always be a string
We don't need string all the time. Sometimes we need a float and sometimes we need an integer
For that purpose we manually change the data type of the value
Example:
 age = input("Enter age:" )
 Here the age will be entered as a string
 age = int(input("Enter age:" ))
 Now in the above line the age will be entered as an integer.

## Acknowledgement 

This repository was created while studying **Lecture 1** of the Python Full course by **Shradha Khapra (Apna College)** on YouTube.
The code examples follow the concepts taught in the lecture, while the explanations, notes, and code comments are written by me in my own words according to my understanding.

## Learning Resource

YouTube channel link: https://youtube.com/@shradhakd?si=4b50O-lVe0Zf7bcH
YouTube video link: https://youtu.be/t2_Q2BRzeEE?si=hbBs8VBtPJkVM58s

## Note for the Reader

Feedback and suggestions are always appreciated. If you notice any mistakes or think something can be explained or implemented in a better way, feel free to share your suggestions.
