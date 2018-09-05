# ViralSpiral.py
import turtle           # Import turtle program
t = turtle.Pen()        # Declare that t is the pen
t.penup()               # Start with the pen up
turtle.bgcolor("black")     # Sets the backgrund color
# Ask the user for the number of sides, default to 4, min 2, max 6
sides = int(turtle.numinput("Number of sides", "How many sides in your spiral of spirals? (2-6)", 4,2,6))
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
# Our outer spiral loop
for m in range(100):    # Set number of iterations
    t.forward(m*4)
    position = t.position() # Remember this corner of the spiral
    heading = t.heading()   # Remember the direction we were heading
    print(position, heading)
    # Our "inner" spiral loop - nested loop
    # Draws a little spiral at each corner of the big spiral
    for n in range(int(m/2)):
        t.pendown()
        t.pencolor(colors[n%sides])
        t.forward(2*n)
        t.right(360/sides - 2)
        t.penup()
        t.setx(position[0]) # Go back to the big spiral's x position
        t.sety(position[1]) # Go back to the big spiral's y location
        t.setheading(heading)   # Point in the big spiral's heading
        t.left(360/sides + 2)   # Aim at the next point on the big spiral
        
