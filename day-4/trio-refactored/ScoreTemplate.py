import abjad


class ScoreTemplate(object):

    def __call__(self):
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
