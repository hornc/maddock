# All tracery rules

with open('maddock/data/towns.txt', 'r') as f:
    towns = f.readlines()

rules = {
        'placename': towns,
        'indent': '\n\n' + '&nbsp;' * 6,
        'smallitem': ['hairbush', 'comb', '#solid# fob', '#solid# snuff-box', '#solid# snuff-box #filled#', '#container# #filled#',
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
        'itemaction': ['#adverb# fidgets with', 'nervously clutches', '#adverb# brandishes', 'is preocupied with', '#adverb# tosses in the air', '#chews# #adverb# on'],
        'itemadv': ['idly', 'nervously', 'distractedly', '#adverb#'],
        'chews': ['chews', 'nibbles', 'sucks',],

        # Character Interests
        'cinterest': ['stamp collecting', 'porcupines', 'animal husbandry', '#adjective# psycho-geography', 'French literature', 'the health problems of others',
                      'the political history of #placename#', '#compass# cuisine', 'the life and exploits of #saint#', 'the #adjective# effects of #snuff#'],

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
                 'There are #adjective# #smellsound# emanating from the #innloc#. The #C1# #says# #cleverthing#',
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

        'innevent': ['#animalsound#', '#innevent#. #innevent#', 'A patron spills #adjective.a# drink #adverb#', 'A small fight breaks out over by the #innloc#',
                'A #innanimal#, sitting under a table, gives itself #adjective.a# scratch #andext#',
                'The #staff# calls for #callthing#',
                'The #staff# is called away', '#someone# storms off', '#someone# is excused #adverb#',
                'The #company# remark upon #remarkable#',
                '#someone.capitalize# #puddleaction# #puddle.a#',
                '#indent#"Barkeep! What\'s in this food? It tastes like #fluid#!" someone #says# loudly. #react#',
                'The #C1#, starts talking about their interest in #interest#. #react#',
                '#interrupt# #int_response#', 
                ],
        'react': ['', '#someone.capitalize# #react1#', '#cleverthing# responds #someone#', '\n#indent#"I\'d rather consume #adjective# #fluid#" #says# #someone#'],
        'react1': ['nods in agreement', 'looks dissaproving', 'guffaws hysterically'],
        'someone': ['the #staff#', 'a patron', 'a surly drunk', 'a bystander', 'one of the #company#', 'the innkeeper'],
        'callthing': ['silence', 'more beer', 'more wine', 'a mop', 'some food', 'attention', 'assistance', 'last drink orders', 'someone to sing a song', 'their mother', 'a shoulder to cry on'],

        'staff': ['stable-hand', 'room-attendant', 'grounds-keeper', 'cook', 'scullery-hand', 'bar-staffer', 'assistant-manager', 'pastry-cook', 'pot-scrubber', 'attendant wait-server',
        'vinter', 'lounge-operative'],
        'remarkable': ['their situation', 'the weather', 'the journey so far', 'their surroundings', '#someone#', '#someone#\'s manner'],

        # Interrupt the teller
        'interrupt': ['#indent#"That\'s not how it happened at all!" interrupts the #C1#.',
                      '#indent#"But... that\'s not how I remember it..." #says# the #C1#.',],

        'int_response': ['The #teller_title# (who is the current storyteller) glares witheringly at the #C1title#, indignant at the #adjective# inerruption, then resumes the tale.',
                         '#indent#"#ctexclaim#" #says# the #C2#, "Let the #teller_title# finish the tale!"'],


        # Weapon
        'weapon': '\n\nAbove the mantle hangs a vicious looking #WEAPON#. #wlabel#',
        'wlabel': ['', 'Next to it is a small #label#. #labelreads#.', 
                   '#innfamily.capitalize# notices the #company# glancing at the #WEAPON# and #moves# over, with #adjective.a# gleam. #wstory#'],
        'label': ['label', 'scrap of parchment', 'plaque', 'luggage tag', 'bronze plate', 'inscription carved in marble', 'baked clay tablet'],
        'labelreads': ['It reads: "((WEAPON)) of Chekhov #ldetail#"', 'It reads: "Chekhov\'s ((WEAPON)) #ldetail#"', 
                       'The inscription upon it is unfortunately obscured by what looks like stains of #fluid#',],
        'ldetail': ['', 'which Chekhov #obtained# #wtime# the #wfrom# #date#'],
        'innfamily': ['the innkeeper', 'the innkeeper\'s #closerelation#'],
        'wstory': '\n#indent#"This #WEAPON# used to belong to my #wperson# #wname#."\n\n#weapreact#',
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
        'crop': ['wheat', 'grape', 'maize', 'barley', 'turnip', 'potato', 'chickweed', 'jimsonweed', ''],
        'weapreact': ['The #company# listen and are #adverb# impressed.', ],

        # Close by, or far away, a raven makes a sound, is seen, or unobservedly does something characteristic yet poignant.
        'animalsound': '#andistance# #animal.a# #andoes#',
        'andistance': ['Off in the distance,', 'Nearby', 'Seemingly emanating from an upstairs room,',],
        'andoes': ['makes #adjective.a# sound #andext#', 'is heard by the #company#', 'makes its presence felt #andext#'],
        'andext': ['', 'as if it were #adjective#',],
        'animal': ['#innanimal#', '#outanimal#'],
        'innanimal': ['cat', 'dog', 'fly', 'parrot', 'crow', 'raven', 'owl', 'falcon', 'hawk', 'thrush', 'dormouse', 'rat', 'mouse', 'vole', 'cockroach', 'deathwatch beetle'],
        'outanimal': ['dung beetle', 'fly', 'lac beetle', 'mantis', 'moth', 'horse', 'donkey', 'mule', 'cow', 'ox', 'sheep', 'lamb', ],

# Presently the Innkeeper (or possibly another staff member such as the vinter or pot-scrubber) undulates over to take their orders. Available impressive offerings are listed, questioned, and chosen; comprising and/or consisting of food and / or drinks. There is indecision, and certainty. Once all orders are made, the group settles in to wait. Drinks may arrive, but the food takes time to prepare.
        'menu': 'Presently the #foodserver# #moves# over to take the #company#\'s orders. #takeorder#',
        'foodserver': ['inkeeper', '#staff#'],
        'takeorder': ['#menuyes#', '#menuno#'],
        'menuno': ['#menunsays#\n\n #menunresponse#\n\n',],
        'menunsays': ['#indent# "#menunreason#, you\'ll just have to order drinks. What\'ll it be?"\n',],
        'menunreason': ['Kitchen\'s closed', 'Cook\'s dead', 'We\'re all out of food, sorry', 'I don\'t think you lot\'ll have the stomach for our #compass# fare'],
        'menunresponse': 'The #company# look dissapointed, but order their drinks.',
        'menuyes': '#indent# #menuysays#.\n\n #menuyresponse#',
        'menuysays': ['"Right, what do you lot want?"', '"Can I interest you in some #menusummary#?"', '"This is our menu, you won\'t find better fare within #num# #distance# of these walls!"',],
        'menuyresponse': ['The #company# order food. #foodevent#', 'Presently the #company# place their orders. #foodevent#'],
        'foodevent': ['The #C1#, complains about allergies.#indent#"I am very allergic to #fluid#!" the #C1title# #says#. #react#', 'The #C1#, places orders for all the #company#.', 'The #company# order their meals indivdually, it takes a long time.',
                      '#innevent#. #indent#"#ctexclaim# We are trying to order food!" #says# the #C1#, #adverb#.', ],
        'num': ['three', 'one score', 'five score', 'three score and six', 'more than I can count', 'some number of', 'many', 'a fair few', 'much more than #num#'],
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
                  'lavender scented unguent', 'rose-water', 'aqua vitae', 'aqua regia', 'formic acid', 'mercury', ],


        'nexttale': '\n\nIn order to entertain themselves, #ntsub#, the #company# decide to pass the time telling stories, and chose from their number one person to tell this evening\'s tale...',
        'ntsub': ['as is their custom on this journey', 'as they have done every evening previously', 'as tradition dictates', 'since no other alternatives are on offer', 'because the night is young'],

        # Addressing the Innkeeper
        'innloc': ['corner', 'fireplace', 'door', 'storeroom', 'kitchen', 'stairs', 'window', 'bar', 'counter', 'main room', 'coat rack', 'rug'],
        'addressinnkeeper': '\n#addrik# #descinnk# #respinnk#',
        'addrik': ['#indent#"#ctexclaim# Look over there by the #innloc#; there is the innkeeper, looking rather #ikpersonality#. Let us talk to #ikpro#!" #says# the #C1#.',
                   'The #company# approach the innkeeper #adverb#, who is busy with something over by the #innloc#.',
                   '#indent#"#ctexclaim# We are but #number# weary travellers in need of lodging and good cheer!" #says# the #C1#.',],
        'descinnk': '\nThe innkeeper, #ik#, has a #ikpersonality# personality, and some #inndchoice# #inndimpart# to impart.',
        'inndimpart': ['advice', 'news', 'rumours', 'moralising', 'complaints'],
        'inndchoice': ['choice adjectives and', '#adjective#', 'and #inndchoice#', 'worldly', '#adjective# #adjective#'],
        'respinnk': ['#indent#"#respa#, #respb#..."', 'Then suddenly, without a word, the innkeeper impatiently waves the #company# to a table.'],
        'respa': ['Sit down over there', 'Grab yourselves a table', 'Be seated', 'Get ye gone'],
        'respb': ['I\'ll be with you shortly to take orders', 'I\'ll send someone over to take your orders'],
        'ctexclaim': ["A!", "Abyde!", "Alas!", "Aleyn!", "Allas!", "Anne!", "Avoy!", "Brok!", "Crist!", "Ey!", "Fy!", "Gyle!", "Ha!", "Help!", "Ho!", "How!", "I!", "Iame!", "Iape!", "Iesus!", "Ioce!", "Iohn!", "Ioye!", "John!", "Lady!", "Lo!", "Loy!", "Marie!", "Mercy!", "Nay!", "O!", "Out!", "Ow!", "Parde!", "Pees!", "Peter!", "Scot!", "Straw!", "Tehee!", "What!", "Ye!"],

        # Character interactions
        'talk': 'The #C1#, talks to the #C2#, about #interest#.',
        'talkpos': ['The #C2short# listens attentively and responds with vigorous enthusiasm.' '#indent#"I have had a great curiosity about #interest# since the days of my youth, when I studied in #placename#. This is exceptionally enlightening!" effusively exudes the #C2short#.\n'],
        'talkneg': ['The #C2short# looks exceedingly bored.', '#indent#"Really? You dare talk to me about #interest#?"',],

        'neutral': ['The #C2short# appears nonplussed.'],

        # Outfit
        'outfitneg': 'The #C1#, insults the #C2#\'s #C2outfit#.',
        'outfitpos': 'The #C1#, compliments the #C2#\'s #C2outfit#. #outfitpos2#',
        'outfitpos2': ['', '#indent#"Your #C2outfit# is so much more #adjective# than my meager #C1outfit#!" #says# the #C1title#.\n\n'],

        # Witness
        'witness': ['The #C1#, #observes# and #wreact#.', 'The #C1#, #observes# in #obsadj#.'],
        'observes': ['observes', 'witnesses', 'looks on', 'notices this', 'registers this interaction', 'cannot help noticing', 'cannot ignore the exchange',
                     'looks on', 'observes', 'bears witness', 'eavesdrops', 'spies this', 'listens in', 'is a witness to this'],
        'wreact': ['is jealous', 'is amused', 'does not understand', 'dies a little inside', 'modifies their opinions and beliefs accordingly'],
        'obsadj': ['disgust', 'sympathy', 'resignation', 'confusion', 'solidarity', 'anger', 'despair', 'amusement', 'barely contained #adjective# rage', 'abject jealously', ],

        'swap': 'The ((C1)), and the ((C2)), set down to the business of trading. The ((C1title)) swaps a ((i1)) for the ((C2title))\'s ((i2)).',
        'give': 'The ((C1)), gives a ((i1)) to the ((C2)).',
        'get': 'The ((C1)), is given a ((i2)) by the ((C2)).',

        'witness_fore': ['The #C1# witnesses #adjective.a# interaction, and #wreact#.', 'In full view of the #C1#, who #wreact# as a result, the following event takes place:',
                         'The #C1# bears witness to the following #adjective# interaction bewtween two other of the #company#:'],

        # Songs
        'goodsong': 'The ((C2)) listens #adverb#, enraputured by the ((C1title))\'s #adjective# voice.',
        'badsong': '#indent#"Cease your #adjective# #noise#!", #says# the ((C2)), interupting the ((C1title)) rudely.',
        'noise': ['caterwauling', 'noise', 'mewling', 'banshee-screeching', 'howling', 'drivel', 'racket'],

        # Challenge the Teller
        'challenge': '#indent#"#ctexclaim# No! Not the #C1# again!" #says# the #C2#, "Let\'s hear the #C3#, instead!" #chagree#',
        'chagree': 'After some #adjective# discussion and bickering, the #company# agree #adverb# to hear the #C3#, over the #C1#.\n',


        # Cinna Facts:
        'cinnafact': ['not to be confused with #othercinna#, #othercinnafact#', 'the poet', 'the neoteric poet', 'author of the poem "Zmyrna"', 'that is Helvius Cinna, the neoteric poet, not to be confused with #othercinna#, #othercinnafact#',
                      '#cinnafact2#', '#cinnafact2# and #cinnafact2#'],
        'cinnafact2': ['who was murdered at the funeral of Julius Caesar after being mistaken for an unrelated #othercinna#, #othercinnafact#',
                      'of whom Shakespeare wrote in act three of his famous play _Julius Ceasar_: "#shakequote#"',
                      'author of the poem "Zmyrna"',
                      'who Ovid included in his list of celebrated erotic poets and writers',
                      'friend of Catullus',],
        'othercinna': ['Lucius Cornelius Cinna', 'Lucius Cinna, the politician', 'Lucius Cornelius Cinna' ],
        'othercinnafact': ['who sought better fortune for himself by joining the failed rebellions of Lepidus and Sertorius', 
                           'who came from a noble family which had gained prominence during the civil wars of the 80s BC',
                           'who gave a famous speech in support of the assasination of Julius Ceasar',
                            '#othercinnafact# and #othercinnafact#', ],
        'shakequote': ['Truly, my name is Cinna.', 'Tear him to pieces; he\'s a conspirator!!!', 'I am Cinna the poet; I am Cinna the poet!', 'Tear him for his bad verses, tear him for his bad verses!', 'I am not Cinna the conspirator!',
                       'It is no matter, his name\'s Cinna! Pluck but his name out of his heart, and turn him going!']

}
