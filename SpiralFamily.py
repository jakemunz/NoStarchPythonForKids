# SpiralFamily.py
import turtle           # Set up turtle graphics
t = turtle.Pen()        # Declars hat t is the on screen pen
turtle.bgcolor("black") # Sets the background color
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "brown", "gray", "pink"]
family = []             # Sets up an empty list for family names
name = turtle.textinput("My family", "Enter a name, or just hit [ENTER] to end:") # Ask for the first name
# Start while loop to keep asking for names
while name != "":       
    # Add their name to the family list
    family.append(name)
    # Ask for another name, or end
    name = turtle.textinput("My family", "Enter a name, or just hit [ENTER] to end:")
# Draw a spiral of the names on the screen
for x in range(100): # Range is the number of times the loop executes
    t.pencolor(colors[x%len(family)])   # Rotate through the colors
    t.penup()                           # Picks up pen, don't draw the regular spiral lines
    t.forward(x*4)                      # Just move the turtle on the screen
    t.pendown()                         # Places pen back down, begins drawing the next set of names
    t.write(family[x%len(family)], font = ("Arial", int((x+4)/4), "bold") ) # Iterates through the names the user entered in the family list, font and fon style
    t.left(360/len(family) + 2)         # Turn left for our spiral
