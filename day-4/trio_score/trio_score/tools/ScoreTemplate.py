# -*- coding: utf-8 -*-
import abjad


class ScoreTemplate(object):

    def __call__(self):

        # Violin
        violin_staff = abjad.Staff(
            [abjad.Voice(name='Violin Voice')],
            name='Violin Staff',
            lilypond_type='ViolinStaff',
            )
        violin_tag = abjad.LilyPondLiteral(r"\tag #'violin", format_slot='before')
        abjad.attach(violin_tag, violin_staff)
        abjad.setting(violin_staff).midi_instrument = abjad.scheme.Scheme(
            'violin', force_quotes=True)

        # Viola
        viola_staff = abjad.Staff(
            [abjad.Voice(name='Viola Voice')],
            name='Viola Staff',
            lilypond_type='ViolaStaff',
            )
        viola_tag = abjad.LilyPondLiteral(r"\tag #'viola", format_slot='before')
        abjad.attach(viola_tag, viola_staff)
        abjad.setting(viola_staff).midi_instrument = abjad.scheme.Scheme(
            'viola', force_quotes=True)

        # Cello
        cello_staff = abjad.Staff(
            [abjad.Voice(name='Cello Voice')],
            name='Cello Staff',
            lilypond_type='CelloStaff',
            )
        cello_tag = abjad.LilyPondLiteral(r"\tag #'cello", format_slot='before')
        abjad.attach(cello_tag, cello_staff)
        abjad.setting(cello_staff).midi_instrument = abjad.scheme.Scheme(
            'cello', force_quotes=True)

        # Everything else
        staff_group = abjad.StaffGroup(
            [violin_staff, viola_staff, cello_staff],
            name='Trio Staff Group',
            )
        score = abjad.Score(
            [staff_group],
            name='Trio Score',
            )

        return score

    def attach(self, score):
        violin_staff = score['Violin Staff']
        viola_staff = score['Viola Staff']
        cello_staff = score['Cello Staff']
        abjad.attach(abjad.Clef('bass'), abjad.select(cello_staff).leaves()[0])
        abjad.attach(abjad.instruments.Cello(), abjad.select(cello_staff).leaves()[0])
        abjad.attach(abjad.Clef('alto'), abjad.select(viola_staff).leaves()[0])
        abjad.attach(abjad.instruments.Viola(), abjad.select(viola_staff).leaves()[0])
        abjad.attach(abjad.Clef('treble'), abjad.select(violin_staff).leaves()[0])
        abjad.attach(abjad.instruments.Violin(), abjad.select(violin_staff).leaves()[0])
