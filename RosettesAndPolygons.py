# RosettesAndPolygons.py draws rosettes at even corners and polygons at odd corners
import turtle
t = turtle.Pen()
# Ask the user for the number of sides, default to 4
sides = int(turtle.numinput("Number of sides", "How many sides in your spiral?", 4))
# Outer spiral loop for polygns and rosettes, from size 5 to 75
for m in range(5,75):
    t.left(360/sides + 5)
    t.width(m//25+1)
    t.penup()           # Don't draw lines on spiral
    t.forward(m*4)      # Move to next corner
    t.pendown()         # Get ready to draw
    # Draw a little rosette at each EVEN corner of the spiral
    if (m % 2 == 0):
        for n in range(sides):
            t.circle(m/3)
            t.right(360/sides)
    # Or, draw a little polygon at each ODD corner of the spiral
    else:
        for n in range(sides):
            t.forward(m)
            t.right(360/sides)
    
