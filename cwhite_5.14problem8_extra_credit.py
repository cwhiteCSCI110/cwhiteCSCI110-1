#-------------------------------------------------------------------------------
# Name:        cwhite_5.14problem8_extra_credit
# Purpose:
#
# Author:      Clay White
#
# Created:     02/03/2025
# Copyright:   (c) Clay White 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import turtle

def draw_bar(t, height):
    if height >= 200:                            #Added conditional if statement
        tess.color("blue", "red")                #to make bars >= 200 red.
    elif height < 200 and height >= 100:         #Added chained conditional to
        tess.color("blue", "yellow")             #make bars 100-199 yellow.
    elif height < 100:                           #Added one more else if to make
        tess.color("blue", "green")              #bars 0-99 green.
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.forward(10)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
                                                #Removed Tess color & fill color
tess.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()