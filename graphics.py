import turtle

# Create a screen
screen = turtle.Screen()
screen.title("Turtle Screen")

# Create the turtle
t = turtle.Turtle()
t.speed(0)
t.color("cyan")
t.shape("turtle")

t.color("cyan")
t.shape("turtle")

for i in range(72):
    t.circle(75)
    t.right(5)

t.color("purple")
t.shape("turtle")

for i in range(72):
    t.circle(90)
    t.right(5)

t.color("pink")
t.shape("turtle")

for i in range(72):
    t.circle(105)
    t.right(5)

t.color("blue")
t.shape("turtle")

for i in range(72):
    t.circle(120)
    t.right(5)

# Keep the window open
screen.mainloop()