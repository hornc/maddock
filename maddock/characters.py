import json
from random import choice, randrange
from string import ascii_uppercase as CAPS


with open('maddock/data/descriptions.json') as f:
    descriptions = json.load(f)


with open('maddock/data/moods.json') as f:
    moods = json.load(f)


def rname(length=0):
    """ Returns an random redacted name."""
    return choice(CAPS) + '_' * (length or randrange(4, 9))


joins = ['', 'yet', 'but', 'and', 'but not so', 'nonetheless', 'and arguably', '-cum-', ]


class Character:
    POSSESIVES = ['her', 'his', 'their']
    def __init__(self, occupation):
        self.title = occupation
        self.pos = choice(self.POSSESIVES)
        self.name = rname()
        self.feature = '{notable feature}'
        self.interest = '{interest}'
        self.outfit = '{outfit}'
        self.d = ' '.join([choice(moods['moods']), choice(joins), choice(descriptions['descriptions'])])

    def desc(self):
        return self.d

    @property
    def dtitle(self):
        """ Description + title ('full-name')"""
        return self.desc() + " " + self.title + ', ' + self.name
