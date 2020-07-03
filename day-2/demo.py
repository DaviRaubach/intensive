import abjad
from presentation import *
import abjadext.rmakers 
rmakers = abjadext.rmakers

def rotate(l, n):
    return l[-n:] + l[:-n]

### PRE ###

def show_demo():
    divisions = [(3, 8), (5, 4), (1, 4), (13, 16)]
    score = abjad.Score()
    counts = [1, 2, 3]
    selector = abjad.select().tuplets()[:-1]
    selector = selector.map(abjad.select().note(-1))

    for i in range(12):
    
        my_talea = rmakers.talea(
        counts, # counts
        16, # denominator
        extra_counts=[0, 1, 1]
        )
        
        voice = abjad.Voice()
    
        talea_rhythm_maker = rmakers.stack(
            my_talea, 
            rmakers.force_rest(abjad.select().logical_ties().get([0, -1]),),# Silences first and last logical ties.
            #rmakers.tie(selector), # Ties across divisions.
            rmakers.beam(), 
            rmakers.extract_trivial(),
            rmakers.rewrite_meter(), 
            )
        selections = talea_rhythm_maker(divisions)
        voice.append(selections)
    
        staff = abjad.Staff(lilypond_type='RhythmicStaff', name=str(i))
        staff.append(voice)
        score.append(staff)
        divisions = rotate(divisions, 1)
        counts = rotate(counts, 1)
    
    lilypond_file = make_sketch_lilypond_file(score)
    abjad.show(lilypond_file)

#show_demo()


### EXAMPLE ONE ###

note_rhythm_maker = rmakers.stack(rmakers.note(),) # abjadext.rmakers is implicit: rmakers = abjadext.rmakers
divisions = [(3, 8), (5, 4), (1, 4), (13, 16)]
selections = note_rhythm_maker(divisions)
staff = abjad.Staff(selections, lilypond_type='RhythmicStaff')
sketch = make_sketch(selections, divisions)
#abjad.show(sketch)

divisions_b = [(5, 16), (3, 8), (3, 8), (5, 8), (1, 4)]
sketch = make_sketch(selections, divisions_b)
#abjad.show(sketch)

divisions_b *= 20
selections = note_rhythm_maker(divisions_b)
sketch = make_sketch(selections, divisions_b)
#abjad.show(sketch)


import random
random_numerators = [random.randrange(1, 16 + 1) for x in range(100)]
random_divisions = [(x, 32) for x in random_numerators]
selections = note_rhythm_maker(random_divisions)
sketch = make_sketch(selections, random_divisions)
#abjad.show(sketch)



### EXAMPLE TWO ###

### INITIAL TALEA RHYTHM-MAKER

my_talea = rmakers.talea(
    [1, 2, 3], # counts
    16, # denominator
    )

talea_rhythm_maker = rmakers.stack(
    my_talea, rmakers.beam(), rmakers.extract_trivial(),
)

#You can see that the Talea creates a cycle of durations:

#for i in range(20):
   #print(i, my_talea[i])

#Next, we give this Talea to a stack:

talea_rhythm_maker = rmakers.stack(
    my_talea,
    rmakers.beam(), 
    rmakers.extract_trivial(),
)

selections = talea_rhythm_maker(divisions)
sketch = make_sketch(selections, divisions)
#abjad.show(sketch)

### SPECIFIERS
selector = abjad.select().tuplets()[:-1]
selector = selector.map(abjad.select().note(-1))

talea_rhythm_maker = rmakers.stack(
    my_talea, 
    rmakers.beam(), 
    rmakers.extract_trivial(),
    rmakers.tie(selector), # Ties across divisions.
)
my_talea = rmakers.talea(
    [1, 2, 3], # counts
    16, # denominator
    extra_counts=[0, 1, 1]
    )
selector = abjad.select().tuplets()[:-1]
selector = selector.map(abjad.select().note(-1))

talea_rhythm_maker = rmakers.stack(
    my_talea, 
    rmakers.force_rest(abjad.select().logical_ties().get([0, -1]),),# Silences first and last logical ties.
    rmakers.beam(), 
    rmakers.extract_trivial(),
    rmakers.rewrite_meter(),
    rmakers.tie(selector), # Ties across divisions.
)
selections = talea_rhythm_maker(divisions)
sketch = make_sketch(selections, divisions)
#abjad.show(sketch)


### EXAMPLE THREE ###
score = abjad.Score()

def rotate(l, n):
    return l[-n:] + l[:-n]

counts = [1, 2, 3]
selector = abjad.select().tuplets()[:-1]
selector = selector.map(abjad.select().note(-1))

for i in range(12):
    
    my_talea = rmakers.talea(
    counts, # counts
    16, # denominator
    extra_counts=[0, 1, 1]
    )
    
    voice = abjad.Voice()
    
    talea_rhythm_maker = rmakers.stack(
            my_talea, 
            rmakers.force_rest(abjad.select().logical_ties().get([0, -1]),),# Silences first and last logical ties.
            #rmakers.tie(selector), # Ties across divisions.
            rmakers.beam(), 
            rmakers.extract_trivial(),
            rmakers.rewrite_meter(), 
            )
    selections = talea_rhythm_maker(divisions)
    voice.append(selections)
    
    staff = abjad.Staff(lilypond_type='RhythmicStaff', name=str(i))
    staff.append(voice)
    score.append(staff)
    divisions = rotate(divisions, 1)
    counts = rotate(counts, 1)

sketch = make_sketch_lilypond_file(score)
#abjad.show(sketch)
