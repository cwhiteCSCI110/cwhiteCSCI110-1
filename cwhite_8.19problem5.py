#-------------------------------------------------------------------------------
# Name:        cwhite_8.19problem5
# Purpose:
#
# Author:      cwhite
#
# Created:     29/03/2025
# Copyright:   (c) white 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

bg_quote = """ You have the right to work, but never to the fruit of work.
You should never engage in action for the sake of reward, nor should
you long for inaction. Perform work in this world, Arjuna, as a man
established within himself - without selfish attachments, and alike in success and defeat. """       # Excerpt from the Baghavad Gita.

import string                                   # Import string module to use definition.

def remove_punctuation(bg_quote):               # Function to remove punctuation.
    bg_quote_without_punct = ""
    for letter in bg_quote:
        if letter not in string.punctuation:
            bg_quote_without_punct += letter
    return bg_quote_without_punct

def count_words(bg_quote):                      # Function to count number of words total.
    words = bg_quote.split()                    # Add split to turn string into list of words, with no punctuation.
    return len(words)

def count_e(bg_quote):                          # Function to count the number of words that contain the letter "e".
    count = 0
    for c in bg_quote:
        if c == "e":
            count += 1
    return(count)

remove_punctuation(bg_quote)                    # Function call for punctuation removal.
words = count_words(bg_quote)                   # Function call assigned to variable.
e = count_e(bg_quote)                           # Other function call assigned to variable.
p = float(100 * (e / words))                    # Assigned percentage of e-words divided by total words as a float to variable.

print('Your text contains ' + str(words) + ' words, of which ' + str(e) + ' (' + str(p) + "%" + ')' + ' contain an "e".')