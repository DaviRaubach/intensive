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
                        \time 2/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 4/4 {
                            \clef "treble"
                            c'8
                            [
                            g8
                            ef'8
                            c'8
                            ]
                        }
                    }   % measure
                    {   % measure
                        \times 4/5 {
                            ef'8
                            [
                            c'8
                            ef'8
                            d'8
                            af8
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 5/8
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 5/7 {
                            g8
                            [
                            e'8
                            cs'8
                            c'8
                            g8
                            ef'8
                            c'8
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 6/8
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 6/6 {
                            ef'8
                            [
                            c'8
                            ef'8
                            d'8
                            af8
                            g8
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 5/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/11 {
                            e'8
                            [
                            cs'8
                            c'8
                            g8
                            ef'8
                            c'8
                            ef'8
                            c'8
                            ef'8
                            d'8
                            af8
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 2/4
                        \times 4/6 {
                            g8
                            [
                            e'8
                            cs'8
                            c'8
                            g8
                            ef'8
                            ]
                        }
                    }   % measure
                    {   % measure
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 4/4 {
                            c'8
                            [
                            ef'8
                            c'8
                            ef'8
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 5/8
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 5/6 {
                            d'8
                            [
                            af8
                            g8
                            e'8
                            cs'8
                            c'8
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 6/8
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 6/8 {
                            g8
                            [
                            ef'8
                            c'8
                            ef'8
                            c'8
                            ef'8
                            d'8
                            af8
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 5/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/10 {
                            g8
                            [
                            e'8
                            cs'8
                            c'8
                            g8
                            ef'8
                            c'8
                            ef'8
                            c'8
                            ef'8
                            ]
                            \bar "|." %! SCORE1
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
                        \time 2/4
                        \clef "alto"
                        c2
                    }   % measure
                    {   % measure
                        ef2
                    }   % measure
                    {   % measure
                        \time 5/8
                        c2
                        ~
                        c8
                    }   % measure
                    {   % measure
                        \time 6/8
                        ef2.
                    }   % measure
                    {   % measure
                        \time 5/4
                        c1
                        ~
                        c4
                    }   % measure
                    {   % measure
                        \time 2/4
                        ef2
                    }   % measure
                    {   % measure
                        c2
                    }   % measure
                    {   % measure
                        \time 5/8
                        ef2
                        ~
                        ef8
                    }   % measure
                    {   % measure
                        \time 6/8
                        c2.
                    }   % measure
                    {   % measure
                        \time 5/4
                        ef1
                        ~
                        ef4
                        \bar "|." %! SCORE1
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
                        \time 2/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 1/1 {
                            \clef "bass"
                            b,16
                            [
                            af,16
                            f8
                            e8.
                            ]
                            r16
                        }
                    }   % measure
                    {   % measure
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 1/1 {
                            bf,4
                            a,16
                            [
                            c16
                            a,8
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 5/8
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/11 {
                            c16
                            [
                            a,16
                            f8
                            c8.
                            ]
                            r16
                            b,8.
                            ~
                        }
                    }   % measure
                    {   % measure
                        \time 6/8
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 1/1 {
                            b,16
                            [
                            af,16
                            f16
                            e8
                            bf,16
                            a,16
                            c8
                            a,8.
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 5/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 20/21 {
                            r16
                            c4
                            a,16
                            [
                            f16
                            c8
                            b,16
                            af,16
                            f8
                            e8.
                            ]
                            r16
                            bf,4
                            ~
                        }
                    }   % measure
                    {   % measure
                        \time 2/4
                        \times 4/5 {
                            bf,16
                            [
                            a,16
                            c8
                            a,16
                            c16
                            a,8
                            f8
                            ~
                            ]
                        }
                    }   % measure
                    {   % measure
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 1/1 {
                            f16
                            r16
                            c4
                            b,16
                            [
                            af,16
                            ~
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 5/8
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 1/1 {
                            af,8
                            [
                            f16
                            e16
                            bf,8
                            a,8.
                            ]
                            r16
                        }
                    }   % measure
                    {   % measure
                        \time 6/8
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 12/13 {
                            c4
                            a,16
                            [
                            c16
                            a,8
                            f16
                            c16
                            b,8
                            af,16
                            ~
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 5/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 1/1 {
                            af,8
                            r16
                            f4
                            e16
                            [
                            bf,16
                            a,8
                            c16
                            a,16
                            c8
                            a,8.
                            ]
                            r16
                            f16
                            \bar "|." %! SCORE1
                        }
                    }   % measure
                }
            }
        >>
    >>
