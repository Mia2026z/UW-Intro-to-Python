level=12
has_gear=True
health=70
has_armor=False
if level < 10:
    print("Level up before entering this area.")
elif (not has_gear):
    print("You need a weapon to fight!")
    if(health < 50):
        print("Heal up before the fight!")
else:
    print("You're ready for battle!")



print(list(range(1, 5, 2)))
for num in range(1,6):
    print(f"The current number is {num}")

for i in range(5, 0, -1):
    print(i)

count = 10
while count>0:
    print(count)
    count -= 1
print("Rocket blasting off!")
i=1
while i <= 3:
    print(i)
    i+=1
x=1
while x < 10:
    x*=2
    print(x)

for floor in range(3):
    print("Starting Floor", floor+1)
    for block in range(4):
        print("Placing block", block+1)

for row in range(3):
    for col in range(4):
        print("*", end="")
    print() #New line after each row)
    
for row in range(5):
    for col in range(5):
        print("^", end="")
    print() #New line after each row

for row in range(1,5):
    for col in range(1,row+1):
        print(col,end="")
    print() #New line after each row


#Define the function
def say_hello(name):
    print(f"Hello, {name}!")
#Call the function with different names
say_hello("Emma")
say_hello("Liam")
say_hello("Sophia")

user_input = input("Ask me a question: ")
print("Yes!")

import random
print(random.randint(1, 100))

import turtle

# Create a screen
screen = turtle.Screen()
screen.title("Turtle Screen")

# Create the turtle
t = turtle.Turtle()
t.speed(5)
t.color("blue")
t.shape("turtle")

# Keep the window open
screen.mainloop()

# Move the turtle
t.forward(100)
t.back()
t.right(90)
t.left(90)

t.penup()
t.pendown()
t.pensize()
t.pencolor("")



# 1st
t.penup()
t.forward(50)
t.right(90)
t.pendown()
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.penup()
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)

# Second square
t.pendown()
t.forward(100)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(100)

# Third square
t.penup()
t.left(90)
t.forward(50)
t.right(90)
t.pendown()
t.forward(150)
t.right(90)
t.forward(300)
t.right(90)
t.forward(300)
t.right(90)
t.forward(300)
t.right(90)
t.forward(150)