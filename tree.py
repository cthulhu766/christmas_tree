import turtle as tt
import time
tt.speed(100)

# Blue Background
tt.penup() # Pull the pen up – no drawing when moving.
tt.goto(0, -250)  # set position
tt.pendown() # Pull the pen down – drawing when moving.
tt.color("light sky blue")
tt.begin_fill()
tt.circle(250)
tt.end_fill()

# Tree Trunk
tt.penup()
tt.goto(-15, -50)
tt.pendown()
tt.color("brown")
tt.begin_fill()
for i in range(2):
    tt.forward(30)
    tt.right(90)
    tt.forward(40)
    tt.right(90)
tt.end_fill()

# Set the start position and the inital tree width
y = -50
width = 240
height = 25

# Green section of tree (add in the greater than symbol next to the 20 - YouTube doesn't allow me to put in pointy brackets).
while width > 20:
    width = width - 30  # Make the tree get smaller as it goes up in height
    x = 0 - width / 2  # Set the starting x-value of each level of the tree
    tt.color("green")
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    tt.begin_fill()
    for i in range(2):
        tt.forward(width)
        tt.left(90)
        tt.forward(height)
        tt.left(90)
    tt.end_fill()

    y = y + height  # Keep drawing the levels of the tree higher than the previous

# Star
tt.penup()
tt.goto(-15, 150)
tt.pendown()
tt.color("yellow")
tt.begin_fill()
for i in range(5):
    tt.forward(30)
    tt.right(144)
tt.end_fill()

# Message
tt.penup()
tt.goto(-130, -150)
tt.color("red")
tt.write("MERRY CHRISTMAS", font=("Arial", 20, "bold"))

time.sleep(15)
tt.hideturtle()