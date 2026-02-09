import math

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