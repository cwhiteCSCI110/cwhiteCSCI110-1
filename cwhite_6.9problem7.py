#-------------------------------------------------------------------------------
# Name:        cwhite_6.9problem7
# Purpose:
#
# Author:      white
#
# Created:     09/03/2025
# Copyright:   (c) white 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def to_secs(hours,minutes,seconds):             # Function to get these units of
    return hours * 3600 + minutes * 60 + seconds
                                                # time to convert to seconds and
                                                # combine for total # of seconds.
def test_suite():
    """ Run the suite of tests for code in this module. """
    test(to_secs(2, 30, 10) == 9010)            # 5 tests to confirm that our
    test(to_secs(2, 0, 0) == 7200)              # function executes correctly.
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)


test_suite()                                                    # Function call.