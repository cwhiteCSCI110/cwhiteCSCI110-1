#-------------------------------------------------------------------------------
# Name:        cwhite13.10problem1_Corrected_Final_Program
# Purpose:
#
# Author:      cwhite
#
# Created:     19/04/2025
# Copyright:   (c) cwhite 2025
# Licence:
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

myfile = open("13.10number1.txt", "w")
myfile.write("My first file written from Python\n")
myfile.write("---------------------------------\n")
myfile.write("Hello, world!\n")
myfile.close()

f = open("13.10number1.txt")                # Open file to read by default.
xs = f.readlines()                          # Read lines, return list of strings.
f.close()                                   # Close file to make available.

xs = xs[::-1]                               # Reverse list w/ slicing operation.

g = open("reversed13.10problem1.txt", "w")  # Open new file in write mode.
for v in xs:                                # Write each line to new file by
    g.write(v)                              # looping through one at a time.
g.close()                                   # Close file.

