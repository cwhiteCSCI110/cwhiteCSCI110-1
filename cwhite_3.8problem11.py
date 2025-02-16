#-------------------------------------------------------------------------------
# Name:        cwhite_3.8problem11
# Purpose:
#
# Author:      white
#
# Created:     16/02/2025
# Copyright:   (c) white 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import turtle
wn = turtle.Screen()            # Creating our turtle and canvas.
Starboy = turtle.Turtle()       # Assigning variable "Starboy".
wn.bgcolor("black")             # Titling and adding background color.
wn.title("Go Starboy")
Starboy.shape("turtle")         # Adding attributes and current states to
Starboy.color("yellow")         # Starboy.
Starboy.pensize(10)
Starboy.speed(3)

Starboy.penup()                 # Starting to invoke our methods. This portion
Starboy.right(90)               # was added to get Starboy out of origin point
Starboy.forward(100)            # to center the star.
Starboy.right(90)
Starboy.forward(75)
Starboy.right(108)
Starboy.pendown()

for i in range(5):              # Creating for loop to get Starboy to make 5
    Starboy.forward(200)        # movements and 5 rotations to complete star.
    Starboy.right(144)

wn.mainloop()

