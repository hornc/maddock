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
}
