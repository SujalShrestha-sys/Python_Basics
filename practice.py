import math
import numbers
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
