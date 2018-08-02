# -*- encoding: utf-8 -*-
import abjad
import abjadext.rmakers


def make_string_trio():
    rhythm_maker = abjadext.rmakers.TaleaRhythmMaker(
        talea=abjadext.rmakers.Talea(counts=[1, 2, 3, -1], denominator=8),
        )
    durations = [abjad.Duration(4, 4)] * 4
    score = make_empty_score()
    score = add_rhythms(score, rhythm_maker, durations)
    score = add_pitches(score)
    score = add_attachments(score)
    score = add_midi_instruments(score)
    lilypond_file = prettify_score(score)
    return lilypond_file


def make_empty_score():
    # Violin
    violin_voice = abjad.Voice()
    violin_staff = abjad.Staff([violin_voice], name='Violin Staff')
    # Viola
    viola_voice = abjad.Voice()
    viola_staff = abjad.Staff([viola_voice], name='Viola Staff')
    # Cello
    cello_voice = abjad.Voice()
    cello_staff = abjad.Staff([cello_voice], name='Cello Staff')
    # Everything else
    staff_group = abjad.StaffGroup([violin_staff, viola_staff, cello_staff])
    score = abjad.Score([staff_group])
    # Return the score
    return score


def add_rhythms(score, rhythm_maker, durations):
    selection = abjad.select(score).components(abjad.Voice)
    counts = list(rhythm_maker.talea.counts)
    for voice in selection:
        print(counts)
        rhythm_maker = abjad.new(rhythm_maker, talea__counts=counts)
        rhythm = rhythm_maker(durations)
        voice.extend(rhythm)
        counts = counts[1:] + [counts[0]]
    return score


def add_pitches(score):
    pitches = abjad.PitchSegment("g b d' f'")
    logical_ties = abjad.select(score).logical_ties(pitched=True)
    for i, logical_tie in enumerate(logical_ties):
        index = i % len(pitches)
        pitch = pitches[index]
        for note in logical_tie:
            note.written_pitch = pitch
    return score


def add_attachments(score):
    selection = abjad.select(score).components(abjad.Voice)
    for voice in selection:
        phrase_selection = abjad.select(voice).leaves().runs()
        for phrase in phrase_selection:
            if len(phrase) > 1:
                slur = abjad.Slur()
                abjad.attach(slur, phrase)
            accent = abjad.Articulation('accent')
            abjad.attach(accent, phrase[0])
    return score


def add_midi_instruments(score):
    violin_staff = score['Violin Staff']
    abjad.setting(violin_staff).midi_instrument = abjad.scheme.Scheme(
        'violin', force_quotes=True)
    viola_staff = score['Viola Staff']
    abjad.setting(viola_staff).midi_instrument = abjad.scheme.Scheme(
        'viola', force_quotes=True)
    cello_staff = score['Cello Staff']
    abjad.setting(cello_staff).midi_instrument = abjad.scheme.Scheme(
        'cello', force_quotes=True)
    abjad.attach(abjad.Clef('alto'), viola_staff[0][0])
    abjad.attach(abjad.Clef('bass'), cello_staff[0][0])
    abjad.attach(abjad.Clef('treble'), violin_staff[0][0])
    abjad.attach(abjad.instruments.Cello(), cello_staff[0][0])
    abjad.attach(abjad.instruments.Viola(), viola_staff[0][0])
    abjad.attach(abjad.instruments.Violin(), violin_staff[0][0])
    return score


def prettify_score(score):
    abjad.override(score).spacing_spanner.strict_grace_spacing = True
    abjad.override(score).spacing_spanner.strict_note_spacing = True
    abjad.override(score).spacing_spanner.uniform_stretching = True
    abjad.override(score).stem.length = 8.25
    abjad.override(score).text_script.outside_staff_padding = 1
    abjad.override(score).tuplet_bracket.bracket_visibility = True
    abjad.override(score).tuplet_bracket.minimum_length = 3
    abjad.override(score).tuplet_bracket.outside_staff_padding = 1.5
    abjad.override(score).tuplet_bracket.padding = 1.5
    abjad.override(score).tuplet_bracket.springs_and_rods = \
        abjad.scheme.Scheme('ly:spanner::set-spacing-rods', verbatim=True)
    abjad.override(score).tuplet_bracket.staff_padding = 2.25
    abjad.override(score).tuplet_number.text = \
        abjad.scheme.Scheme('tuplet-number::calc-fraction-text', verbatim=True)
    abjad.setting(score).proportional_notation_duration = \
        abjad.scheme.SchemeMoment((1, 24))
    abjad.setting(score).tuplet_full_length = True
    lilypond_file = abjad.lilypondfile.LilyPondFile.new(score)
    lilypond_file.layout_block.indent = abjad.lilypondfile.LilyPondDimension(20, 'mm')
    lilypond_file.layout_block.short_indent = abjad.lilypondfile.LilyPondDimension(15, 'mm')
    return lilypond_file
