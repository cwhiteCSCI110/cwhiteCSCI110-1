#-------------------------------------------------------------------------------
# Name:        cwhite_5.14problem1
# Purpose:
#
# Author:      white
#
# Created:     01/03/25
# Copyright:   (c) white 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def day_name (day_number):       #Create function to get day name.
    if day_number == 0:          #Create conditional statement.
        print("Sunday")          #If conditional statement is true, print day
    elif day_number == 1:        #name. If false, check next statement.
        print("Monday")          #
    elif day_number == 2:        #
        print("Tuesday")         #
    elif day_number == 3:        #
        print("Wednesday")       #
    elif day_number == 4:        #
        print("Thursday")        #
    elif day_number == 5:        #
        print("Friday")          #
    elif day_number == 6:        #
        print("Saturday")        #
    else:                                                   #If all statements
        print("Invalid value. Choose number from 0 to 6.")  #are false, this
                                                            #ends statement.
day_name(0)         #
day_name(1)         #
day_name(2)         #Run each day number through the function to ensure they
day_name(3)         #execute correctly.
day_name(4)         #
day_name(5)         #
day_name(6)         #

day_name(9)         #Chose value outside of range to check else clause.