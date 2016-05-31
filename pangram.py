"""
Check if a sentence is a Pangram.
A Pangram or holoalphabetic sentence for a given alphabet,
  is a sentence using every letter of the alphabet at least once.
"""
# Import the Regular Expressions Module
import re
# Get the letters of the alphabet
letters = map(chr, range(97, 123))


def is_pangram(str):
    # Get the expression
    expression = re.findall(r'[a-z]+', str, re.I)
    if expression:
        # Get the first letter of the first word in the expression
        exp = expression[0][0]
        # Incerment using all letters in the expression
        for word in expression:
            for letter in word:
                exp = exp + letter
        # Make it into a set to determine if every letter of the alphabet is
        # available
        ex = set(exp)
        # Check if the letters in the set are up to the total number of letters
        # in the alphabet
        if len(ex) < len(letters):
            return False
        return True
    return False
