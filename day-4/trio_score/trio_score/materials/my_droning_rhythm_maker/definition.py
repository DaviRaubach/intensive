# -*- encoding: utf-8 -*-
import os
import abjad
import abjadext.rmakers


my_droning_rhythm_maker = abjadext.rmakers.NoteRhythmMaker(
    tie_specifier=abjadext.rmakers.TieSpecifier(
        tie_across_divisions=[True, False],
        ),
    )


if __name__ == '__main__':
    illustration_path = os.path.join(
        os.path.dirname(__file__),
        'illustration.pdf',
        )
    abjad.persist(my_droning_rhythm_maker).as_pdf(illustration_path)
    abjad.system.IOManager.open_file(illustration_path)
