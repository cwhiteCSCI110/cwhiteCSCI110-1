#-------------------------------------------------------------------------------
# Name:        cwhite20.8problem3
# Purpose:
#
# Author:      cwhite
#
# Created:     26/04/2025
# Copyright:   (c) cwhite 2025
# Licence:
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import string

#Remove Punctuation.
def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

#Function to count words, alphabetize, clean, and return as updated dictionary.
def count_words(text):
    words = text.split()
    word_dict = {}
    for word in words:
        clean_word = remove_punctuation(word).lower()
        if clean_word.isalpha():
            word_dict[clean_word] = word_dict.get(clean_word, 0) + 1
    return word_dict


def main():
    # Read the text file
    with open("alice.txt", "r") as file:
        aline = file.read().lower()

    # Count words and store them in a dictionary
    aline_dict = count_words(aline)

    dict_list = list(aline_dict.items())

    #Open new file to begin writing to.
    out = open('alice_words.txt', 'w')

    out.write("Word             Count\n")
    out.write("=======================\n")

    #Format layout of words and word counts in new file.
    for word, count in sorted(dict_list):
        n1 = word
        n2 = count
        layout = "{0:<17}{1:<18}"
        out.write(layout.format(n1, n2))
        out.write("\n")

    #Close file.
    out.close()

    print("The word alice occurs " + str(aline_dict["alice"]) + " times in Alice’s Adventures in Wonderland.")

if __name__ == "__main__":
    main()