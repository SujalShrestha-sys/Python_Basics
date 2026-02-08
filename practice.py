import math
course= "python for beginners"
#        01234567890123456789



#print(f'The length of the word "{course}" is {len(course)}')
#print(course[0]);
#print(course.find('Beginners'));
#print(course.replace("Beginners", "Absolute Beginners").upper())


#SLICING
#print(course[0:3])
#print(course[:])
#print(course[1:])
#print(course[:5])
#print(course[1:5])
#print(course[1:5:2])  [start:stop:step]



# BOOLEAN METHODS
#isAvailable = 'Python' in course
#print(isAvailable)



#isAvailable = 'beginners' in course
#print(isAvailable)



#FIND METHODS
#name = 'Jennifer'
#print(name.find('n'))



#Index Methods
#name='Samuel Smith'
#print(name.index('u'))




#title() : method capitalizes the first letter of each word in the string
#print(course.title())




#strip() : method removes any leading and trailing whitespace from the string
#name = "   John Doe   "
#print(name.strip())




#split() : method splits a string into a list of substrings based on a specified delimiter
#sentence = "Hello, how are you?"
#print(sentence.split())  # Default delimiter is whitespace
#print(sentence.split(','))  # Split using comma as delimiter  




#replace() : method replaces all occurrences of a specified substring with another substring
#greeting = "Hello, World!"
#print(greeting.replace("Hello", "Hi"))  # Output: "Hi, World!"

#Floor, Ceil, and Square Root


#Floor : The floor of a number is the largest integer less than or equal to that number. 
# For example,
#print(math.floor(3.7))  # Output: 3


#Ceil : The ceil of a number is the smallest integer greater than or equal to that number. 
# For example,
#print(math.ceil(3.2))   # Output: 4


#Square Root : The square root of a number is a value that, when multiplied by itself, gives the original number.
#print(math.sqrt(16))    # Output: 4.0  



#if else statements

'''
is_hot = False
is_cold = False

if is_hot == True:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day") 
    
'''

"""

HousePrice = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = int(0.1 * HousePrice)
    print(f"Down Payment: Nrs {down_payment}")
else:
    down_payment = int(0.2 * HousePrice)
    print(f"Down Payment: Nrs {down_payment}")

"""

#logical operators
'''
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

'''

#combine logical operators
"""
has_high_income = True
has_good_credit = True
has_criminal_record = False 

if has_high_income and has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:    
    print("Not eligible for loan")

"""

#comparison operators
'''
temperature = 30
if temperature >= 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's a nice day")

'''


#name length validation
'''
name_length = 51
if name_length < 3:
    print("Name must be atleast 3 characters long")
elif name_length > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")

'''

'''
#name length validation
name = 'Su'
print(len(name))

if len(name) < 3:
    print("Name must be atleast 3 characters long")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")

'''


#upper() : method converts all characters in a string to uppercase
#lower() : method converts all characters in a string to lowercase
#title() : method capitalizes the first letter of each word in the string


'''
weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if unit.title() == 'L':
    converted_weight = int(weight) * 0.453592  # Convert pounds to kilograms
    rounded_weight = round(converted_weight,2)  # Round to 2 decimal places
    print(f"You are {rounded_weight} kilos")
elif unit.title() == 'K':
    converted_weight = int(weight) * 2.20462  # Convert kilograms to pounds
    rounded_weight = round(converted_weight,2)  # Round to 2 decimal places
    print(f"You are {converted_weight} pounds")
else:
    print("Invalid unit. Please enter 'L' for pounds or 'K' for kilograms.")

'''


#While loops

"""
digit = 1
while digit < 5:
    print(digit)
    digit += 1

    """


"""
while True:
    command = input("Type 'exit' to quit: ")

    if(command.lower()  == 'exit'):
        break
 """  
"""

import random

#Guessing game
secret_number = random.randint(1, 10)
guess_count = 0
guess_limit = 2

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    if guess < secret_number:
        print("Too low")
    elif guess == secret_number:
        print("You won!")
        break
    elif guess > secret_number:
        print("Too high")
    guess_count += 1
else:
    print(f"Sorry, you failed:( The secret number was {secret_number}")

"""

