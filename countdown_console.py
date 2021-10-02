"""
Countdown (Console)
Play a game of Countdown in the console.
Created: 02.10.21;    Author: SL
The "module docstring", documenting the file contents. pylint gets sad without.
"""

import sys
# import random
# import itertools as it
import string
# from time import time, sleep, perf_counter
# from PIL import Image
from numpy.random import shuffle  # , randint


# Get lists of vowels and consonants, with normalised distributions.
# Source: http://www.thecountdownpage.com/letters.htm (circa 2009)
ALP = list(string.ascii_uppercase)
VOWELS = ['A', 'E', 'I', 'O', 'U']
V_DIST = [15, 21, 13, 13, 5]                 # Distribution of vowels.
CONSONANTS = [let for let in ALP if let not in VOWELS]
C_DIST = [2, 3, 6, 2, 3, 2, 1, 1, 5, 4, 8, 4, 1, 9, 9, 9, 1, 1, 1, 1, 1]

# Stack of letters.
V_STACK = []
for [i, _] in enumerate(V_DIST):
    for j in range(V_DIST[i]):
        V_STACK.extend(VOWELS[i])
        shuffle(V_STACK)

C_STACK = []
for [i, _] in enumerate(C_DIST):
    for j in range(C_DIST[i]):
        C_STACK.extend(CONSONANTS[i])
        shuffle(C_STACK)

# Ask if player wants to play a game.
KEEN = input('Want to play a game of Countdown? (Y/N) ')
KEEN = KEEN[0].lower()
if KEEN == 'n':
    sys.exit('Ok, nevermind.')
elif KEEN != 'y':
    sys.exit("I'll take that as a no.")

# Draw letters.
LETTERS = []
LET_STR = ''
for _ in range(9):
    LET = input('Consonant or vowel? (C/V) ')
    LET = LET[0].upper()
    if LET == 'C':
        NEW_LET = C_STACK.pop(0)
    elif LET == 'V':
        NEW_LET = V_STACK.pop(0)
    else:
        sys.exit('Come on! Take it seriously.')
    LETTERS.extend(NEW_LET)
    if LET_STR == '':
        LET_STR = NEW_LET
    else:
        LET_STR = '{0} | {1}'.format(LET_STR, NEW_LET)
    print(LET_STR, '\n')

# Start 'timer'.
# Next steps: add timer, results/word checker.
