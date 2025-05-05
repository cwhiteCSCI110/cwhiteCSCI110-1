#-------------------------------------------------------------------------------
# Name:        cwhite19.6problem1
# Purpose:
#
# Author:      cwhite
#
# Created:     04/05/2025
# Copyright:   (c) cwhite 2025
# Licence:
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def readposint():
   while True:
       user_input = input("Enter a positive integer: ")
       if user_input.isdigit():
           user_int = int(user_input)
           if user_int > 0:
               return user_int
       print("Does not meet requirements. Please enter a positive integer. Try again.")

readposint()