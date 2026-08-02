# Topic : Tuples in Python

print("____________________Tuples_________________")
print()

# round brackets are used in tuples instead of square brackets 

tup = (87, 64, 33, 95, 76)
print("Tuple :", tup)
print("Type of 'tup' :", type(tup))
print("Length of 'tup' :", len(tup))
print()

print("_______________Indexing in Tuples____________")
print()

# Indexing in tuples is same as indexing in lists
# Tuples are immutable. Modification is not allowed in tuples.
# tup[0] = 5 is invalid

print("Element at 0th index of 'tup' :", tup[0])  
print("Element at 1st index of 'tup' :", tup[1])
print("Element at 2nd index of 'tup' :", tup[2])
print("Element at 3rd index of 'tup' :", tup[3])
print("Element at 4th index of 'tup' :", tup[4])
print()

tup = (12, 34.5, "coffee")
print("tup :", tup)
print("Type of 'tup' :", type(tup))
print("Length of 'tup' :", len(tup))
print()

# Tuples can store multiple values of different data types

print("Type of 0th element of 'tup' :", type(tup[0]))
print("Type of 1st element of 'tup' :", type(tup[1]))
print("Type of 2nd element of 'tup' :", type(tup[2]))
print()

tup = ()     # It is an empty tuple which is valid
print(tup)
print()

print("_______________Slicing in Tuples____________")
print()

new_tup = (9, 23, 6.7, "Hi", 8)

# Positive indexing

print("Positive indexing :")
print(new_tup[0:])
print(new_tup[1:])
print(new_tup[:5])
print(new_tup[:4])
print(new_tup[0:3])
print()

# Negative Indexing

print("Negative indexing :")
print(new_tup[-5:-3])
print(new_tup[-1:])
print(new_tup[-4:-1])

print("_______________Method of Tuples____________")
print()

# index() => This method tells first occurrence of an element in the tuple

num_tup = (2, 3, 1, 2, "Apple", 6, 1, 8, 1, "Apple", 3, 6, 8)
print("num_tup :", num_tup)
print()
print("The first occurrence of element 8 is at index :", num_tup.index(8))
print("The first occurrence of element 6 is at index :", num_tup.index(6))
print("The first occurrence of element 3 is at index :", num_tup.index(3))
print("The first occurrence of element 1 is at index :", num_tup.index(1))
print("The first occurrence of element 2 is at index :", num_tup.index(2))
print("The first occurrence of element 'Apple' is at index :", num_tup.index("Apple"))
print()

# count() => This function tells total number of occurrence of an element in a tuple.

print("Total occurrences of element 1 are :", num_tup.count(1))
print("Total occurrences of element 2 are :", num_tup.count(2))
print("Total occurrences of element 3 are :", num_tup.count(3))
print("Total occurrences of element 6 are :", num_tup.count(6))
print("Total occurrences of element 8 are :", num_tup.count(8))
print("Total occurrences of element 'Apple' are :", num_tup.count("Apple"))
