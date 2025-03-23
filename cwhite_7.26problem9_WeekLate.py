#-------------------------------------------------------------------------------
# Name:        cwhite_7.26problem9_WeekLate
# Purpose:
#
# Author:      cwhite
#
# Created:     23/03/2025
# Copyright:   (c) white 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def print_triangular_numbers(n):                # Naming function to find triangular numbers.
    "Function to generate triangular numbers."  #
    for n in range(1, n + 1):                   # Telling range to start at 1, then compensate for the missing iteration.
        dots_in_triangle = n*(n+1) // 2         # Assigning formula to variable and reformatting copy/pasted equation for syntax.
        print(n, "\t", dots_in_triangle)        # Telling Python to format as requested in problem and print our results.

print_triangular_numbers(5)                     # Call.