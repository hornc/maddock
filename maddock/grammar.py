import json
import re
import tracery
from tracery.modifiers import base_english

from maddock import rules as madrules

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
follows = [', followed by', ', #tadj# followed by', '#follow#, #tadj#,', '. Next,', '. Then #tverb#', '. Then', '. #tadj.capitalize# after #tverb#',
        '. Next in #tline# #tverb#', ]

def wspace(text, *params):
    """Fix up extra whitespace + punctuation."""
    text = re.sub(r'\s{2,}', ' ', text)  # consolidate multiple spaces
    text = re.sub(r',{2,}', ',', text)  # consolidate multiple commas
    text = re.sub(r' -|- ', '-', text)
    return text

my_mods = {'wspace': wspace}

rules = {
    'adjective': adjectives,
    'epithet': '#epithet1.wspace#',
    'epithet1': '#mood# #join# #human_desc#',
    'mood': ['#mood1#', '#mood1# #join# #mood1#'],
    'mood1': moods,
    'human_desc': descriptions,
    'occupation': occupations,
    'join': joins,

    'travel': '#first# #tverb#',
    'fol': '#follow.wspace#',
    'first': firsts,
    'follow': follows,
    'tverb': ['is', 'comes', 'travels', 'goes', 'passes', 'moves', 'proceeds', 'processes', 'perambulates', 'approaches', ],
    'tline': ['line', 'sequence', 'procession', 'order', 'file', 'their #tline#', 'this #adjective# #tline#', 'the group' ],
    'tadj': ['closely', 'immediately', 'subsequently', 'stoically', 'reservedly', 'conscientiously', 'hopefully', 'doggedly', 'spasmodically', 'soon after', ],

    }

rules = {**rules, **madrules.rules}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
grammar.add_modifiers(my_mods)

