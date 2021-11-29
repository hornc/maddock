#!/usr/bin/env python3

"""
NaNoGenMo 2021: Þys Maddock


"""

import json
import random
import sys
from random import choice, sample

from maddock.characters import Character, interact
from maddock.grammar import adjectives, cinna, moods, grammar, number
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
ordinals = [' ', ' ', 'Second ', 'Third ', 'Fourth ', 'Fifth ', 'Sixth ', 'Seventh ', 'Eighth ', 'Ninth ', 'Tenth ', 'Eleventh', 'Twelfth ', 'Thirteenth ']


def group(characters):
    # list and describe the party
    l = random.sample(characters, len(characters))
    travel = grammar.flatten('#travel# %s' + '#fol# %s' * (len(l) - 1)) + '.'
    subs = tuple([c.atitle + c.desc() for c in l])
    return cinna(travel % subs)


def travel(characters, inn):
    if DEBUG:
        print(TRAVEL)
    print("%s %s travellers make their way by %s towards *%s* Inn." % (number(len(characters) + 1).capitalize(), random.choice(trav_adj), random.choice(method), inn.name))
    print("The weather is %s.\n" % (inn.weather.desc()))
    print(group(characters))
    print('\n')
    interactions(characters, inn)
    print('\nAs they near their destination they notice ', inn.sign(), inn.weather.item_desc('sign'))
    # Emotional state of the group
    print('The group feels %s as they approach the entrance to the inn.\n' % (choice(moods)))


def interactions(characters, inn):
    if DEBUG:
        print('***{INTERACTIONS}***')
    n = random.randint(0, len(characters) // 2)
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
    inn.interact(characters)
    for i in range(random.randint(4, 10)):
         inn.event()
    print(grammar.flatten('#animalsound#.'))
    inn.innkeeper(characters)
    party_sit(characters, inn)


def party_sit(characters, inn):
    print(f'\nThe weary travellers sit at the {inn.table}.')
    inn.event()
    interactions(characters, inn)
    inn.event()
    inn.event()
    inn.menu()
    inn.event()
    inn.event()
    print(grammar.flatten('#nexttale#'))


def tell_tale(inn, teller, characters):
    inn.teller = teller
    travel(characters, inn)
    the_inn(characters, inn)

    next_teller = teller.friend(characters)
    if next_teller:
        next_teller, disp = next_teller
        print(f"The {next_teller.title} stands up to be the next storyteller.\n")
        if next_teller == inn.previous_teller:
            next_teller = challenge_teller(inn, teller, next_teller, characters)
        inn.roll()

        removed = next_teller.enemy(characters)
        characters.remove(removed[0])
        next_teller.tales += 1
        print("The %s, waits for the chatter to subside and begins %s tale...\n" % (next_teller.dtitle, next_teller.pos))
        print(f" ## {24-len(characters)}: The {next_teller.title.title()}'s {ordinals[next_teller.tales]}Tale ({next_teller.tales})\n")
        #print("* the teller's enemy is", next_teller.enemy(characters))
        friend = next_teller.friend(characters)
        if DEBUG and friend:
            print(f"* the teller's friend is {friend[0].title} ({friend[1]}).\n")
    else:
        next_teller = None
    inn.previous_teller = teller
    return (next_teller, characters)


def challenge_teller(inn, teller, reject, characters):
    chars = characters.copy()
    chars.remove(teller)
    chars.remove(inn.previous_teller)
    if not chars:
        # no one left to challenge, accept the chosen teller
        return reject
    c = choice(chars)
    t = choice(chars)
    response = grammar.flatten('#challenge#')
    if c == t:
        # TODO: tidy this hack!
        response = response.replace('After some', '"Oh, that\'s me!" exclaims the ((C2title)) in surprise. After some')
    response = response.replace('((C1title))', reject.title)
    response = response.replace('((C1))', reject.dtitle)
    response = response.replace('((C2))', c.dtitle)
    response = response.replace('((C2title))', c.title)
    response = response.replace('((C3))', t.dtitle)
    print(response)
    return t



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
    #print('*{INTRO}*\n\n')
    teller = characters[0]
    while teller:
        last = teller
        teller, characters = tell_tale(inn, teller, characters)

    end = grammar.flatten('#ending#')
    end = end.replace('((WEAPON))', inn.weapon)
    end = end.replace('((teller))', last.title)
    print(end)

