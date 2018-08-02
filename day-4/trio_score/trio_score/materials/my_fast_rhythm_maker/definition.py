# -*- encoding: utf-8 -*-
import os
import abjad
import abjadext.rmakers


my_fast_rhythm_maker = abjadext.rmakers.TaleaRhythmMaker(
    extra_counts_per_division=[0, 0, 1, 0, 1, 2],
    talea=abjadext.rmakers.Talea(
        counts=[1, 1, 2, 3, -1, 4, 1, 1, 2],
        denominator=16,
        ),
    tie_specifier=abjadext.rmakers.TieSpecifier(
        tie_across_divisions=[True, False],
        ),
    )


if __name__ == '__main__':
    illustration_path = os.path.join(
        os.path.dirname(__file__),
        'illustration.pdf',
        )
    abjad.persist(my_fast_rhythm_maker).as_pdf(illustration_path)
    abjad.system.IOManager.open_file(illustration_path)
