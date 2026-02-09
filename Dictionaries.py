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

