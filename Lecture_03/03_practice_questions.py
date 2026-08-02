# Topic : Practice Questions (Lecture_03)

print("_____________________Question (1)____________")
print()

# Question (1)
# Write a program to ask the user to enter names of their three favorite movies
# and store them in a list. 

movie1 = input("Enter your 1st favorite movie: ")
movie2 = input("Enter your 2nd favorite movie: ")
movie3 = input("Enter your 3rd favorite movie: ")

# Method 1:

list_of_movies = [movie1, movie2, movie3]
print("My fav movies list :", list_of_movies)
print()

# Method 2 => creating an empty list before

movies = []             
movies.append(movie1)   # adding each element to that list separately
movies.append(movie2)
movies.append(movie3) 
print("My fav movies list :", movies)
print()

# Method 3 => using same variable

movies = [] 
mov = input("Enter 1st movie: ")            
movies.append(mov)
mov = input("Enter 2nd movie: ")    
movies.append(mov)
mov = input("Enter 3rd movie: ") 
movies.append(mov) 
print("My fav movies list :", movies)
print()

# Method 4 => direct append

movie = []
movie.append(input("Enter first movie :"))
movie.append(input("Enter second movie :"))
movie.append(input("Enter third movie :"))
print(movie)
print()

print("_____________________Question (2)____________")
print()

# Question (2)
# Write a program to check if a list contains a palindrome of elements.
#  Hint: Use copy() method.

# Palindrome :

list1 = [1, 2, 3, 2, 1]
copy_list = list1.copy()
copy_list.reverse()

if copy_list == list1:
    print("Palindrome")
else:
    print("Not palindrome")
print()

list2 = [1, 'abc', 'abc', 1]
copy_list = list2.copy()
copy_list.reverse()

if copy_list == list2:
    print("Palindrome")
else:
    print("Not palindrome")
print()

# Not Palindrome :

list3 = [1, 2, 3]
copy_list = list3.copy()
copy_list.reverse()

if copy_list == list3:
    print("Palindrome")
else:
    print("Not palindrome")
print()

print("_____________________Question (3)____________")
print()

# Question (3)
# Write a program to count the number of students with the 'A' grade in the
# following tuple:['C', 'D', 'A', 'A', 'B', 'B', 'A']

grade_tup = ('C', 'D', 'A', 'A', 'B', 'B', 'A')
num_of_std = grade_tup.count("A")
print("Number of students with 'A' grade: ", num_of_std)
print()

# Question (4)
# Store the above values in a list and sort them from A to D.

grade_list = ['C', 'D', 'A', 'A', 'B', 'B', 'A']
grade_list.sort()
print(grade_list)
print()