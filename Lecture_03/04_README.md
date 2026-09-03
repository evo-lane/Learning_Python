# Lecture 03 : Lists and Tuples

## 1. Lists in Python

### What is a List in Python ?

1. List is a built-in data type in Python.
2. A list can store values of different data types together, such as integers,
   floats, strings, booleans, and even other lists.
3. To simplify more, we can understand list data type by compairing it with
   other data types. We know that integer data type stores only integer values, float data type stores only float values and string data type stores only string values. Each data type stores only specific values. Integer data type can't store float or string values and vice versa. But list is the data type that does the opposite. List data type in Python can store the values of all other data types. It means to say that list can store the values of integer, float, string and boolean data types.
4. List has the ability to hold different data types values into a variable.
5. Lists are mutable. It means that they can be changed or modified easily.
6. Lists supports item assignment.

### Syntax of List

list_name = [value1, value2, value3]

1. First of all write the variable name means the name of your list that you want
   to create. The variable name or list name should not violate the variable naming rules. 
2. Then use assignment operator to assign values to the list
3. Then by following the syntax use square brackets [].
4. At last write your values in the the square brackets by separating them with
   commas.

### Why do we need Lists in Python ?

Suppose I want to store marks of 5 students. I can easily do it by creating 5 variables and storing values in the respective variables as given below:
```python
    marks1 = 50
    marks2 = 60
    marks3 = 70
    marks4 = 80
    marks5 = 90
```
But what if I want to store the marks of 100 students or 500 students ? Will creating 100 or 500 individual variables be convenient ? If we are dealing with large data then creating seprarte variable for each value is not a good practice and useful. Here to solve this problem lists are used. Multiple values can be storede in a single variable and they can be manipulated easily. The main purpose of list is to collect and manage multiple ordered values.

### List Indexing

1. Index means the place or position of the value.
2. Indexing is the technique by which we can work on the values on desired index.
3. We can access the value by using indexing as given below:
```python
# Create a list
first_list = [1,2,3,4,5]
# Then write the name of the list and in square brackets write the index of the value that you want to access. For example I want to access the vlue at the 1st index so I will write index number 1 in square bracket
print(first_list[1])
# As first_list[1] is giving a value back so we will directly print it
```
### Index range and Index Error

1. Suppose my list is: marks = [87, 64, 33, 95].
2. The valid indexes of my list are 0, 1, 2 and 3 which are given below:
   marks[0] = 87
   marks[1] = 64
   marks[2] = 33
   marks[3] = 95
3. The valid indexes of a list containing 4 elements are 0, 1, 2, and 3. I can
   access or mutate the values from index 0 to index 3 only. If I want to access or change the value at the 4th index Python will give an error. Because we are accessing the value beyond the limit of the list which is invalid.
4. Example code:
  ```python
  marks = [87, 64, 33, 95]
  print(marks[4])
  ```

### List Mutation

1. Mutation means change. It means that we can change or modify the values of
   our list.
2. List mutation means changing the existing values of a list. Unlike strings,
   lists support mutation. 
3. For instance my list is: marks = [87, 64, 33, 95].
4. Now in my list the value at the 3rd index is 95. If I want number 100 at
   the 3rd index I can change it by the following method:
```python
marks = [87, 64, 33, 95]
# write the name of the list and write the index of the value in square brackets whose value you want to change as I want to change 95 into 100 means I want to change the value at the 3rd index so write the index number in square brackets and then using assignment operator(=) give the new value
marks[3] = 100
print("New list :", marks)
marks[2] = "Ali"
print(marks)
# We can assign different data type values
```
### List slicing

1. Slicing means spliting the list into parts.
2. Using slicing we can access the desired parts of the list.

#### Syntax of list slicing

list_name[starting_index : ending_index]

1. Write the name of the list
2. Then write the starting index (from where you want to start)
3. Then write the ending index (where you want to end)
4. Keep in mind that the ending index is not included.
5. Example code:
```python
marks = [87, 64, 33, 95]
print(marks[0:2])
# This will print values from 0th index to 1st index excluding the last index
print(marks[0:])
# This will print values from 0th index till the end
print(marks[:4])
# This will print values from the beginning till the 3rd index
print(marks[0:3])
# This will print values from 0th index to 2nd index excluding the last index
print(marks[:])
# This will print the whole list
```
### List Methhods

Methods are specific functions to perform particular tasks. There are multiple
different list methods. Some of them are given below:

1. append() => used to add a single element at the end of the list
   1. Syntax:
    list_name.append(element) 
   2. Example code:    
```python
marks = [87, 64, 33, 95]
marks.append(100)
print(marks)
marks.append("Apple")
print(marks)
# The element can be of any data type
```
2. sort() => sort the list in ascending order
   1.Syntax:
    list_name.sort() 
   2. Example code: 
```python
marks = [87, 64, 33, 95]
marks.sort()
print(marks)
```
3. sort(reverse = True) => sort the list in descending order
   1. Syntax:
    list_name.sort(reverse=True) 
   2. Example code: 
