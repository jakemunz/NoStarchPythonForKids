# IfSpiral.py
answer = input("Do you want to see a spiral? y/n:")      # Asks user for y or n response and stores in 'answer'
if answer == 'y':   # If the answer is 'y' than the program executes      
    print("Working...")
    import turtle
    t = turtle.Pen()
    t.width(2)
    for x in range(100):
        t.forward(x*2)
        t.left(89)
print("Okay, we're done!")
