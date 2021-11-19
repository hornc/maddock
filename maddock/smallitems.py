# small items, for loading into pytracery

rules = {
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
        'quality': ['', 'finest', 'cheapest', 'meanest', 'expensive', 'regal', 'incomparably excellent', 'astounding', 'unparalled'], 


        # Item actions
        'itemaction': ['fidgets with', 'nervously clutches', '#adverb# brandishes', 'is preocupied with', 'idly tosses in the air', 'chews distractedly on'],



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
        'hall': ['#C1#\'s #C1outfit# catches on a #snag#',
                 '#C1# stops briefly to admire their #C1outfit# in a mirror placed in the entranceway',
                 'There are #adjective# #smellsound# emanating from the #innloc#. #CR# #says# #cleverthing#',
                 'The #company# notice #adjective# marks upon the walls',],
        'smellsound': ['smells', 'sounds'],
        'snag': ['hook', 'exposed nail', 'splintered floor-board', 'coat-stand', 'umbrella, conviniently made available for guests who may have neglected to bring their own'],
        'says': ['quips', 'laughs', 'jokes', 'whispers', 'snarls'],
        'cleverthing': ['"I\'d like some of that!"', 'I have no idea what that is.'],
        

        # Inn interior
        'innside': ['#inntro# #is# #innadj#.'],
        'inntro': ['The interior of XXX', ],
        'is': ['is the embodiment of', 'appears to be the epitome of', 'suggests', 'compells them forward with its', 'repells them with its'],
        'innadj': ['warmth', 'welcoming #innadj#', '#innadj# and #innadj#', 'coziness', 'darkness', 'dankness', 'smokiness', 'chasteness', 'austerity', 'opulence', 'chaos', 'order'],

        'innevent': ['#animalsound#', '#innevent#. Additionally, #innevent#', 'A patron spills a drink', 'A small fight breaks out in the corner',
                'A dog, sitting under a table, gives itself #adjective.a# scratch #andext#',
                'The #staff# calls for #callthing#',
                'The #staff# is called away.', '#someone# storms off.', '#someone# is excused',
                'The #company# remark upon #remarkable#',
                #Someone may be called away, or storm off, or otherwise be excused.
                ],
        'someone': ['the #staff#', 'a patron', 'a surly drunk', 'a bystander', 'one of the #company#', 'the innkeeper'],
        'callthing': ['silence', 'more beer', 'more wine', 'a mop', 'some food', 'attention', 'assistance', 'last drink orders', 'someone to sing a song', 'their mother', 'a shoulder to cry on'],

        'staff': ['stable-hand', 'room-attendant', 'grounds-keeper', 'cook', 'scullery-hand', 'bar-staffer', 'assistant-manager', 'pastry-cook', 'pot-scrubber', 'attendant wait-server',
        'vinter', 'lounge-operative'],
        'remarkable': ['their situation', 'the weather', 'the journey so far', 'their surroundings', '#someone#', '#someone#\'s manner'],

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
        'takeorder': 'Available #menusummary# are listed, questioned, and chosen; comprising and/or consisting of food and / or drinks. There is indecision, and certainty. Once all orders are made, the #company# settles in to wait. Drinks may arrive, but the food takes time to prepare.',
        'menusummary': ['goods', 'victuals', 'bare necessities', 'gourmet offerings', 'foul sounding slops', 'provisions', 'tasty treats', 'servicable foodstuffs', 'sweetmeats', 'hearty pub meals',
                'pretentious sounding dishes', 'swillish slops', 'delicious delights', 'yummies', 'standard offerings', 'uninspring offerings', 'disapointing selections', 'impressive offerings',
                'forgettable fare'],


        'moves': ['walks', 'strides', 'saunters', 'sashays', 'slinks', 'slithers', 'bounds', 'traipses', 'stumbles', 'catapults', 'zips',
             'bumbles', 'moves', 'charges', 'speeds', 'wriggles', 'undulates', 'sprints', 'shoots', 'scoots', 'dances', 'leaps'],
}
