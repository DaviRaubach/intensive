import abjad

def scale_and_chop_staff(voice_number, staff, time_signature):
    # Scales a staff's durations by a factor and then chops & ties everything at 3/4 measure boundaries.
    scale_factor = 2 ** voice_number
    copy = abjad.mutate(staff).copy()
    for leaf in copy:
        leaf.written_pitch -= voice_number * 12
    abjad.mutate(copy).scale(abjad.Multiplier(scale_factor, 1))
    abjad.mutate(copy[:]).split([time_signature], cyclic=True)
    return copy

def duplicate_music(num_copies, staff):
    #given an input staff, outputs a staff containing num_copies copies of input staff
    out_staff = abjad.Staff()
    for x in range(num_copies):
        out_staff.extend(abjad.mutate(staff).copy())
    return out_staff

def make_scaled_staves(melody_staff, time_signature):
    # make three scaled staves, each twice the duration of the last
    scaled_staves = []
    for voice_number in range(3):
      scaled_staff = scale_and_chop_staff(voice_number, melody_staff, time_signature)
      scaled_staves.append(scaled_staff)
    return scaled_staves

def duplicate_score(scaled_staves):
    score = abjad.Score()
    for scaled_staff, duplicate_index in zip(scaled_staves, reversed(range(3))):
        scale_factor = 2**duplicate_index
        staff = duplicate_music(scale_factor, scaled_staff)
        score.append(staff)
    return score

def format_score(score, key_signature, time_signature):
    for staff in score:
        key_sig = abjad.KeySignature(key_signature.tonic, key_signature.mode)
        abjad.attach(key_sig, staff[0])
        time_sig = abjad.TimeSignature(time_signature)
        abjad.attach(time_sig, staff[0])
    abjad.attach(abjad.Clef('bass'), score[2][0])

def make_canon(melody_staff, key_signature, time_signature):
    # make a three-voice prolation canon from a melody
    scaled_staves = make_scaled_staves(melody_staff, time_signature)
    score = duplicate_score(scaled_staves)
    format_score(score, key_signature, time_signature)
    return score

# # "Arirang"
melody_staff = abjad.Staff("e'4. fs'8 e'4 a'4. b'8 a' b' cs''4 b'8 cs''16 b' a'8 fs' e'4. fs'8 e' fs' a'4. b'8 a' b' cs'' b' a' fs' e' fs' a'4. b'8 a'4 a'2.")
melody_staff.extend("e''2 e''4 e'' cs'' b' cs'' b'8 cs''16 b' a'8 fs' e'4. fs'8 e' fs' a'4. b'8 a' b' cs'' b' a' fs' e' fs' a'4. b'8 a'4 a'2.")

for note in melody_staff:
    note.written_pitch += 12

score = make_canon(melody_staff, abjad.KeySignature('d', 'major'), abjad.TimeSignature((3,4)))
abjad.show(score)
