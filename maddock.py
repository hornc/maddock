#!/usr/bin/env python3

"""
NaNoGenMo 2021: Þys Maddock


"""

import json
import random
import sys
from random import choice, sample

from maddock.characters import Character, interact
from maddock.grammar import adjectives, moods, grammar
from maddock.inn import Inn

professions = 'maddock/data/occupations.json'

DEBUG = False
INDENT = '&nbsp;' * 6

TRAVEL = """
- [ ] (description of approach to the Inn)
- [x] (method of travel, horse, foot, carriage, other mechanical)
- [x] (weather, time of day, landscape)
- [ ] (emotional theme of the travel)
- [x] (interactions between travellers)
- [ ] (some event, notable interaction)
- [ ] (distance + time to arrive at the inn)
- [ ] (characters exhibit some facet of personality + disposition)
"""

INN = """
- [x] (arriving at the Inn)
- [x] (description of the Inn, the sign (weather + time of day), building, state, echo emotional theme)
- [x] (entering the Inn)
- [ ] (description of interior, number of patrons)
- [ ] (characters exhibit some facet of personality + disposition)
- [ ] (describe a constant feature of the current Inn)
- [ ] (some characters make a modification of the constant feature's state)
- [x] (Interaction, or not, with the proprietor)
- [x] (sit down at a table)
- [x] (order food or drinks)
- [x] (character interactions)
- [ ] (events in the Inn room)
- [ ] (characters exhibit some facet of personality + disposition)
- [x] (choose a story teller)
- [x] (dispositions adjust)
"""


trav_adj = ['weary', 'intrepid', 'lusty', 'brave', 'foolhardy', 'optimistic', 'eager', 'browbeaten']
method = ['foot', 'horse', 'carriage', 'train', 'barge', 'sea', 'ocean going vessel', 'coach', 'camel', 'mule']
to_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
            'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one',
            'twenty-two', 'twenty-three', 'twenty-four']
ordinals = [' ', ' ', 'Second ', 'Third ', 'Fourth ', 'Fifth ', 'Sixth ', 'Seventh ', 'Eighth ', 'Ninth ', 'Tenth ', 'Eleventh', 'Twelfth ', 'Thirteenth ']


def group(characters):
    # list and describe the party
    l = random.sample(characters, len(characters))
    #out = grammar.flatten(f'#travel# %s}')
    travel = grammar.flatten('#travel# %s' + '#fol# %s' * (len(l) - 1)) + '.'
    subs = tuple([c.atitle + c.desc() for c in l])
    return travel % subs


def travel(characters, inn):
    if DEBUG:
        print(TRAVEL)
    print("%s %s travellers make their way by %s towards *%s* Inn." % (to_words[len(characters)].capitalize(), random.choice(trav_adj), random.choice(method), inn.name))
    print("It is %s.\n" % (inn.weather.desc()))
    print(group(characters))
    print('\n')
    interactions(characters, inn)
    print('\nAs they near their destination they notice ', inn.sign(), inn.weather.item_desc('sign'))
    # Emotional state of the group
    print('The group feels %s as they approach the entrance to the inn.\n' % (choice(moods)))


def interactions(characters, inn):
    if DEBUG:
        print('***{INTERACTIONS}***')
    n = random.randint(0, len(characters) // 3)
    interactors = sample(characters, n * 2)
    for i in range(0, n, 2):
        observer = choice(characters)
        interact(interactors[i], interactors[i + 1], observer)


def the_inn(characters, inn):
    if DEBUG:
        print(INN)
    first = choice(characters)
    print(first.enters(inn))
    print(grammar.flatten('#react#'))
    #print('The %s, reacts {reaction}.' % (choice(characters).dtitle), '{supplementary reaction from a third individual or the group}.')
    #print('\nInside, the inn %s' % inn.description)
    inn.interact(characters)
    for i in range(random.randint(1, 7)):
         inn.event()
    print(grammar.flatten('#animalsound#.'))
    inn.innkeeper(characters)
    party_sit(characters, inn)


def party_sit(characters, inn):
    print(f'\nThe weary travellers sit at {inn.table}.')
    inn.event()
    #print('They have some interactions, and remark upon their situation.\n\t')
    interactions(characters, inn)
    #print('\n\nPossibly, something notable happens. What is the outcome?')
    inn.event()
    inn.menu()
    inn.event()
    print(grammar.flatten('#nexttale#'))


def tell_tale(inn, teller, characters):
    travel(characters, inn)
    the_inn(characters, inn)

    next_teller = teller.friend(characters)
    if next_teller:
        inn.roll()
        next_teller, disp = next_teller
        print(f"* The current storyteller ({teller.title}) chooses the {next_teller.title} ({disp}) as the next storyteller.\n")
        removed = next_teller.enemy(characters)
        characters.remove(removed[0])
        next_teller.tales += 1
        print("The %s, waits for the chatter to subside and begins %s tale...\n" % (next_teller.dtitle, next_teller.pos))
        print(f" ## {24-len(characters)}: The {next_teller.title.title()}'s {ordinals[next_teller.tales]}Tale ({next_teller.tales})\n")
        #print("* the teller's enemy is", next_teller.enemy(characters))
        friend = next_teller.friend(characters)
        if friend:
            print(f"* the teller's friend is {friend[0].title} ({friend[1]}).\n")
    else:
        next_teller = None
    return (next_teller, characters)


if __name__ == '__main__':
    with open(professions, 'r') as f:
        occupations = json.load(f)
        characters = [Character(c) for c in random.sample(occupations['occupations'], 24)]

    for c in characters:
        c.init_dispositions(characters)

    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        DEBUG = True
    inn = Inn(characters)
    print('# Þys Maddock')
    print('### a NaNoGenMo 2021 simulated, recursive tale.')
    print('*{INTRO}*\n\n')
    teller = characters[0]
    while teller:
        last = teller
        teller, characters = tell_tale(inn, teller, characters)

    print('\n\n ... RESOLUTION for the final storyteller: the %s!' % last.dtitle)

