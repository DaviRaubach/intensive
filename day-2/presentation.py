import abjad

def make_sketch_lilypond_file(component):
    abjad.override(component).bar_line.stencil = False
    abjad.override(component).bar_number.stencil = False
    abjad.override(component).beam.positions = abjad.SchemePair((4, 4))
    abjad.override(component).spacing_spanner.strict_grace_spacing = True
    abjad.override(component).spacing_spanner.strict_note_spacing = True
    abjad.override(component).spacing_spanner.uniform_stretching = True
    abjad.override(component).stem.length = 8.25
    abjad.override(component).text_script.outside_staff_padding = 1
    abjad.override(component).time_signature.stencil = False
    abjad.override(component).tuplet_bracket.bracket_visibility = True
    abjad.override(component).tuplet_bracket.minimum_length = 3
    abjad.override(component).tuplet_bracket.outside_staff_padding = 1.5
    abjad.override(component).tuplet_bracket.padding = 1.5
    abjad.override(component).tuplet_bracket.springs_and_rods = \
        abjad.Scheme('ly:spanner::set-spacing-rods', verbatim=True)
    abjad.override(component).tuplet_bracket.staff_padding = 2.25
    abjad.override(component).tuplet_number.text = \
        abjad.Scheme('tuplet-number::calc-fraction-text', verbatim=True)
    abjad.setting(component).proportional_notation_duration = \
        abjad.SchemeMoment((1, 24))
    abjad.setting(component).tuplet_full_length = True
    lilypond_file = abjad.LilyPondFile.new(component)
    lilypond_file.layout_block.indent = 0
    lilypond_file.paper_block.system_system_spacing = abjad.Scheme(
        "#'((basic-distance . 28)(minimum-distance . 1)(padding . 4)(stretchability . 1))",
        verbatim=True)    
    return lilypond_file

def make_sketch(selections, divisions): 
    # rhythmic creation
    voice = abjad.Voice()
    voice.append(selections)
    voice.remove_commands.append('Forbid_line_break_engraver')
    staff = abjad.Staff([voice], lilypond_type='RhythmicStaff')
    score = abjad.Score([staff])
    lilypond_file = make_sketch_lilypond_file(score)
    return lilypond_file

__all__ = [
    'make_sketch',
    'make_sketch_lilypond_file',
    ]