import json
import re
import tracery
from tracery.modifiers import base_english

from maddock import rules as madrules

with open('maddock/data/adjs.json') as f:
    adjectives = json.load(f)['adjs']

with open('maddock/data/adverbs.json') as f:
    adverbs = json.load(f)['adverbs']

with open('maddock/data/occupations.json', 'r') as f:
        occupations = json.load(f)['occupations']


with open('maddock/data/moods.json', 'r') as f:
        moods = json.load(f)['moods']


with open('maddock/data/descriptions.json', 'r') as f:
        descriptions = json.load(f)['descriptions']

with open('maddock/data/ending.txt', 'r') as f:
        ending = f.read()

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

def number(n):
    """Returns the number of characters in words."""
    to_words = ['zero', 'one', 'a pair', 'a trio', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
            'thirteen', 'fourteen', 'fifteen', 'four shy of a full score of', 'three shy of a full score of', 'two shy of a full score of', 'one shy of a full score of', 'a full score of', 'one score and one',
            'one score and two', 'one score and three', 'one score and four', 'one score and five']
    return to_words[n]

my_mods = {'wspace': wspace}

rules = {
    'adjective': adjectives,
    'adverb': adverbs,
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
    'ending': ending,
    }

rules = {**rules, **madrules.rules}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
grammar.add_modifiers(my_mods)

