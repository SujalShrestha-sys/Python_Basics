import math



#Functions: A function is a reusable block of code that performs a specific task. It allows you to organize your code into smaller, manageable pieces and promotes code reusability. Functions are defined using the def keyword followed by the function name and parentheses ().




def greet(name):
    print(f"Hello, {name}!")  # This function takes a name as an argument and prints a greeting message using an f-string to include the name in the output

greet("Sujal")  # This calls the greet function with the argument "Sujal" to print a personalized greeting message

#function rules:
#1. Function names should be descriptive and follow the snake_case convention (lowercase letters with underscores).

#2. Functions should be defined using the def keyword followed by the function name and parentheses.

#3. Functions can take parameters (arguments) that allow you to pass data into the function for processing.

#4. Functions can return a value using the return statement, which allows you to get a result back from the function after it has completed its task.

#5. Functions should be called (invoked) to execute the code within the function and perform the desired task.


#Function with return value
def square(number):
    return number * number  # This function takes a number as an argument and returns the square of that number by multiplying it by itself


result = square(2)  # This calls the square function with the argument 5 and stores the returned value in the variable result

print(result)  # This shows the result of squaring the number 5, which is 25


#Function with multiple parameters
def calculate_area(length, width):
    return length * width  # This function takes two parameters, length and width, and returns the area by multiplying them together

area = calculate_area(5, 3)  # This calls the calculate_area function with the arguments 5 and 3 and stores the returned value in the variable area
print(area)  # This shows the calculated area based on the provided length and width, which is 15


#Keyword arguments
def greet(name, greeting):
    print(f"{greeting}, {name}!")  # This function takes two parameters, name and greeting, and prints a personalized greeting message using an f-string to include both the greeting and the name in the output

greet(name="Sujal", greeting="Hi")  # This calls the greet function using keyword arguments to specify the values for name and greeting, resulting in a personalized greeting message being printed

#exercise: 
# Create a function that takes a list of numbers as input and returns the average of those numbers.

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # Return 0 if the list is empty to avoid division by zero
    total = sum(numbers)  # Calculate the sum of the numbers in the list
    average = total / len(numbers)  # Calculate the average by dividing the total by the number of elements in the list
    return average  # Return the calculated average

numbers = [10, 20, 30, 40, 50]  # Example list of numbers

average_result = calculate_average(numbers)  # Call the calculate_average function with the list of numbers and store the result in average_result

print(f"The average of the numbers is: {average_result}")  # This shows the calculated average of the numbers in the list, which is 30


#creathing a reusable function to calculate the area of a circle given its radius

def calculate_area_of_circle(radius):
    area = round(math.pi * radius ** 2, 2)  # Calculate the area of a circle using the formula A = πr^2, where math.pi provides the value of π and radius is squared
    return area  # Return the calculated area
radius = 2 
area_of_circle = calculate_area_of_circle(radius)  # Call the calculate_area_of_circle function with the radius and store the result in area_of_circle
print(f"The area of the circle with radius {radius} is: {area_of_circle}")