```python
marks = [87, 64, 33, 95]
marks.sort(reverse = True)
print(marks)
```
4. reverse() => reverse the list
   1. Syntax:
    list_name.reverse() 
   2. Example code: 
```python
marks = [87, 64, 33, 95]
marks.reverse()
print(marks)
```
5. remove() => remove first occurrence of element
   1. Syntax:
    list_name.remove(element) 
   2. Example code: 
```python
num = [1, 2, 3, 1]
num.remove(1)
print(num)
```
6. pop() => removes element at specific index
   1. Syntax:
    list_name.pop(index) 
   2. Example code: 
```python
marks = [87, 64, 33, 95]
marks.pop(2)
print(marks)
```
7. insert() => insert element at specific index
   1. Syntax:
    list_name.insert(index,element) 
   2. Example code: 
```python
marks = [87, 64, 33, 95]
marks.insert(2,888)
print(marks)
```
## 2. Tuples in Python

### What is a Tuple in Python ?

1. A tuple is a sequence data type that can store multiple values of different
   data types and is immutable.
2. For Example : tuple1 = (12, 78.9, 'Coffee', [10, 4.3, 'Tea'])
3. In the above example tuple1 is holding the integer, float, string and list data
   types 
   => 12 = int data type
   => 78.9 = float data type
   => Coffee = string data type
   => [10, 4.3, Tea] = list data type

### Syntax of Tuple:

tuple_name = (value1, value2, value3)

1. Write the name of the tuple. The name of tuple should follow the variable 
   naming rules.
2. Use assignment operator to assign values to the created tuple variable
3. Then add two parentheses / round brackets
4. At last write the values in the parentheses that you want to assign to the
   tuple.

### Why do we need Tuples in Python ?

1. A tuple is used when we want to keep several related values together as one
   group and we do not want those values to be changed.
2. Tuples are used when we have multiple related values.
3. Those values naturally belong together.
4. We want to treat them as one group.
5. We want that group to stay fixed.
6. We don't want the values to be accidentally changed during the program.
7. For example:
```python
# Coordinates of a point
point = (10, 20)
print(point)
# Together 10 and 20 represent one point
```
### Tuple Indexing

1. We can access the elements of a tuple by indexing.
2. The syntax of tuple indexing is given below:
   tuple_name(index)
   => write the name of the tuple and then write the index so that the value at that index will be accessed
3. Suppose a tuple that is: tuple1 = (12, 78.9, 'Coffee', [10, 4.3, 'Tea'])
4. Example:
```python
tuple1 = (12, 78.9, 'Coffee', [10, 4.3, 'Tea'])
# accessing 'Coffee' from tuple1
print(tuple1[2])
# accessing 78.9 from tuple1
print(tuple1[1])
# accessing 12 from tuple1
print(tuple1[0])
# accessing [10, 4.3, 'Tea'] from tuple1
print(tuple1[3])
```
### Index range and Index Error of Tuple:

1. If we want to try to access an index outside the tuple's range, Python gives
  an IndexError.
2. Example:
```python
tuple1 = (12, 78.9, 'Coffee')
# The tuple has only 3 elements, so its indexes are:
# 12 → index 0
# 78.9 → index 1
# "Coffee" → index 2
# There is no index 3, so If we want to access the element at index 3 as
# given below Python gives an error
print(tuple1[3])
```

### Tuple Mutation

1. Tuple data  type is immutable.
2. It means we cannot change, modify or mutate the elements or values of tuple data
   type.
3. The values in tuple are accessible with the help of indexing but we cannot 
   change them.
4. Tuple does not support item assignment
5. Example:
```python
tuple1 = (12, 78.9, 'Coffee')
print(tuple1[0]) # allowed
tuple1[0] = 67    # Not allowed
print(tuple1[0])  # Error
```
### Tuple slicing:

1. Tuple slicing means getting a specific portion (part) of a tuple by using a 
   range of indexes.
2. Syntax of slicing is :
   tuple[start : stop] => starting index is included and ending index is excluded
3. Example:
```python
tuple1 = (10, 20, 30, 40, 50)
print(tuple1[1:4])  # 20, 30, 40
```
4. Slicing does not change the original sequence. It creates a new sequence
   containing the selected portion
5. To simplify more we can say that slicing does not modify the original tuple;
   it produces a new sliced sequence.
6. Example:
```python
tuple1 = (10, 20, 30, 40, 50)
new_tuple = tuple1[1:4]
print(new_tuple)  # (20, 30, 40)
print(tuple1)     # (10, 20, 30, 40, 50)
```
### Tuple Methods():

1. index() => return index of first occurrence of an element
   Example:
   ```python
   tup = (2, 4, 3, 4)
   print(tup.index(4))
   ```
2. count() => count how many times an element occurs in the sequence
   Example:
   ```python
   tup = (2, 4, 3, 4)
   print(tup.count(4))
   ```