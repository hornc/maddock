import random
from random import choice
from string import ascii_uppercase as CAPS
from maddock.characters import rname
from maddock.grammar import adjectives, moods, grammar, number


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


STAFF = ['stable-hand', 'room-attendant', 'grounds-keeper', 'cook', 'scullery-hand', 'bar-staffer', 'assistant-manager', 'pastry-cook', 'pot-scrubber', 'attendant wait-server',
        'vinter', 'lounge-operative']

CROWD = ['is next to empty', 'is almost empty', 'is barely full', 'is not very packed', 'is moderately crowded', 'has a reasonable crowd', 'is packed with very rowdy patrons']

class Keeper:
    def __init__(self):
        self.name = choice([rname(), f'{rname()} the {rname()}', f'{rname()} of {rname()}', f'{rname()}, {rname()} of {rname()}'])
        self.pro = choice(['them', 'him', 'hir',])
        self.personality = choice(moods)


class Inn:
    def __init__(self, characters):
        self.characters = characters
        self.teller = None
        self.previous_teller = None
        self.mantel = ['golden sovereign', 'small bust of the poet Cinna', 'apple', 'maggot (Rhagoletis pomonella) writhing spasmodically outside the soft flesh of its preferred substrate']
        self.weapon = choice(['axe', 'sword', 'polearm', 'flail', 'crossbow', 'greatsword', 'battleaxe', 'mace', 'warhammer', 'maul', 'sabre', 'scimitar', 'halberd', 'claymore', 'falchion', 'pike',
                              'stiletto', 'gladius'])
        self.painting = choice(['blasted landscape', 'coastal scene', 'pastoral scene', 'woman', 'man'])
        self.roll()

    def roll(self):
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
        out += possesive if self.possesive else descriptive
        out += grammar.flatten('#style#')
        return out

    @property
    def table(self):
        adj = choice(adjectives)
        return f"{adj} table"

    def feature(self):
        """Returns a random feature of the inn."""
        return grammar.flatten('#innloc#')

    def event(self):
        chars = self.characters.copy()
        chars.remove(self.teller)
        if not chars:
            return
        e = grammar.flatten('#innevent.capitalize#.')
        c1 = choice(chars)
        chars.remove(c1)
        if chars:
            c2 = choice(chars)
            e = e.replace('((C2))', c2.dtitle)
            e = e.replace('((C2title))', c2.title)
        e = e.replace('((C1))', c1.dtitle)
        e = e.replace('((C1title))', c1.title)
        e = e.replace('((interest))', c1.interest)
        e = e.replace('((teller_title))', self.teller.title)
        print(e)

    def staff(self):
        return choice(STAFF)

    def menu(self):
        r = grammar.flatten('#menu#')
        c1 = choice(self.characters)
        #c2 = choice(self.characters)
        r = c1.interaction_replace(r)
        print(r)

    def showmantel(self, characters):
        if self.mantel:
            mantel = ' Upon the mantel in the main room, above a roaring fire, are the following items: one %s.' % (', one '.join(self.mantel))
        else:
            mantel = ' There is a roaring fire in the public room. Its mantel is bare.'
        mantel += grammar.flatten('#weapon#').replace('((WEAPON))', self.weapon)
        mantel = mantel.replace('Cinna', 'Cinna (' + grammar.flatten('#cinnafact#' + ')'))
        print(mantel)
        c = choice(characters)
        if not c.possesions:
            take = True
        elif not self.mantel:
            take = False
        else:
            take = choice([True, False])

        if take:
            if self.mantel:
                i = choice(self.mantel)
                print(f'The {c.title}, when no one is looking, takes the {i} from the mantel and pockets it.')
                c.possesions.append(i)
                self.mantel.remove(i)
            else:
                print(f'The {c.title} surreptitiously moves over to the mantel looking for a worthwhile trinket to pocket, but finds in bare. Dissapointed, {c.dtitle}, rejoins the party.')
        else:
            i = choice(c.possesions)
            print(f'The {c.title} wanders over to take a look, and adds a {i} to the collection of trinkets.')
            self.mantel.append(i)
            c.possesions.remove(i)

    def interact(self, characters):
        """ Initial interaction with the inn after characters pass the entrance."""
        crowd = choice(CROWD)
        
        painting = f' By the {self.feature()} hangs a painting of a {self.painting}.'
        print('\n\n' + grammar.flatten('#innside#').replace('XXX', self.name))
        print(painting)
        self.showmantel(characters)
        print(f'\n\nThe public room {crowd}.')

    def innkeeper(self, characters):
        out = grammar.flatten('#addressinnkeeper#')
        c1 = choice(characters)
        out = out.replace('((C1))', c1.dtitle)
        out = out.replace('((ik))', self.keeper.name)
        out = out.replace('((ikpersonality))', self.keeper.personality)
        out = out.replace('((ikpro))', self.keeper.pro)
        out = out.replace('((number))', number(len(characters) + 1))
        print(out)

