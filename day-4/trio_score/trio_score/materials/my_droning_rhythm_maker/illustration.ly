\version "2.19.82"
\language "english"

\include "default.ily"
\include "rhythm-maker-docs.ily"

\header {
    tagline = ##f
}

\layout {}

\paper {}

\score {
    \new Score
    <<
        \new GlobalContext
        {
            {   % measure
                \time 3/8
                s1 * 3/8
            }   % measure
            {   % measure
                \time 4/8
                s1 * 1/2
            }   % measure
            {   % measure
                \time 3/16
                s1 * 3/16
            }   % measure
            {   % measure
                \time 4/16
                s1 * 1/4
            }   % measure
        }
        \new RhythmicStaff
        {
            {   % measure
                \time 3/8
                c'4.
                ~
            }   % measure
            {   % measure
                \time 4/8
                c'2
            }   % measure
            {   % measure
                \time 3/16
                c'8.
                ~
            }   % measure
            {   % measure
                \time 4/16
                c'4
            }   % measure
        }
    >>
}