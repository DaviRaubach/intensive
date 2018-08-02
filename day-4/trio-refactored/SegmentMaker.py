# -*- encoding: utf-8 -*-
import abjad
import abjadext.rmakers


class SegmentMaker(object):

    def __init__(self, durations):
        self.durations = durations
        self.rhythm_maker = abjadext.rmakers.TaleaRhythmMaker(
            talea=abjadext.rmakers.Talea([1, 2, 3, -1], 8),
            )

    def __call__(self):
        from ScoreTemplate import ScoreTemplate
        score_template = ScoreTemplate()
        score = score_template()
        score = self.add_rhythms(score, self.rhythm_maker, self.durations)
        score = self.add_pitches(score)
        score = self.add_attachments(score)
        score = self.add_midi_instruments(score)
        lilypond_file = self.prettify_score(score)
        return lilypond_file

    def __illustrate__(self):
        return self()

    def add_rhythms(self, score, rhythm_maker, durations):
        selection = abjad.select(score).components(abjad.Voice)
        counts = list(rhythm_maker.talea.counts)
        for voice in selection:
            print(counts)
            rhythm_maker = abjad.new(rhythm_maker, talea__counts=counts)
            rhythm = rhythm_maker(durations)
            voice.extend(rhythm)
            counts = counts[1:] + [counts[0]]
        return score

    def add_pitches(self, score):
        pitches = abjad.PitchSegment("g b d' f'")
        logical_ties = abjad.select(score).logical_ties(pitched=True)
        for i, logical_tie in enumerate(logical_ties):
            index = i % len(pitches)
            pitch = pitches[index]
            for note in logical_tie:
                note.written_pitch = pitch
        return score

    def add_attachments(self, score):
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

    def add_midi_instruments(self, score):
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

    def prettify_score(self, score):
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
