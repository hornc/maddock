# All tracery rules

with open('maddock/data/towns.txt', 'r') as f:
    towns = f.readlines()

rules = {
        'placename': towns,
        'indent': '\n\n' + '&nbsp;' * 6,
        'smallitem': ['hairbush', 'comb', '#solid# fob', 'snuff-box', '#solid# snuff-box #filled#', '#container# #filled#',
            '#threadform# of #color# #thread#', '#solid# mirror', 'small coin', '#color# glass bead', 'small #solid# disc', 'hair pin', 'pocket knife with a #solid# handle',
            'reliquary housing fragments of the #side# #bone# of #saint#',
            ],
        'solid': ['wooden', 'metal', 'jeweled', 'tin', 'battered'],
        'filled': ['', 'filled with #quality# #snuff#', 'containing #quality# #snuff#', 'tightly packed with #quality# #snuff#',],
        'snuff': ['tobacco', 'snuff', 'laudanum', 'jimson-weed', 'lint', 'ash', "sheep's wool", 'pastry crumbs'],
        'container': ['phial', 'purse', 'container', 'box', 'sachet', 'satchel', 'bag', 'glove',],
        'threadform': ['scrap', 'skein', 'ball', 'twist', 'knot', 'fragment', 'fillament'],
        'color': ['red', 'blue', 'yellow', 'tan', 'purple', 'black', 'pale', 'aquamarine', 'turquoise'],
        'thread': ['string', 'yarn', 'wool', 'cloth', 'silk', 'embroidery wool', 'cotton', 'hemp', 'linen'],
        'side': ['left', 'right'],
        'bone': ['thigh', 'femur', 'tibia', 'clavicle', 'ulnar', 'finger', 'cranial hemisphere'],
        'saint': ['Saint #sname# of #splace#', 'an unknown #stype#', ],
        'stype': ['fanatic', 'martyr', 'saint', 'apostate', 'zealot',],
        'sname': ['Thomas', 'Judith', 'Stephen', 'Aedesius', 'Chad', 'Alban', 'Dunstan', 'Ioannis'],
        'splace': ['Antioch', 'the #color# fields', 'Abington', 'Durham', 'the venerable temperament', 'somewhere exotic', '#compass# parts',],
        'compass': ['eastern', 'western', 'northern', 'southern', 'foreign', 'local', 'exotic', 'distant', ],
        'quality': ['', 'finest', 'cheapest', 'meanest', 'expensive', 'regal', 'incomparably excellent', 'astounding', 'unparalleled'],


        # Item actions
        'itemaction': ['fidgets with', 'nervously clutches', '#adverb# brandishes', 'is preocupied with', 'idly tosses in the air', 'chews distractedly on'],

        # Character Interests
        'cinterest': ['stamp collecting', 'porcupines', 'animal husbandry', '#adjective# psycho-geography', 'French literature', 'the health problems of others'],

        # Clothing
        'outfit': ['#cadj# #citem#', '#cadj# #citem# made of #quality# #cmaterial#'],
        'cadj': ['flowing', '#color#', 'elegant', 'tattered', 'worn', 'dirty', 'moth-eaten', 'odure-stained', 'stained', 'voluminous',],
        'citem': ['dress', 'overcoat', 'frock-coat', 'hauberk', 'suit', 'robe', 'rags', 'livery', 'oufit', 'costume', 'gown', 'bathing cosutme', 'safari suit', '#color# #citem#'],
        'cmaterial': ['burlap', 'silk', 'linen', 'fabric', 'velour', 'chainmail', 'leather', 'seerskin', 'leopard print', 'cotton', 'needlepoint', 'embroidered #cmaterial#', 'goatskin',
            'crocodile leather', ],

        # Going Inn
        'company': ['group', 'cavalcade', 'party', 'travellers', 'wanderers', 'troupe', 'company'],
        'goinginn': '%s leads the #company# and enters the inn first, #entry#. #hall#.',
        'entry': ['stooping low to enter via the #doorway#', 'striding gallantly through the #doorway#', 'impatiently beckoning the #company# to follow through the #doorway#'],
        'doorway': ['doorway', '#door# door'],
        'door': ['rough hewn', 'glass paned', 'sturdy', 'stout', 'ramshackle', 'reinforced', 'suspisiously missing', 'negligently ajar'],
        'hall': ['The #C1#\'s #C1outfit# catches on a #snag#',
                 'The #C1# stops briefly to admire their #C1outfit# in a mirror placed in the entranceway',
                 'There are #adjective# #smellsound# emanating from the #innloc#. #CR# #says# #cleverthing#',
                 'The #company# notice #adjective# marks upon the walls',],
        'smellsound': ['smells', 'sounds'],
        'snag': ['hook', 'exposed nail', 'splintered floor-board', 'coat-stand', 'umbrella, conviniently made available for guests who may have neglected to bring their own'],
        'says': ['quips', 'laughs', 'jokes', 'whispers', 'snarls'],
        'cleverthing': ['#indent#"I\'d like some of that!"', '#indent#"I have no idea what that is."'],
        

        # Inn interior
        'innside': ['#inntro# #inn_is# #innadj#.'],
        'inntro': ['The interior of XXX', ],
        'inn_is': ['is the embodiment of', 'appears to be the epitome of', 'suggests', 'compells them forward with its', 'repells them with its'],
        'innadj': ['warmth', 'welcoming #innadj#', '#innadj# and #innadj#', 'coziness', 'darkness', 'dankness', 'smokiness', 'chasteness', 'austerity', 'opulence', 'chaos', 'order'],

        'innevent': ['#animalsound#', '#innevent#. Additionally, #innevent#', 'A patron spills a drink', 'A small fight breaks out in the corner',
                'A dog, sitting under a table, gives itself #adjective.a# scratch #andext#',
                'The #staff# calls for #callthing#',
                'The #staff# is called away', '#someone# storms off', '#someone# is excused',
                'The #company# remark upon #remarkable#',
                '#someone.capitalize# #puddleaction# #puddle.a#',
                '#indent#"Barkeep! What\'s in this food? It tastes like #fluid#!" someone #says# loudly #react#',
                'The #C1#, starts talking about their interest in #interest#. #react#',
                #Someone may be called away, or storm off, or otherwise be excused.
                ],
        'react': ['', '. #someone.capitalize# #react1#', '#innevent# in response', '. #cleverthing# responds #someone#', '\n#indent#"I\'d rather consume #adjective# #fluid#" #says# #someone#'],
        'react1': ['nods in agreement', 'looks dissaproving', 'guffaws hysterically'],
        'someone': ['the #staff#', 'a patron', 'a surly drunk', 'a bystander', 'one of the #company#', 'the innkeeper'],
        'callthing': ['silence', 'more beer', 'more wine', 'a mop', 'some food', 'attention', 'assistance', 'last drink orders', 'someone to sing a song', 'their mother', 'a shoulder to cry on'],

        'staff': ['stable-hand', 'room-attendant', 'grounds-keeper', 'cook', 'scullery-hand', 'bar-staffer', 'assistant-manager', 'pastry-cook', 'pot-scrubber', 'attendant wait-server',
        'vinter', 'lounge-operative'],
        'remarkable': ['their situation', 'the weather', 'the journey so far', 'their surroundings', '#someone#', '#someone#\'s manner'],


        # Weapon
        'weapon': '\n\nAbove the mantle hangs a vicious looking #WEAPON#. #wlabel#',
        'wlabel': ['', 'Next to it is a small #label#. #labelreads#.', 
                   '#innfamily.capitalize# notices the #company# glancing at the #WEAPON# and #moves# over, with #adjective.a# gleam. #wstory#'],
        'label': ['label', 'scrap of parchment', 'plaque', 'luggage tag', 'bronze plate', 'inscription carved in marble', 'baked clay tablet'],
        'labelreads': ['It reads: "((WEAPON)) of Chekhov #ldetail#"', 'It reads: "Chekhov\'s ((WEAPON)) #ldetail#"', 
                       'The inscription upon it is unfortunately obscured by what looks like stains of #fluid#',],
        'ldetail': ['', 'which Chekhov #obtained# #wtime# the #wfrom# #date#'],
        'innfamily': ['the innkeeper', 'the innkeeper\'s #closerelation#'],
        'wstory': '\n#indent#"This #WEAPON# used to belong to my #wperson# #wname#."\n\n',
        'wperson': ['#closerelation#','#closerelation#', '#closerole#',
                    '#wperson#\'s #wperson#',
                    '#wperson# who got it from their #wperson#',
                    '#wperson# who #obtained# it #wtime# the #wfrom# #date#. Before that, it belonged to #fadj.a# #famous#, who #fgot# it from their #wperson#'],
        'fgot': ['inherited', 'acquired', 'got', 'was gifted', 'had it passed on to them'],
        'fadj': ['renowned', 'famous', 'loyal', 'enemy', 'gifted', 'wealthy', 'remarkable', 'esteemed', '#compass#'],
        'famous': ['Duke', 'Duchess', 'Captain', 'Noble', 'scholar', 'warrior', 'citizen', 'courtesan', 'cleric', 'merchant', 'orator'],
        'obtained': ['won', 'stole', 'found', 'liberated', 'traded for', 'earned', 'was awarded', 'uncovered', 'performed services in payment for', 'committed serious crimes for'], 
        'wfrom': ['#madj# #militaryevent# of #placename#'],
        'wtime': ['during', 'after', 'in the months after', 'in the preparations for', 'while looting in the wake of', ],
        'militaryevent': ['siege', 'liberation', 'defence', 'destruction', 'battle', 'campaign'],
        'closerole': ['doctor', 'commanding officer', 'lieutenant', 'captain', 'priest', 'confessor', 'acquaintance', 'cook', 'bondsman', 'servant', 'comrade-in-arms'],
        'closerelation': ['father', 'mother', 'brother', 'sister', 'lover', 'spouse', 'grandfather', 'grandmother', 'uncle', 'aunt', 'cousin'],
        'wname': ['whose name was Chekhov', 'whose name is unfortunately long forgotten',
                  'who is commonly known, in #compass# parts at least, as Chekhov',
                  'who went by the name of "Chekhov"'],
        'madj': ['tragic', 'joyous', 'victorious', 'horrendous', 'famed', 'fabled', 'renowned', 'last', 'first', 'disasterous', 'ill-fated', 'botched', 'bungled', 'decisive', 'virtuous'],
        'date': ['', ', which occurred in the year of the #dateevent#'],
        'dateevent': ['#adjective# #animal#', "failed #crop# harvest", "bountiful #crop# harvest", "plague of #animal.s#", '#compass# drought'],
        'crop': ['wheat', 'grape', 'maize', 'barley', 'turnip', 'potato', 'chickweed', ''],

        # Close by, or far away, a raven makes a sound, is seen, or unobservedly does something characteristic yet poignant.
        'animalsound': '#andistance# #animal.a# #andoes#',
        'andistance': ['Off in the distance,', 'Nearby', 'Seemingly emanating from an upstairs room,',],
        'andoes': ['makes #adjective.a# sound #andext#', 'is heard by the #company#', 'makes its presence felt #andext#'],
        'andext': ['', 'as if it were #adjective#',],
        'animal': ['cat', 'dog', 'parrot', 'crow', 'raven', 'owl', 'falcon', 'hawk', 'thrush', 'dormouse', 'rat', 'mouse', 'vole', 'cockroach', 'deathwatch beetle',
        'dung beetle', 'fly', 'lac beetle', 'mantis', 'moth', 'horse', 'donkey', 'mule', 'cow', 'ox', 'sheep', 'lamb', ],

# Presently the Innkeeper (or possibly another staff member such as the vinter or pot-scrubber) undulates over to take their orders. Available impressive offerings are listed, questioned, and chosen; comprising and/or consisting of food and / or drinks. There is indecision, and certainty. Once all orders are made, the group settles in to wait. Drinks may arrive, but the food takes time to prepare.
        'menu': 'Presently the #foodserver# #moves# over to take the #company#\'s orders. #takeorder#',
        'foodserver': ['inkeeper', '#staff#'],
        'takeorder': ['#menuyes#', '#menuno#'],
        'menuno': ['#indent# #menunsays#\n #menunresponse#',],
        'menunsays': ['#indent# "#menunreason#, you\'ll just have to order drinks. What\'ll it be?"\n',],
        'menunreason': ['Kitchen\'s closed', 'Cook\'s dead', 'We\'re all out of food, sorry', 'I don\'t think you lot\'ll have the stomach for our #compass# fare'],
        'menunresponse': 'The #company# look dissapointed, but order their drinks.',
        'menuyes': '#indent# #menuysays#\n #menuyresponse#', 
        'menuysays': ['"Right, what do you lot want?"', '"Can I interest you in some #menusummary#?"', '"This is our menu, you won\'t find better fare within #num# #distance# of these walls!"',],
        'menuyresponse': 'The #company# order food.',
        'num': ['three', 'twenty', 'one hundered', 'four-hunnerd-an\' twen\'y summint', 'more than I can count', 'some number of', 'many', 'a fair few', 'much more than #num#'],
        'distance': ['feet', 'leagues', 'miles', 'counties', 'spans',],

            #'Available #menusummary# are listed, questioned, and chosen; comprising and/or consisting of food and / or drinks. There is indecision, and certainty.\n\n Once all orders are made, the #company# settles in to wait. Drinks may arrive, but the food takes time to prepare.',
        'menusummary': ['goods', 'victuals', 'bare necessities', 'gourmet offerings', 'foul sounding slops', 'provisions', 'tasty treats', 'servicable foodstuffs', 'sweetmeats', 'hearty pub meals',
                'pretentious sounding dishes', 'swillish slops', 'delicious delights', 'yummies', 'standard offerings', 'uninspring offerings', 'disapointing selections', 'impressive offerings',
                'forgettable fare'],


        'moves': ['walks', 'strides', 'saunters', 'sashays', 'slinks', 'slithers', 'bounds', 'traipses', 'stumbles', 'catapults', 'zips',
             'bumbles', 'moves', 'charges', 'speeds', 'wriggles', 'undulates', 'sprints', 'shoots', 'scoots', 'dances', 'leaps'],

        # Fluids
        'puddleaction': ['gingerly steps over', 'narrowly avoids stepping in', 'falls, drunk, into', 'creates', 'mops up', 'draws attention to', 'looks quizically at'],
        'puddle': 'puddle of #puddleadj1# #fluid#',
        'puddleadj1': ['', '#puddleadj#', '#puddleadj#', '#puddleadj#', '#puddleadj# and #puddleadj#'],
        'puddleadj': ['slowly spreading', 'dried', 'deliberately spilled', 'acidentally spilled', 'fresh', 'stale', 'coagulating', 'effervescing', 'quiescent', 'stagnant', 'flowing'],
        'fluid': ['#fluid# and #fluid#', '#fluid# mixed with a tiny amount of #fluid#', 'piss', 'shit', 'vomit', 'ale', 'wine', 'gin', 'purl', 'mead', 'honey', 'blood', 'ichor', 'rubbing alcohol', 'rainwater', 'seawater', 'slops', 'stew', 'fermenting fruit pulp', 'juice',
                  'lavender scented unguent', 'roser-water', 'aqua vitae', 'aqua regia', 'formic acid', 'mercury', ],


        'nexttale': '\n\nIn order to entertain themselves, #ntsub#, the #company# decide to pass the time telling stories, and chose from their number one person to tell this evening\'s tale...',
        'ntsub': ['as is their custom on this journey', 'as they have done every evening previously', 'as tradition dictates', 'since no other alternatives are on offer', 'because the night is young'],

        # Addressing the Innkeeper
        'addressinnkeeper': '#addrik# #descinnk# #respinnk#',
        'addrik': '#indent#"Oh look, over there by the {inn.feature()}; there is the innkeeper, looking rather {inn.keeper.personality}. Let us talk to {inn.keeper.pro}!" says the {choice(characters).dtitle}.',
        'descinnk': '\nThe innkeeper, {inn.keeper.name}, has a {inn.keeper.personality} personality, and some #inndchoice# #inndimpart# to impart.',
        'inndimpart': ['advice', 'news', 'rumours', 'moralising', 'complaints'],
        'inndchoice': ['choice adjectives and', '#adjective#', 'and #inndchoice#', 'worldly', '#adjective# #adjective#'],
        'respinnk': ['#indent#"#respa#, #respb#..."', 'The suddenly, without a word, the innkeeper impatiently waves the #company# to a table.'],
        'respa': ['Sit down over there', 'Grab yourselves a table', 'Be seated', 'Get ye gone'],
        'respb': ['I\'ll be with you shortly to take orders', 'I\'ll send someone over to take your orders'],


        # Character interactions
        'talk': 'The #C1#, talks to the #C2#, about #interest#.',
        'talkpos': ['The #C2short# listens attentively and responds with vigorous enthusiasm.' '#indent#"I have had a great curiosity about #interest# since the days of my youth, when I studied in #placename#. This is exceptionally enlightening!" effusively exudes the #C2short#.\n'],
        'talkneg': ['The #C2short# looks exceedingly bored.', '#indent#"Really? You dare talk to me about #interest#?"',],

        'neutral': ['The #C2short# appears nonplussed.'],

        # Outfit
        'outfitneg': 'The #C1# insults the #C2#\'s #C2outfit#.',
        'outfitpos': 'The #C1# compliments the #C2#\'s #C2outfit#. #outfitpos2#"',
        'outfitpos2': ['', '#indent#"Your #C2outfit# is so much more #adjective# than my meager #C1outfit#!" #says# the #C1title#.\n\n'],

        # Witness
        'witness': ['The #C1# observes this interaction and #wreact#.', 'The #C1#, looks on in disgust.'],
        'wreact': ['is jealous', 'is amused', 'does not understand'],

        'swap': 'The ((C1)) swaps a ((i1)) for the ((C2))\'s, ((i2)).',
        'give': 'The ((C1)) gives a ((i1)) to the ((C2)).',
        'get': 'The ((C1)) is given a ((i2)) by the ((C2)).',

        # Songs
        'goodsong': 'The ((C2)) listens, enraputured by the ((C1title))\'s #adjective# voice.',
        'badsong': '#indent#"Cease your #adjective# caterwauling!", #says# the ((C2)), interupting the ((C1title)) rudely.',

}
