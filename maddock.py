#!/usr/bin/env python3

"""
NaNoGenMo 2021: Þys Maddock


"""

import json
import random
from random import choice

from maddock.characters import Character, moods
from maddock.inn import Inn

professions = 'maddock/data/occupations.json'


TRAVEL = """*(description of approach to the Inn)
(method of travel, horse, foot, carriage, other mechanical)
(weather, time of day, landscape)
(emotional theme of the travel)
(interactions between travellers)
(some event, notable interaction)
(distance + time to arrive at the inn)
(characters exhibit some facet of personality + disposition)*
"""

INN = """
*(arriving at the Inn)
(description of the Inn, the sign (weather + time of day), building, state, echo emotional theme)
(entering the Inn)
(description of interior, number of patrons)
(characters exhibit some facet of personality + disposition)
(describe a constant feature of the current Inn)
(some characters make a modification of the constant feature's state)
(Interaction or not with the proprieter)
(sit down at a table)
(order food or drinks)
(character interactions)
(events in the Inn room)
(characters exhibit some facet of personality + disposition)
(choose a story teller)
(dispositions adjust)*
"""


trav_adj = ['weary', 'intrepid', 'lusty', 'brave', 'foolhardy', 'optimistic', 'eager', 'browbeaten']
method = ['foot', 'horse', 'carriage', 'train', 'barge', 'sea', 'ocean going vessel', 'coach', 'camel', 'mule']
to_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
            'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one',
            'twenty-two', 'twenty-three', 'twenty-four']

def movements():
    movements = ['walks', 'strides', 'saunters', 'sashays', 'slinks', 'slithers', 'bounds', 'traipses', 'stumbles', 'catapults', 'zips',
             'bumbles', 'moves', 'charges', 'speeds', 'wriggles', 'undulates', 'sprints', 'shoots', 'scoots', 'dances', 'leaps']
    return choice(movements)


def group(characters):
    # list and describe the party
    l = random.sample(characters, len(characters))
    out = 'First is the %s %s' % (l[0].desc(), l[0].title)
    for c in l[1:]:
        out += ' followed by the %s %s,' % (c.desc(), c.title)
    return out + '.'


def travel(characters, inn):
    print(TRAVEL)
    print("%s %s travellers make their way by %s towards *%s* Inn." % (to_words[len(characters)].capitalize(), random.choice(trav_adj), random.choice(method), inn.name))
    print("It is %s." % (inn.weather.desc()))
    print(group(characters))
    interactions(characters, inn)
    print('As they near their destination, they notice ', inn.sign(), inn.weather.item_desc('sign'))
    # Emotional state of the group
    print('The group feels %s as they approach the entrance to the inn.' % (choice(moods['moods'])))


def interactions(characters, inn):
    for i in range(0, random.randint(0, int(len(characters) * 0.3333))):
        print('The', choice(characters).dtitle, ' interacts with the', choice(characters).dtitle,)
        print('It is a', choice(['positive', 'negative', 'neutral']), 'interaction.')
        print('The', choice(characters).dtitle, choice(['looks on in disgust', 'is jealous', 'is amused', 'does not understand']), '.')


def the_inn(characters, inn):
    print(INN)
    print('*INN: ARRIVE ENTER DESCRIBE INN_INTERACT INNKEEP SIT INDOOR_INTERACT ORDER NEXT_STORYTELLER*\n\n')
    print('*SOME MECHANIC REDUCES THE GROUP BY ONE .........*\n\n')
    print('The %s enters the inn first %s.' % (choice(characters).dtitle, '{description}'))
    print('The %s reacts {reaction}.' % (choice(characters).dtitle), '{supplementary reaction from a third individual or the group}')
    print('Inside, the inn %s' % inn.description)
    inn_interact(characters, inn)
    innkeeper(characters, inn)
    party_sit(characters, inn)


def inn_interact(characters, inn):
    print('The travelers interact with the Inn in an interesting and satisfying way.')
    print('Close by, or far away, a %s makes a sound, is seen, or unobservedly does something characteristic yet poignant.' % inn.animal)


def innkeeper(characters, inn):
    print(f'"Oh look, over there by the {inn.feature()}; there is the innkeeper, looking rather {inn.keeper.personality}. Let us talk to {inn.keeper.pro}!" says the {choice(characters).dtitle}.')
    print('The innkeeper, %s, has a %s personality, and some worldly advice to impart (if the mood takes %s).' % (inn.keeper.name, inn.keeper.personality, inn.keeper.pro))
    print('"Grab yourselves a table, and I\'ll be with you shortly to take orders..."')


def party_sit(characters, inn):
    print(f'The weary travellers sit at {inn.table}.')
    print('They have some interactions, and remark upon their situation.')
    interactions(characters, inn)
    print('Possibly, something notable happens. What is the outcome?')
    print('Someone may be called away, or storm off, or otherwise be excused.')
    print(f'Presently the Innkeeper (or possibly another staff member) {movements()} over to take their orders.')
    print('Available goods are stated, questioned, and chosen, consisting of food and / or drinks. There is indecision, and certainty.')
    print('Once all orders are made, the group settles in to wait. Drinks may arrive, but the food takes time to prepare.')
    print('Something happens in the main room.')
    print('In order to entertain themselves, as is their custom on this journey, they decide to pass the time telling stories,',
          ' and chose from their number one person to tell this evening\'s tale...')


def tell_tale(teller, characters):
    inn = Inn()
    travel(characters, inn)
    the_inn(characters, inn)

    characters = characters[:-1]
    if characters:
        next_teller = choice(characters)
        print("The %s waits for the chatter to subside and begins %s tale...\n" % (next_teller.dtitle, next_teller.pos))
        print(" ## The %s's Tale\n" % next_teller.title.title())
    else:
        next_teller = None
    return (next_teller, characters)


if __name__ == '__main__':
    with open(professions, 'r') as f:
        occupations = json.load(f)
        characters = [Character(c) for c in random.sample(occupations['occupations'], 24)]

    #print('# Þæt Maddock')
    print('# Þys Maddock')
    print('### a NaNoGenMo 2021 simulated, recursive tale.')
    print('*{INTRO}*\n\n')
    teller = characters[0]
    while teller:
        teller, characters = tell_tale(teller, characters)

    print('\n\n ... RESOLUTION for the final storyteller, %s' % '{someone}')

