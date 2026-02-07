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

example_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in example_matrix:
    for item in row:
        print(f"Row: {example_matrix.index(row)}, Item: {item}")  # This shows how nested loops work by iterating through each row of the matrix and then through each item in the row to print all elements of the matrix


"""

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")  # This shows how nested loops work by printing all combinations of x and y values within the specified ranges

"""