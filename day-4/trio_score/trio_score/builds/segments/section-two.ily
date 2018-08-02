    \context Score = "Trio Score"
    <<
        \context StaffGroup = "Trio Staff Group"
        <<
            \tag #'violin
            \context ViolinStaff = "Violin Staff"
            \with
            {
                midiInstrument = #"violin"
            }
            {
                \context Voice = "Violin Voice"
                {
                    {   % measure
                        \time 3/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 12/12 {
                            \clef "treble"
                            ef''16
                            [
                            c''16
                            ef''16
                            c''16
                            ef''16
                            d''16
                            af'16
                            g'16
                            e''16
                            cs''16
                            c''16
                            g'16
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 4/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 16/16 {
                            ef''16
                            [
                            c''16
                            ef''16
                            c''16
                            ef''16
                            d''16
                            af'16
                            g'16
                            e''16
                            cs''16
                            c''16
                            g'16
                            ef''16
                            c''16
                            ef''16
                            c''16
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 7/8
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 14/14 {
                            ef''16
                            [
                            d''16
                            af'16
                            g'16
                            e''16
                            cs''16
                            c''16
                            g'16
                            ef''16
                            c''16
                            ef''16
                            c''16
                            ef''16
                            d''16
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 4/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 16/16 {
                            af'16
                            [
                            g'16
                            e''16
                            cs''16
                            c''16
                            g'16
                            ef''16
                            c''16
                            ef''16
                            c''16
                            ef''16
                            d''16
                            af'16
                            g'16
                            e''16
                            cs''16
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 3/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 12/12 {
                            c''16
                            [
                            g'16
                            ef''16
                            c''16
                            ef''16
                            c''16
                            ef''16
                            d''16
                            af'16
                            g'16
                            e''16
                            cs''16
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 4/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 16/16 {
                            c''16
                            [
                            g'16
                            ef''16
                            c''16
                            ef''16
                            c''16
                            ef''16
                            d''16
                            af'16
                            g'16
                            e''16
                            cs''16
                            c''16
                            g'16
                            ef''16
                            c''16
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 7/8
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 14/14 {
                            ef''16
                            [
                            c''16
                            ef''16
                            d''16
                            af'16
                            g'16
                            e''16
                            cs''16
                            c''16
                            g'16
                            ef''16
                            c''16
                            ef''16
                            c''16
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 4/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 16/16 {
                            ef''16
                            [
                            d''16
                            af'16
                            g'16
                            e''16
                            cs''16
                            c''16
                            g'16
                            ef''16
                            c''16
                            ef''16
                            c''16
                            ef''16
                            d''16
                            af'16
                            g'16
                            ]
                            \bar "||" %! SCORE1
                        }
                    }   % measure
                }
            }
            \tag #'viola
            \context ViolaStaff = "Viola Staff"
            \with
            {
                midiInstrument = #"viola"
            }
            {
                \context Voice = "Viola Voice"
                {
                    {   % measure
                        \time 3/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 3/3 {
                            \clef "alto"
                            bf4
                            d4
                            g4
                            ~
                        }
                    }   % measure
                    {   % measure
                        \time 4/4
                        \times 8/9 {
                            g8
                            [
                            af8
                            b8
                            d8
                            ef8
                            a8
                            bf8
                            g8
                            bf8
                            ~
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 7/8
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 1/1 {
                            bf2..
                            ~
                        }
                    }   % measure
                    {   % measure
                        \time 4/4
                        \times 4/5 {
                            bf4
                            g4
                            bf4
                            d4
                            g4
                            ~
                        }
                    }   % measure
                    {   % measure
                        \time 3/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 6/6 {
                            g8
                            [
                            af8
                            b8
                            d8
                            ef8
                            a8
                            ~
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 4/4
                        \times 2/3 {
                            a2
                            bf2
                            g2
                            ~
                        }
                    }   % measure
                    {   % measure
                        \time 7/8
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 7/6 {
                            g4
                            bf4
                            g4
                            ~
                        }
                    }   % measure
                    {   % measure
                        \time 4/4
                        \times 8/9 {
                            g8
                            [
                            bf8
                            d8
                            g8
                            af8
                            b8
                            d8
                            ef8
                            a8
                            ]
                            \bar "||" %! SCORE1
                        }
                    }   % measure
                }
            }
            \tag #'cello
            \context CelloStaff = "Cello Staff"
            \with
            {
                midiInstrument = #"cello"
            }
            {
                \context Voice = "Cello Voice"
                {
                    {   % measure
                        \time 3/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 1/1 {
                            \clef "bass"
                            c'16
                            [
                            cs'16
                            e'8
                            g8.
                            ]
                            r16
                            af4
                            ~
                        }
                    }   % measure
                    {   % measure
                        \time 4/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 1/1 {
                            af16
                            [
                            d'16
                            ef'8
                            c'16
                            ef'16
                            c'8
                            ef'8.
                            ]
                            r16
                            g4
                        }
                    }   % measure
                    {   % measure
                        \time 7/8
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 14/15 {
                            c'16
                            [
                            cs'16
                            e'8
                            g16
                            af16
                            d'8
                            ef'8.
                            ]
                            r16
                            c'8.
                            ~
                        }
                    }   % measure
                    {   % measure
                        \time 4/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 1/1 {
                            c'16
                            [
                            ef'16
                            c'16
                            ef'8
                            g16
                            c'16
                            cs'8
                            e'8.
                            ]
                            r16
                            g8.
                            ~
                        }
                    }   % measure
                    {   % measure
                        \time 3/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 12/13 {
                            g16
                            [
                            af16
                            d'16
                            ef'8
                            c'16
                            ef'16
                            c'8
                            ef'8.
                            ]
                            r16
                        }
                    }   % measure
                    {   % measure
                        \time 4/4
                        \times 8/9 {
                            g4
                            c'16
                            [
                            cs'16
                            e'8
                            g16
                            af16
                            d'8
                            ef'8.
                            ]
                            r16
                            c'8
                            ~
                        }
                    }   % measure
                    {   % measure
                        \time 7/8
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 1/1 {
                            c'8
                            [
                            ef'16
                            c'16
                            ef'8
                            g16
                            c'16
                            cs'8
                            e'8.
                            ]
                            r16
                        }
                    }   % measure
                    {   % measure
                        \time 4/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 1/1 {
                            g4
                            af16
                            [
                            d'16
                            ef'8
                            c'16
                            ef'16
                            c'8
                            ef'8.
                            ]
                            r16
                            \bar "||" %! SCORE1
                        }
                    }   % measure
                }
            }
        >>
    >>