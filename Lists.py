
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
