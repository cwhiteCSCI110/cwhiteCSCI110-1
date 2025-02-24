#-------------------------------------------------------------------------------
# Name:        cwhite_4.9problem2
# Purpose:
#
# Author:      white
#
# Created:     23/02/2025
# Copyright:   (c) white 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import turtle

def draw_growing_squares(t, size):          # Create function definition with 2 parameters
    """Make turtle t draw 5 squares each increasing in size by 20."""
    for i in ["square", "square1", "square2", "square3", "square4"]:        # Create for loop with 5 item sequence
        t.forward(size)                     # Draw square
        t.right(-90)                        #
        t.forward(size)                     #
        t.right(-90)                        #
        t.forward(size)                     #
        t.right(-90)                        #
        t.forward(size)                     #
        t.penup()                           # Begin reposition for next square
        t.forward(10)                       #
        t.right(-90)                        #
        t.forward(-10)                      #
        t.pendown()                         #
        size = size + 20                    # Increasing size for next square


wn = turtle.Screen()                        # Create window, canvas, title
wn.bgcolor("lightgreen")                    #
wn.title("Oliver draws 5 growing squares")  #

Oliver = turtle.Turtle()                    # Assign turtle to variable
Oliver.color("hotpink")                     # Assign attributes, state
Oliver.pensize(3)                           #
draw_growing_squares(Oliver, 20)            # Call the function
wn.mainloop()