#Car simulation Program
"""
command = " "
started = True

while True:
    command = input(">>> ").lower()
    if(command == "start"):
        if(started):
            print("Car is already started:)")
        else:
            started = True
            print("car Started...Ready to go!")
    elif(command == "stop"):
        if not started:
            print("Car is already stopped:)")
        else:
            started = False
            print("car Stopped.")
    elif(command == "help"):
        print("start - to start the car stop - to stop the car quit - to exit")
    elif(command == "quit"):
        break
    else:
        print("Sorry, I don't understand that")

"""

#For loops
"""
numbers = [1,2,3,4,5]
for number in numbers:
    print(number * '*')  # This shows how for loops work by printing asterisks for each number in the list

"""

"""

names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
for name in names:
    print(name + " is a student")  # This shows how for loops work by printing a message for each name in the list

"""

#using the range function

"""
for number in range(5):
    print(number)  # This shows how the range function works by printing numbers from 0 to 4

"""

"""
for number in range(1,11):
    print(number)  # This shows how the range function works by printing numbers from 5 to 9


for i in range(1, 11, 2):  # Start=1, Stop=11 (exclusive), Step=2
    print(i)  # This shows how the range function works by printing odd numbers from 1 to 10        

"""

"""
price = [10, 20, 30]
total = 0

for p in price:
    total += p
    print(total)  # This shows how to calculate the total price by iterating through the list of prices and adding them up  

"""

#Nested loops

#matrix concept : A matrix is a two-dimensional array of numbers arranged in rows and columns. It is a fundamental data structure in mathematics and computer science, used to represent and manipulate data in various applications such as linear algebra, computer graphics, machine learning, and more. Each element in a matrix can be accessed using its row and column indices.

'''
example_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in example_matrix:
    for item in row:
        print(f"Row: {example_matrix.index(row)}, Item: {item}")  # This shows how nested loops work by iterating through each row of the matrix and then through each item in the row to print all elements of the matrix

'''

"""

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")  # This shows how nested loops work by printing all combinations of x and y values within the specified ranges

"""

#list comprehensions
'''
names = ["John", "Bob", "Mosh", "Sarah", "Mary"]

'''

'''

print(names)  # This shows the original list of names
print(f"First name: {names[0]}")  # This prints the first name in the list (index 0)

'''

'''
names[0] = 'Sujal'  # This changes the first name in the list to "Sujal"


print(names)  # This shows the updated list of names after changing the first name  


print(names[:3])  # This shows the first three names in the list using slicing


print(names[::2])  # This shows every second name in the list using slicing with a step of 2


print(names[1::2])  # This shows every second name starting from the second name (index 1) using slicing with a step of 2

'''
'''
names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
first_names = [name[0] for name in names]  # This creates a new
print(first_names)  # This shows the new list of first names extracted from the original list using a list comprehension

'''

#Program to find the largest number in a list
'''
numbers = [3, 6, 2, 8,10, 4]
max_number = numbers[0]  # Initialize max_number to the first element of the list

for number in numbers:
    if number > max_number:
        max_number = number  # Update max_number if a larger number is found
    
    if number < max_number:
        print(f"{number} is smaller than {max_number}")  # This shows the comparison of each number with the current max_number during the iteration

print(f"The largest number is: {max_number}")  # This shows the largest number found in the list after iterating through all the numbers

'''
#2D lists (lists of lists)
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(f"Row: {matrix.index(row)}, Item: {item}")  # This shows how to iterate through a 2D list (matrix) using nested loops to print each item in the matrix

'''

#example No 2
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(len(matrix))  # This shows the number of rows in the matrix (length of the outer list)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"Row: {i}, Column: {j}, Item: {matrix[i][j]}")  # This shows how to iterate through a 2D list (matrix) using nested loops with index-based access to print each item along with its row and column indices
'''


#List methods

