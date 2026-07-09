times = True
if (times):
    print("Jumping!")
else:
    print("Too tired to jump.")
    
#Define the function
def say_hello(name):
    print(f"Hello, {name}!")
#Call the function with different names
say_hello("Emma")
say_hello("Liam")
say_hello("Sophia")

#Define the function
def introduce(first_name, last_name, age):
    #Basic print
    print("Let's meet our student!")
    #Print multiple items
    print(first_name, "is", age, "years old.")
    #Using sep to chagne space to dashes
    print(first_name, last_name, sep="-")
    #Using sep to remove all spaces
    print(first_name, "is", age, "years old.", sep="")
    #Using end to avoid a new line
    print("Name:", first_name, end="")
    print(last_name)
    #Using string multiplication
    print(first_name*2, last_name*3)
    print("*"*20)
#Call the function with your own values!
introduce("Amelia", "Zhang", 12)


import turtle

# Create a screen
screen = turtle.Screen()
screen.title("Turtle Screen")

# Create the turtle
t = turtle.Turtle()
t.speed(5)
t.color("blue")
t.shape("turtle")

t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

t.forward(100)
t.right(180)
t.forward(200)
t.left(180)
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)

t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)

t.right(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)

t.right(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)

t.right(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)

t.forward(100)
t.left(90)
t.forward(100)

turtle.goto(0, 0)
turtle.goto(-100, -100)
turtle.goto(100, 100)
turtle.goto

print(turtle.xcor())
print(turtle.ycor())

# Keep the window open
screen.mainloop()

