import random
from random import choice
from string import ascii_uppercase as CAPS
from maddock import adjectives
from maddock.characters import rname, moods


def article(word):
    # Put this somewhere sensible.......
    if word[0].lower() in 'aeiou':
        return 'an'
    return 'a'


class Weather:
    TYPES = ['fair', 'foggy', 'rainy', 'sunny', 'stormy', 'windy', 'blustery']
    descs = {
            'fair': {'verbs': ['sparkles', 'glints', 'shimmers'], 'desc': ['in the sun']},
            'foggy': {'verbs': ['is barely visible', 'is covered with a slow moisture', 'looms menacingly'], 'desc': ['in the fog', 'through the fog']},
            'windy': {'verbs': ['clatters', 'bangs', 'dances crazily'], 'desc': ['in the wind']},
            'rainy': {'verbs': ['drips', 'is drenched', 'runs in rivulets'], 'desc': ['in the rain', 'in the downpour']},
            }
    descs['sunny'] = descs['fair']
    descs['stormy'] = choice([descs['windy'], descs['rainy']])
    descs['blustery'] = descs['windy']

    def __init__(self):
        self.type = choice(self.TYPES)
        self.strength = random.random()

    def desc(self):
        adj = ''
        if self.strength > 0.5:
            adj = 'very '
        if self.strength < 0.2:
            adj = 'barely '
        return adj + self.type

    def item_desc(self, item):
        return 'The %s %s %s.' % (item, choice(self.descs[self.type]['verbs']), choice(self.descs[self.type]['desc']))


ANIMALS = [
        'cat', 'dog', 'parrot', 'crow', 'raven', 'owl', 'falcon', 'hawk', 'thrush', 'dormouse', 'rat', 'mouse', 'vole', 'cockroach', 'deathwatch beetle',
        'dung beetle', 'fly', 'lac beetle', 'mantis', 'moth', 'horse', 'donkey', 'mule', 'cow', 'ox', 'sheep', 'lamb', ] 


STAFF =['stable-hand', 'room-attendant', 'grounds-keeper', 'cook', 'scullery-hand', 'bar-staffer', 'assistant-manager', 'pastry-cook', 'pot-scrubber', 'attendant wait-server',
        'vinter', 'lounge-operative']


class Keeper:
    def __init__(self):
        self.name = choice([rname(), f'{rname()} the {rname()}', f'{rname()} of {rname()}', f'{rname()}, {rname()} of {rname()}'])
        self.pro = choice(['them', 'her', 'him'])
        self.personality = choice(moods['moods'])


class Inn:
    def __init__(self):
        self.possesive = choice(['', "'s"])
        self.name = f'The {rname()}{self.possesive} {rname()}'
        self.weather = Weather()
        self.animal = choice(ANIMALS)
        self.keeper = Keeper()

    def sign(self):
        the, a, b = self.name.lower().replace("'s", '').split()
        out = "the Inn's sign depicts "
        descriptive = f"a very {choice(adjectives)} {b}, which appears exceedingly {a}."
        possesive = f"a very {choice(adjectives)} {b}, belonging to a {choice(adjectives)} {a}."
        return out + (possesive if self.possesive else descriptive)

    @property
    def table(self):
        adj = choice(adjectives)
        return f"{article(adj)} {adj} table"

    def feature(self):
        """Returns a random feature of the inn."""
        features = ['fireplace', 'door', 'storeroom', 'kitchen', 'stairs', 'window', 'bar', 'counter', 'main room', 'coat rack', 'rug']
        return choice(features)

    def staff(self):
        return choice(STAFF)

    def menu(self):
        summary = ['goods', 'victuals', 'bare necessities', 'gourmet offerings', 'foul sounding slops', 'provisions', 'tasty treats', 'servicable foodstuffs', 'sweetmeats', 'hearty pub meals',
                'pretentious sounding dishes', 'swillish slops', 'delicious delights', 'yummies', 'standard offerings', 'uninspring offerings', 'disapointing selections', 'impressive offerings',
                'forgettable fare']
        return choice(summary)

    @property
    def description(self):
        return 'is really awesome and well described.'
