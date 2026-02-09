
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
#A program to demonstrate tuple unpacking with a function that returns multiple values

def get_coordinates():
    return (10, 20, 30)  # This function returns a tuple containing three coordinate values
x, y, z = get_coordinates()  # This unpacks the returned tuple from the function into individual variables x, y, and z
print(f"Coordinates: x={x}, y={y}, z={z}")  # This shows the values of x, y, and z after unpacking the tuple returned by the function

