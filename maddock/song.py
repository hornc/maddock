from random import choices
# Data source https://www.gutenberg.org/ebooks/9405
# The Book of Old English Ballads by George Wharton Edwards


with open('maddock/data/9405.txt', 'r') as f:
    rawlines = f.readlines()[505:4114]


def getsong(lines=10):
    song = '  \n'.join(s.strip() for s in choices(rawlines, k=lines) if s[0] == ' ')
    return '> ' + song + '\n'

