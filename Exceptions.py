

#Exceptions: Exceptions are errors that occur during the execution of a program. They can be caused by various factors such as invalid input, division by zero, or trying to access an index that is out of range. Python provides a way to handle exceptions using try-except blocks, allowing you to gracefully handle errors and prevent your program from crashing.

#Example of handling a ZeroDivisionError exception
def divide_numbers(a, b):
    try:
        result = int(a / b)  # This will raise a ZeroDivisionError if b is zero
        return result  # Return the result of the division if it is successful
    except ZeroDivisionError:  
        return "Error: You cannot divide by zero!"  # Return an error message if a ZeroDivisionError occurs
print(divide_numbers(10, 2))  # This will show the result of dividing 10 by 2, which is 5.0
print(divide_numbers(10, 0))  # This will show the error message for division by zero, which is "Error: You cannot divide by zero!"
