# -*- coding: utf-8 -*-
import collections
import abjad
from trio_score.tools import ScoreTemplate


class SegmentMaker(object):

    def __init__(
        self,
        time_signatures=None,
        violin_pitches=None,
        violin_rhythm_maker=None,
        violin_seed=None,
        viola_pitches=None,
        viola_rhythm_maker=None,
        viola_seed=None,
        cello_pitches=None,
        cello_rhythm_maker=None,
        cello_seed=None,
        is_last_segment=False,
        ):
        time_signatures = [abjad.TimeSignature(_) for _ in time_signatures]
        assert len(time_signatures)
        self.time_signatures = time_signatures
        self.violin_pitches = violin_pitches
        self.violin_rhythm_maker = violin_rhythm_maker
        self.violin_seed = violin_seed
        self.viola_pitches = viola_pitches
        self.viola_rhythm_maker = viola_rhythm_maker
        self.viola_seed = viola_seed
        self.cello_pitches = cello_pitches
        self.cello_rhythm_maker = cello_rhythm_maker
        self.cello_seed = cello_seed
        self.score_template = ScoreTemplate()
        self.is_last_segment = bool(is_last_segment)

    def __call__(
        self,
        segment_metadata=None,
        previous_segment_metadata=None,
        ):
        score = self.score_template()
        violin_measures = self._make_measures(
            self.time_signatures,
            self.violin_rhythm_maker,
            self.violin_pitches,
            self.violin_seed,
            )
        score['Violin Voice'].extend(violin_measures)
        viola_measures = self._make_measures(
            self.time_signatures,
            self.viola_rhythm_maker,
            self.viola_pitches,
            self.viola_seed,
            )
        score['Viola Voice'].extend(viola_measures)
        cello_measures = self._make_measures(
            self.time_signatures,
            self.cello_rhythm_maker,
            self.cello_pitches,
            self.cello_seed,
            )
        score['Cello Voice'].extend(cello_measures)
        if self.is_last_segment:
            score.add_final_bar_line('|.', to_each_voice=True)
        else:
            score.add_final_bar_line('||', to_each_voice=True)
        self.score_template.attach(score)
        lilypond_file = abjad.LilyPondFile.new(
            score,
            includes=['../../stylesheets/stylesheet.ily'],
            )
        return lilypond_file, segment_metadata

    def _make_measures(self, time_signatures, rhythm_maker, pitches, seed):
        seed = seed or 0
        measures = abjad.Voice()
        for time_signature in time_signatures:
            multimeasure_rest = abjad.MultimeasureRest(1)
            multiplier = abjad.Multiplier(time_signature)
            abjad.attach(multiplier, multimeasure_rest)
            measures.append(abjad.Measure(time_signature, [multimeasure_rest]))
        if rhythm_maker is not None:
            # rotation not available anymore
            divisions = rhythm_maker(time_signatures)
            abjad.mutate(measures).replace_measure_contents(divisions)
        if pitches is not None:
            if not isinstance(pitches, collections.Iterable):
                pitches = [pitches]
            iterator = abjad.iterate(measures).logical_ties(pitched=True)
            iterator = enumerate(iterator, seed)
            for i, logical_tie in iterator:
                pitch = pitches[i % len(pitches)]
                for leaf in logical_tie:
                    leaf.written_pitch = pitch
        return measures
