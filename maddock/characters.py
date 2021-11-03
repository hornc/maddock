import json
from random import choice, randrange
from string import ascii_uppercase as CAPS

from maddock.grammar import descriptions, moods, grammar


def rname(length=0):
    """ Returns an random redacted name."""
    return choice(CAPS) + '_' * (length or randrange(4, 9))


class Character:
    POSSESIVES = ['her', 'his', 'their']
    def __init__(self, occupation):
        self.title = occupation
        self.epithet = grammar.flatten('#epithet#')
        self.pos = choice(self.POSSESIVES)
        self.name = rname()
        self.feature = '{notable feature}'
        self.interest = '{interest}'
        self.outfit = '{outfit}'

    def desc(self):
        return self.epithet

    @property
    def dtitle(self):
        """ Description + title ('full-name')"""
        return self.epithet + " " + self.title + ', ' + self.name
