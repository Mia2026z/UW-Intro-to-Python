file = open("testing.py", "w")

file = open("testing.py", "w")
file.write("Hi!\n")
file.close()

file = open("Warm-up.py", "r")
content = file.read()
print(content)
file.close

with open("testing.py", "r") as file:
    print(file.read())

file = open("my_info.txt", "w")
file.write("Hi! My name is Amelia and my favorite food is pizza.\n")
file.close()

file = open("my_info.txt", "a")
file.write("My favorite colors are blue and pink.")

file = open("my_info.txt", "r")
content = file.read()
print(content)
file.close

file = open("story.txt", "w")
file.close()

with open("story.txt", "w") as file:
    file.write("Hello world!!!\n\n\n\n")
    file.write("Happy Monday!")

file = open("story.txt", "r")
lines_list = file.readlines()
print("Number of lines: ", len(lines_list))
file.close()