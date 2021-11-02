# Þys Maddock

NaNoGenMo 2021

This year I am attempting a simulated story generator. In previous NaNoGenMos I've focused on
methods of text generation through code, where any resulting 'story' is a happy accident, or secondary to some 
feature of the code or *quantity* of text. This year I want to focus on generating *story* rather than just
words... 

### Inspiration
This story is to be a recursive storytelling simulation, inspired variously by: 
* [The Canterbury Tales](https://en.wikipedia.org/wiki/The_Canterbury_Tales),
* John Fowles' [A Maggot](https://en.wikipedia.org/wiki/A_Maggot) (at least the first few pages, it's initial scene, and some discussion of his writing and obsession with that scene I half remember reading somewhere (have not read the full book)).
* [Rashomon](https://en.wikipedia.org/wiki/Rashomon), for the repetition of stories, but here rather than differing recollections, the characters' stories are in some
abstract sense *prescriptive* and shape their reality, and 
* [The Saragossa Manuscript](https://en.wikipedia.org/wiki/The_Saragossa_Manuscript_(film)), for stories-within-stories (yes, ok, I haven't read that book either, just seen the film...).
* Other public entries and ideas for story and game-like simulations from past NaNoGenMos. There are multiple, but the ealiest one that stuck in my head and got me thinking about this sort of thing first was Chris Pressy's 2018 effort: [The League of Extraordinarily Dull Gentlemen](https://github.com/NaNoGenMo/2018/issues/6). I am probably going to do less detail and aim for more character motivation, if things work out.


### Goals
The characters should have personalities, which are revealed or developed over the course of the novel, and be in control of their own destinies within the constraints of the story environment and the 'rules' of the story.

The Inn (the main setting) should be a character. Most surface, trivial, details about the Inn change at every telling, but some core aspects of the Inn will remain and develop across the story. Some because they are modelled, and others will hopefully form in the mind of the reader from reading the played out interations. 

Characters should be playing to win (motivation), against each other and the environment, although I can't quite figure out what the 'game' looks like yet. Hopefully the logic of this will reveal itself and come together as the story progresses. When characters are telling their story, they have some power over the others, and the environment, but it is constrained by some rules... somehow other characters still retain some ability to react *within* another's story. (still working on this idea... )

Explore redaction, vagueness, and ambivalence as a way to allow the reader to fill in interesting blanks which will probably make more sense and be more satisfying that randomly generating some specific non-sense. Specifically using the technique of redacted names, which were used in some older novels to imply real-world people's identities are being protected, therefore the story is *real*. i.e "J____ S____ is an very discerning gentleman..." .

Recursion.

Not too much focus on techniques, more on output, but L-systems and generative grammars seem like they'd be helpful concepts to keep in mind. I'll probably just hack some code and corpora together quickly so that it kind of works, and explore and optimise the ideas later (next year?).

DIY; let's re-invent some wheels so I can see what works and how. Not particularly concerned with discovering or learning existing tools here, the resulting code may not be groundbreaking or the best example of anything. I just want to quickly explore some simulation ideas to see what works and doesn't. Experimentation!


## Dev Diary

### 02 Nov 2021
Late night hacking a basic skeleton of the concept together from some thoughts I had immediately after Nov 2020. Main pieces of the story named and loosley described. Looping / recursion implemented.
Character numbers at least decrease now, with the idea that the last one is somehow the *winner*, and the story has a *direction*. The game mechanic still needs to be made consistent and more coherent. Redacted naming used in various places. Spacing and punctuation is messy.

17K word output, although a lot of that is bolierplate filler. Need to work in a better structure now the concept is taking shape. Now detail can be added *within* the various components.

#### Sample:

>Twenty-four brave travellers make their way by ocean going vessel towards *The D_____ Q____* Inn.
It is barely foggy.
First is the sincere but miserable real estate broker followed by the youthful but suspicious physician assistant, followed by the elated but stern wood patternmaker, followed by the wishful but not so lame bill and account collector, followed by the shunned but not so warm dental laboratory technician, followed by the tepid but not so quick meter reader, followed by the spunky but competent clinical laboratory technologist, followed by the suffocated yet drowsy life scientist, followed by the stressed -cum- well-rounded musician, followed by the bold and stern psychiatric aide, followed by the perplexed -cum- quiet craft artist, followed by the replaced and drowsy geography teacher, followed by the neurotic and serious stock mover, followed by the nasty nonetheless insensitive hand laborer, followed by the ignored  ambitious ceiling tile installer, followed by the faithful but not so cowardly traffic technician, followed by the manipulated yet serene tour guide, followed by the burned-out but flashy hunter, followed by the ashamed and arguably maternal mining safety engineer, followed by the pensive and crafty tool sharpener, followed by the enriched but circumspect forestry teacher, followed by the disgraced but not so blue forester, followed by the innovative and lively automotive glass installer, followed by the sunk but not so attentive foreign language teacher,.
The intrigued but stern physician assistant, O______  interacts with the crappy and arguably cynical tool sharpener, C_______
It is a neutral interaction.
The trembly but not so drowsy craft artist, T_____ does not understand .
The impatient but well-behaved physician assistant, O______  interacts with the threatened and stupid ceiling tile installer, F_____
It is a neutral interaction.
The glorious and obliging meter reader, Y_____ does not understand .
As they near their destination, they notice  the Inn's sign depicts a Q____ which appears exceedingly D_____. The sign is covered with a slow moisture in the fog.
The group feels forgotten as they approach the entrance to the inn.

>The trapped but not so sensitive craft artist, T_____ enters the inn first {description}.
The obligated and arguably drunk real estate broker, L_______ reacts {reaction}. {supplementary reaction from a third individual or the group}
Inside, the inn is really awesome and well described.
The travelers interact with the Inn in an interesting and satisfying way.
Close by, or far away, a horse makes a sound, is seen, or unobservedly does something characteristic yet poignant.
"Oh look, over there by the counter; there is the innkeeper, looking rather lethargic. Let us talk to him!" says the foolish nonetheless great ceiling tile installer, F_____.
The innkeeper, G________, has a lethargic personality, and some worldly advice to impart (if the mood takes him).
"Grab yourselves a table, and I'll be with you shortly to take orders..."
The weary travellers sit at a knowledgeable table.
They have some interactions, and remark upon their situation.
The amazed and short-tempered wood patternmaker, E_______  interacts with the hateful and cordial tool sharpener, C_______
It is a positive interaction.
The persecuted but not so timid life scientist, M____ is amused .
The trustful -cum- egotistical traffic technician, I____  interacts with the okay nonetheless stable clinical laboratory technologist, F____
It is a negative interaction.
The insecure nonetheless well-rounded forester, S_______ looks on in disgust .
Possibly, something notable happens. What is the outcome?
Someone may be called away, or storm off, or otherwise be excused.
Presently the Innkeeper (or possibly another staff member such as the bar-staffer or pot-scrubber) scoots over to take their orders.
Available yummies are listed, questioned, and chosen, comprising and/or consiting of food and / or drinks. There is indecision, and certainty.
Once all orders are made, the group settles in to wait. Drinks may arrive, but the food takes time to prepare.
Something happens in the main room.
In order to entertain themselves, as is their custom on this journey, they decide to pass the time telling stories,  and chose from their number one person to tell this evening's tale...
The delicate yet unmotivated bill and account collector, Q________ waits for the chatter to subside and begins her tale...

> ### The Bill And Account Collector's Tale
>Twenty-three optimistic travellers make their way by carriage towards *The I____ L_____* Inn. It is very stormy.
>...


