import json
from random import choice, randrange
from string import ascii_uppercase as CAPS

from maddock.grammar import descriptions, moods, grammar


NEUTRAL = 0.5


def rname(length=0):
    """ Returns an random redacted name."""
    return choice(CAPS) + '_' * (length or randrange(4, 9))


class Character:
    POSSESIVES = ['her', 'his', 'their']

    def __init__(self, occupation):
        self.title = occupation
        self.tales = 0
        self.epithet = grammar.flatten('#epithet#')
        self.pos = choice(self.POSSESIVES)
        self.name = rname()
        self.feature = '{notable feature}'
        self.interest = '{interest}'
        self.outfit = '{outfit}'
        self.dispositions = {}

    def desc(self):
        return self.epithet

    def init_dispositions(self, others):
        for other in others:
            if other == self:
                continue
            self.dispositions[other.title] = NEUTRAL

    def interact(self, other):
        print('The', self.dtitle, ', interacts with the', other.dtitle, '.')
        mood = choice([0.5, 1, 1.5])
        moods = {0.5: 'negative', 1: 'neutral', 1.5: 'positive'}
        print('It is a', moods[mood], 'interaction.')
        self.dispositions[other.title] *= mood
        other.dispositions[self.title] *= mood
        print('***DEBUG DISPOSITIONS:***', self.dispositions)
        return mood

    def witness(self, a, b, mood):
        print('The', self.dtitle, ', ', choice(['looks on in disgust', 'is jealous', 'is amused', 'does not understand']), '.')

    def enemy(self):
        return sorted(self.dispositions.items(), key=lambda x: x[1])[0]

    def friend(self):
        return sorted(self.dispositions.items(), key=lambda x: x[1])[-1]

    @property
    def atitle(self):  # used for default traveller listing
        return f'the {self.epithet} {self.title}'

    @property
    def dtitle(self):
        """ Description + title ('full-name')"""
        return self.epithet + " " + self.title + ', ' + self.name
