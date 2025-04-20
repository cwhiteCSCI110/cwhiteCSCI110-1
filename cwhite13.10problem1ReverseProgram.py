#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      white
#
# Created:     19/04/2025
# Copyright:   (c) white 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

f = open("13.10number1.txt")                # Open file to read by default.
xs = f.readlines()                          # Read lines, return list of strings.
f.close()                                   # Close file to make available.

xs = xs[::-1]                               # Reverse list w/ slicing operation.

g = open("reversed13.10problem1.txt", "w")  # Open new file in write mode.
for v in xs:                                # Write each line to new file by
    g.write(v)                              # looping through one at a time.
g.close()                                   # Close file.

