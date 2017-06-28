from turtle import *
import math

# Name your Turtle. Right now her name is t. If you change her name, make sure to change the name below, too.
t = Turtle()

# Set Up your screen and starting position.
setup(600,600)
x_pos = -250
y_pos = -150
t.penup()
t.setposition(x_pos, y_pos)
t.pendown()

sidesstring = input('Enter number of sides: ')
sidesinteger = int(sidesstring)

sizestring = input('Enter size: ')
sizeinteger = int(sizestring)

colorstring = input('Enter color: ')
print(colorstring, "polygon of",sidesstring, "sides and",sizestring, "size")

def draw(sidesinteger, size, color):
    t.penup()
    t.fillcolor(color)
    t.setposition(0,0)
    t.pendown()
    t.begin_fill()

    for sides in range(sidesinteger):
        t.forward(size)
        t.right(360/sidesinteger)
    t.end_fill()
draw(sidesinteger, sizeinteger, colorstring)
### Write your code below:


# Close window on click.
exitonclick()
