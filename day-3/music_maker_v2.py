import abjad
import abjadext.rmakers

# THIS IS THE INPUT TO MY MUSICAL IDEA
time_signature_pairs = [(4, 4), (3, 4), (7, 16), (6, 8)] * 10
counts = [1, 2, -3, 4, 1, 1, 1, 1, 2, 8]
denominator = 32
pitches = abjad.CyclicTuple([0, 1])


def make_basic_rhythm(time_signature_pairs, counts, denominator):
    # THIS IS HOW WE MAKE THE BASIC RHYTHM
    total_duration = sum(abjad.Duration(pair) for pair in time_signature_pairs)
    talea = abjadext.rmakers.Talea(counts=counts, denominator=denominator)
    talea_index = 0
    all_leaves = []
    current_duration = abjad.Duration(0)
    while current_duration < total_duration:
        leaf_duration = talea[talea_index]
        if leaf_duration > 0:
            pitch = abjad.NamedPitch("c'")
        else:
            pitch = None
        leaf_duration = abs(leaf_duration)
        if (leaf_duration + current_duration) > total_duration:
            leaf_duration = total_duration - current_duration
        current_leaves = abjad.LeafMaker()([pitch], [leaf_duration])
        all_leaves.extend(current_leaves)
        current_duration += leaf_duration
        talea_index += 1
    music = abjad.Container(all_leaves)
    return music


def clean_up_rhythm(music, time_signature_pairs):
    # THIS IS HOW WE CLEAN UP THE RHYTHM
    shards = abjad.mutate(music[:]).split(time_signature_pairs)
    for i, shard in enumerate(shards):
        measure = abjad.Measure(time_signature_pairs[i])
        abjad.mutate(shard).wrap(measure)
    return music


def add_pitches(music, pitches):
    # THIS IS HOW WE ADD PITCHES
    pitches = abjad.CyclicTuple(pitches)
    logical_ties = abjad.iterate(music).logical_ties(pitched=True)
    for i, logical_tie in enumerate(logical_ties):
        pitch = pitches[i]
        for note in logical_tie:
            note.written_pitch = pitch
    return music


def add_attachments(music):
    # THIS IS HOW WE ADD DYNAMICS AND ACCENTS
    for run in abjad.select(music).leaves().runs():
        if not isinstance(run[0], (abjad.Note, abjad.Chord)):
            continue
        abjad.attach(abjad.Articulation('accent'), run[0])
        if 1 < len(run):
            abjad.attach(abjad.Hairpin('p < f'), run)
        else:
            abjad.attach(abjad.Dynamic('ppp'), run[0])
    return music


def make_music(time_signature_pairs, counts, denominator, pitches):
    music = make_basic_rhythm(
        time_signature_pairs,
        counts,
        denominator,
        )
    music = clean_up_rhythm(music, time_signature_pairs)
    music = add_pitches(music, pitches)
    music = add_attachments(music)
    return music





























