"""
This algorithm helps you to swap cases.

User will give input and then program will perform swap cases.

In other words, convert all lowercase letters to uppercase letters and vice versa.
For example:
1)>>> Please input sentence: Algorithm.Python@89
  aLGORITHM.pYTHON@89
2)>>> Please input sentence: github.com/mayur200
  GITHUB.COM/MAYUR200

"""
import re

# This re.compile() function saves the pattern from 'a' to 'z' and 'A' to 'Z' into 'regexp' variable
regexp = re.compile("[^a-zA-Z]+")


def swap_case(sentence):
    """
    This function will convert all lowercase letters to uppercase letters and vice versa.

    >>> swap_case('Algorithm.Python@89')
    aLGORITHM.pYTHON@89
    """
    new_string = ""
    for char in sentence:
        if char.isupper() == True:
            new_string += char.lower()
        if char.islower() == True:
            new_string += char.upper()
        if regexp.search(char) == True:
            new_string += char

    return new_string


if __name__ == '__main__':
    s = input("Please input sentence:")
    result = swap_case(s)
    print(result,"\n")


