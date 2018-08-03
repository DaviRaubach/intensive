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
                        \time 4/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 1/1 {
                            \clef "treble"
                            c'16
                            [
                            d'16
                            c'8
                            d'8.
                            ]
                            r16
                            c'4
                            d'16
                            [
                            c'16
                            d'8
                            ~
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 3/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 1/1 {
                            d'16
                            [
                            c'16
                            d'8
                            c'8.
                            ]
                            r16
                            d'4
                        }
                    }   % measure
                    {   % measure
                        \time 5/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 20/21 {
                            c'16
                            [
                            d'16
                            c'8
                            d'16
                            c'16
                            d'8
                            c'8.
                            ]
                            r16
                            d'4
                            c'16
                            [
                            d'16
                            c'8
                            d'16
                            ~
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 4/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 1/1 {
                            d'16
                            [
                            c'8
                            d'8.
                            ]
                            r16
                            c'4
                            d'16
                            [
                            c'16
                            d'8
                            c'16
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 3/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 12/13 {
                            d'16
                            [
                            c'8
                            d'8.
                            ]
                            r16
                            c'4
                            d'16
                            [
                            c'16
                            ~
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 5/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/11 {
                            c'8
                            [
                            d'16
                            c'16
                            d'8
                            c'8.
                            ]
                            r16
                            d'4
                            c'16
                            [
                            d'16
                            c'8
                            d'16
                            c'16
                            d'8
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
                        \time 4/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 4/4 {
                            \clef "alto"
                            c'4
                            d'4
                            c'4
                            d'4
                            ~
                        }
                    }   % measure
                    {   % measure
                        \time 3/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 6/7 {
                            d'8
                            [
                            c'8
                            d'8
                            c'8
                            d'8
                            c'8
                            d'8
                            ~
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 5/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 5/4 {
                            d'2
                            c'2
                            ~
                        }
                    }   % measure
                    {   % measure
                        \time 4/4
                        \times 4/5 {
                            c'4
                            d'4
                            c'4
                            d'4
                            c'4
                            ~
                        }
                    }   % measure
                    {   % measure
                        \time 3/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 6/6 {
                            c'8
                            [
                            d'8
                            c'8
                            d'8
                            c'8
                            d'8
                            ~
                            ]
                        }
                    }   % measure
                    {   % measure
                        \time 5/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 5/6 {
                            d'2
                            c'2
                            d'2
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
                        \time 4/4
                        \clef "bass"
                        c'1
                        ~
                    }   % measure
                    {   % measure
                        \time 3/4
                        c'2.
                    }   % measure
                    {   % measure
                        \time 5/4
                        d'1
                        ~
                        d'4
                        ~
                    }   % measure
                    {   % measure
                        \time 4/4
                        d'1
                    }   % measure
                    {   % measure
                        \time 3/4
                        ef'2.
                        ~
                    }   % measure
                    {   % measure
                        \time 5/4
                        ef'1
                        ~
                        ef'4
                        \bar "||" %! SCORE1
                    }   % measure
                }
            }
        >>
    >>
