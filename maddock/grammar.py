import json
import re
import tracery
from tracery.modifiers import base_english


with open('maddock/data/adjs.json') as f:
    adjectives = json.load(f)['adjs']


with open('maddock/data/occupations.json', 'r') as f:
        occupations = json.load(f)['occupations']


with open('maddock/data/moods.json', 'r') as f:
        moods = json.load(f)['moods']


with open('maddock/data/descriptions.json', 'r') as f:
        descriptions = json.load(f)['descriptions']


joins = ['', 'yet', 'but', 'and', 'but not so', 'nonetheless', 'and arguably', '-cum-', ]

firsts = ['First', 'In the lead', 'At the fore', 'Heading the group', 'Taking the initial position', 'At the forefront of the party', 'Leading, ', 'In first position', ]
follows = ['followed by the', '#tadj# #follow#', 'next in sequence #tverb# the', 'next', ]

def wspace(text, *params):
    """Fix up extra whitespace + punctuation."""
    text = re.sub(r'\s{2,}', ' ', text)  # consolidate multiple spaces
    text = re.sub(r' -|- ', '-', text)
    return text

my_mods = {'wspace': wspace}

rules = {
    'char_desc': '#epithet.wspace# #occupation#',
    'epithet': '#mood# #join# #human_desc#',
    'mood': ['#mood1#', '#mood1# #join# #mood1#'],
    'mood1': moods,
    'human_desc': descriptions,
    'occupation': occupations,
    'join': joins,

    'travel': '#first# #tverb# the #char_desc#, ' + '#fol# ' * 4,
    'fol': '#follow# the #char_desc#,',
    'first': firsts,
    'follow': follows,
    'tverb': ['is', 'comes', 'travels', 'goes', 'passes', 'moves', 'proceeds', 'processes', 'perambulates', 'approaches', ],
    'tadj': ['closely', 'immediately', 'subsequently', 'stoically', 'reservedly', 'conscientiously', 'hopefully', 'doggedly', 'spasmodically', 'soon after', ],
    }

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
grammar.add_modifiers(my_mods)

