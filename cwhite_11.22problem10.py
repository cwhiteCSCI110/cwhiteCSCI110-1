#-------------------------------------------------------------------------------
# Name:        cwhite_11.22problem10
# Purpose:
#
# Author:      white
#
# Created:     06/04/2025
# Copyright:   (c) white 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import sys

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"

def replace(s, old, new):
    """ Replace all occurrence of old with new in s string """
    s = s.split(old)
    j = new.join(s)
    return j

def test(did_pass):
    """ Print test result """
    linenum = sys._getframe(1).f_lineno             # Get caller's line number
    if did_pass:
        msg = "Test at line {0} is ok".format(linenum)
    else:
        msg = "Test at line {0} is FAILED".format(linenum)
    print(msg)

def test_suite():
    """Function to run test suite """
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")

    test(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")

    test(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

test_suite()                                                    # Function call