""" 
numbers = [3, 6, 2, 8, 10, 4]
numbers.append(12)  # This adds the number 12 to the end of the list
print(numbers)  # This shows the updated list after appending a new number


numbers.insert(0, 0)  # This inserts the number 0 at index 0 (the beginning of the list)
print(numbers)  # This shows the updated list after inserting a new number at the beginning


numbers.remove(2)  # This removes the first occurrence of the number 2 from the list
print(numbers)  # This shows the updated list after removing the number 2


numbers.pop()  # This removes the last item from the list and returns it
print(numbers)  # This shows the updated list after popping the last item


numbers.sort()  # This sorts the items in the list in ascending order
print(numbers)  # This shows the updated list after sorting the items in ascending order    


numbers.sort(reverse=True)  # This sorts the items in the list in descending order
print(numbers)  # This shows the updated list after sorting the items in descending order


numbers.extend([1, 2, 3])  # This adds multiple items (1, 2, and 3) to the end of the list
print(numbers)  # This shows the updated list after extending it with multiple new items


numbers.count(3)  # This counts the number of occurrences of the number 3 in the list
print(numbers.count(3))  # This shows the count of how many times the number 3 appears in the list


numbers.index(2)  # This returns the index of the first occurrence of the number 2 in the list
print(numbers.index(2))  # This shows the index of the first occurrence of the number 2


print(6 in numbers)  # This checks if the number 50 is present in the list and returns True or False


print(numbers.copy())  # This creates a shallow copy of the list and returns it
print(numbers)  # This shows the original list after copying it, which remains unchanged


numbers.clear()  # This removes all items from the list, making it empty
print(numbers)  # This shows the updated list after clearing all items, resulting in an empty list  

"""


#A program to remove duplicates from a list
'''
numbers = [1, 2, 3, 2, 4, 1, 5]

unique_numbers = list(set(numbers)) # This converts the list to a set to remove duplicates and then converts it back to a list

print(unique_numbers)  # This shows the list of unique numbers after removing duplicates from the original list
'''

'''
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)  # This iterates through the original list and appends only unique numbers to the new list
print(unique)  # This shows the list of unique numbers after iterating through the original list and collecting unique values

'''

#Tuples: A tuple is an ordered, immutable collection of items. It is similar to a list but cannot be modified after it is created. Tuples are defined using parentheses () and can contain elements of different data types.

'''
tuple_example = (1, 2, 3, 4, 5)

print(tuple_example)  # This shows the original tuple
print(tuple_example[0])  # This shows the first element of the tuple (index 0)


#Unpacking: Unpacking is a feature in Python that allows you to assign the elements of a collection (like a list or tuple) to multiple variables in a single line of code. It is a convenient way to extract values from a collection and assign them to individual variables.

coordinates = (10, 20, 30)
x, y, z = coordinates  # This unpacks the tuple into individual variables x, y, and z

print(f"x: {x}, y: {y}, z: {z}")  # This shows the values of x, y, and z after unpacking the tuple

'''
#Dictionaries: A dictionary is an unordered collection of key-value pairs. It is a data structure that allows you to store and retrieve values based on unique keys. Dictionaries are defined using curly braces {} and consist of key-value pairs separated by colons (:).

'''
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
}

print(person)  # This shows the original dictionary


print(person["name"])  # This shows the value associated with the key "name" in the dictionary


print(person.get("age"))  # This shows the value associated with the key "age" using the get method, which returns None if the key is not found


print(person.get("country", "Not Found"))  # This shows the value associated with the key "country" using the get method with a default value of "Not Found" if the key is not found

'''


#A program to count the frequency of each word in a given text
"""
text = "hello world hello sujal hello python"
word_count = {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1  # This increments the count of the word if it already exists in the dictionary
    else:
        word_count[word] = 1  # This initializes the count of the word to 1 if it is not already in the dictionary

    print(word_count)  # This shows the dictionary containing each word and its corresponding frequency count after iterating through the text and counting the occurrences of each word
"""

#Program - 2

'''
words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5
}

input_word = input("Enter a number in words (e.g., 'one', 'two', etc.): ").lower()
if input_word in words:
    print(f"The numeric value of '{input_word}' is: {words[input_word]}")  # This shows the numeric value corresponding to the input word if it exists in the dictionary
else:
    print("The word is not in the dictionary.")  # This shows a message if the input word is not found in the dictionary    

print("End of the program.")

'''

#program 3
'''
numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five"
}

input_number = int(input("Enter a number between 1 and 5: "))
if input_number in numbers:
    print(f"The word for number {input_number} is: {numbers[input_number]}")
else:
    print("The number is not in the dictionary.")
    
print("End of the program.")
'''



