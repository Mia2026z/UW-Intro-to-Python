# Creating a list of strings
fruits = ["apple", "banana", "cherry"]
print(fruits) # Output: ['apple', 'banana', 'cherry']

# Adding elements
fruits.append("orange")
print(fruits) # Output: ['apple', 'banana', 'cherry', 'orange']

# Inserting elements at a specific position
fruits.insert(1, "blueberry")
print(fruits) # Output: ['apple', 'blueberry', 'banana', 'cherry', 'orange']

# Removing elements
fruits.remove("banana")
print(fruits) # Output: ['apple', 'blueberry', 'cherry', 'orange']

# Popping elements (removes and returns the last element by default)
last_fruit = fruits.pop()
print(last_fruit) # Output: orange
print(fruits) # Output: ['apple', 'blueberry', 'cherry']

fav_food = ["fruit", "rice", "sandwhich", "cookie", "pizza"]
print(fav_food)

# Slicing a list
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1:4]) # Output: [2, 3, 4]
print(numbers[:3]) # Output: [1, 2, 3]
print(numbers[3:]) # Output: [4, 5, 6]
print(numbers[-3:]) # Output: [4, 5, 6]

# Slicing a list
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(number[:3]) # Output: [1, 2, 3]

# Sorting a list
marks = [87, 45, 78, 92, 66]
marks.sort()
print(marks)

import statistics as sts

# Average function
average_marks = sts.mean(marks)
print(average_marks)

# Creating a tuple
subject_tuple = ("math", "laguage arts", "science", "history")
print(subject_tuple)

# Accessing tuple items
animals = ("cat", "dog", "rabit", "hamster")
print(animals)
animal_list = list(animals)
print(animal_list)

# Min and max for animals and subjects
print(min(animals))
print(max(animals))
print(min(subject_tuple))
print(max(subject_tuple))

# Creating a dictionary
student = {
    "name": "Jordan",
    "age": 13,
    "grade": "8th"
}
print(student["name"])
# Output: Jordan

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "Data Analysis"]
}

# Accessing values
print(person["name"]) #Alice
print(person.get("age")) # 30
print(person["skills"])

# Adding/Updating values
person["city"] = "New York"
person["age"] = 31

# Removing items
del person["city"]
removed_age = person.pop("age")

# Creating another dictionary
person2 = {
    "name": "Margo",
    "age": 49,
    "skills": ["Python", "Data Analysis", "Biotechs"]
}

# Printing all info
print(person)

# Creating a list of dictionaries (list also in dictionary)
dict_list = [person, person2]
print(dict_list)

# Dictionary practice
b_day = {
    "Claire": "11/15",
    "Bob": "02/03",
    "Lily": "10/18"
}

# New student dictionary
student = {
    "name": "Alex",
    "grade": 8,
    "school": "Sunrise Middle"
}

# Print student's name
print(student["name"])

# Change grade to 9th
student["grade"] = "9" 
grade = student["grade"]

name = "hello WORLD"
print(name.upper()) # HELLO WORLD
print(name.lower()) # hello world
print(name.title()) # Hello World
print(name.capitalize()) # Hello world
print(name.swapcase()) # HELLO world

# .len() How many characters
#.strip() Removes space
#.replace() Swap one word for another
#.count() Count occurrences of a substring
#.find() Find index of a substring
#.split() Split into a list of words