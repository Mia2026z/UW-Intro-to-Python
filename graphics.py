import turtle

# Create a screen
screen = turtle.Screen()
screen.title("Turtle Screen")

# Create the turtle
t = turtle.Turtle()
t.speed(2)
t.color("blue")
t.shape("arrow")

t.circle(50)

# Keep the window open
screen.mainloop()

