import json
from random import choice, randrange
from string import ascii_uppercase as CAPS

from maddock.grammar import descriptions, moods, grammar
from maddock.song import getsong

DISPOSITIONS = {0.5: 'negative', 1: 'neutral', 1.5: 'positive'}
NEUTRAL = 0.5


def rname(length=0):
    """ Returns an random redacted name."""
    return choice(CAPS) + '_' * (length or randrange(4, 9))


def interact(c1, c2, observer=None):
    """ Plays out an interaction between 2 Characters, and one optional observer."""
    kind = choice(['item', 'talk', 'song', 'outfit',])
    obs = choice(('fore', 'aft'))
    if observer and obs == 'fore':
        r = grammar.flatten('#witness_fore#')
        r = r.replace('((C1))', observer.dtitle)
        print(r)
    if kind == 'talk':
        result = c1.interact_talk(c2)
    elif kind == 'outfit':
        result = c1.interact_outfit(c2)
    elif kind == 'item':
        result = c1.interact_item(c2)
    elif kind == 'song':
        result = c1.interact_song(c2)
    else:
        result = c1.interact(c2)
    if observer and obs == 'aft':
        observer.witness(c1, c2, result)
    print('\n')


class Character:
    POSSESIVES = ['her', 'his', 'their', 'hir']

    def __init__(self, occupation):
        self.title = f'**{occupation}**'
        self.tales = 0
        self.epithet = grammar.flatten('#epithet#')
        self.pos = choice(self.POSSESIVES)
        self.name = rname()
        self.feature = '{notable feature}'
        self.interest = grammar.flatten('#cinterest#')
        self.outfit = grammar.flatten('#outfit#')
        self.possesions = []
        for i in range(randrange(0, 4)):
            self.possesions.append(grammar.flatten('#smallitem#'))
        #print('DEBUG', self.possesions)
        self.dispositions = {}

    def desc(self):
        fidget = self.possesions and f'{grammar.flatten("#itemaction#")} a {choice(self.possesions)}'
        wearing = f'is wearing a {self.outfit}'
        desc = choice([None, fidget, wearing])
        if not desc:
            return ''
        return f', who {desc}'

    def init_dispositions(self, others):
        for other in others:
            if other == self:
                continue
            self.dispositions[other.title] = NEUTRAL

    def interact(self, other):
        print('The', self.dtitle, ', interacts with the', other.dtitle, '.')
        mood = choice([0.5, 1, 1.5])
        print('It is a', DISPOSITIONS[mood], 'interaction.')
        self.dispositions[other.title] *= mood
        other.dispositions[self.title] *= mood
        # print('***DEBUG DISPOSITIONS:***', self.dispositions)
        return mood

    def interact_item(self, other):
        i1 = bool(self.possesions) and choice(self.possesions)
        i2 = bool(other.possesions) and choice(other.possesions)
        if not i1:
            interaction = grammar.flatten('#get#')
        elif not i2:
            interaction = grammar.flatten('#give#')
        else:
            interaction = grammar.flatten('#swap#')
        if i2:
            self.possesions.append(i2)
            other.possesions.remove(i2)
        if i1:
            other.possesions.append(i1)
            self.possesions.remove(i1)
        if not i2:
            i2 = 'consoling hug'
        interaction = self.interaction_replace(interaction, other)
        interaction = interaction.replace('((i1))', str(i1))
        interaction = interaction.replace('((i2))', str(i2))
        print(interaction)
        return 1.5

    def interact_outfit(self, other):
        mood = choice([0.5, 1.5])
        if mood == 0.5:
            interaction = grammar.flatten('#outfitneg#')
        else:
            interaction = grammar.flatten('#outfitpos#')
        interaction = self.interaction_replace(interaction, other)
        print(interaction)
        return mood

    def interact_song(self, other):
        mood = choice([0.5, 1.5])
        song = getsong(15)
        if mood == 1.5:
            response = grammar.flatten('#goodsong#')
        else:
            song = song[:60] + '...'
            response = grammar.flatten('#badsong#')
        print(f"The {self.dtitle}, begins to sing:\n\n{song}")
        response = self.interaction_replace(response, other)
        print(response)
        return mood

    def interact_talk(self, other):
        interaction = grammar.flatten('#talk#')
        mood = choice([0.5, 1, 1.5])
        responses = {0.5: '#talkneg#', 1: '#neutral#', 1.5: '#talkpos#'}
        interaction += grammar.flatten(responses[mood])
        interaction = self.interaction_replace(interaction, other)
        print(interaction)
        return mood

    def interaction_replace(self, s, other=None):
        """Takes an interaction string and replaces character specific subs."""
        if not other:
            other = self
        s = s.replace('((C1))', self.dtitle)
        s = s.replace('((C2))', other.dtitle)
        s = s.replace('((C1title))', self.title)
        s = s.replace('((C2short))', other.title)
        s = s.replace('((C2title))', other.title)
        s = s.replace('((interest))', self.interest)
        s = s.replace('((C1outfit))', self.outfit)
        s = s.replace('((C2outfit))', other.outfit)
        return s

    def witness(self, a, b, mood=None):
        response = grammar.flatten('#witness#')
        response = response.replace('((C1))', self.dtitle)
        print(response)

    def enemy(self, characters):
        avail = [(c, self.dispositions[c.title]) for c in characters if c != self]
        if avail:
            return sorted(avail, key=lambda x: x[1])[0]

    def friend(self, characters):
        avail = [(c, self.dispositions[c.title]) for c in characters if c != self]
        if avail:
            return sorted(avail, key=lambda x: x[1])[-1]

    def enters(self, inn):
        content = grammar.flatten('#goinginn#')
        content = content.replace('((C1outfit))', self.outfit)
        content = content.replace('((C1))', self.title)
        return content % f'The {self.dtitle},'

    @property
    def atitle(self):  # used for default traveller listing
        return f'the {self.epithet} {self.title}'

    @property
    def dtitle(self):
        """ Description + title ('full-name')"""
        return self.epithet + " " + self.title + ', ' + self.name
