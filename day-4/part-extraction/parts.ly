\version "2.19.82"
\language "english"


\book {
    \bookOutputSuffix "violin"
    \score {
        \keepWithTag #'(violin)
        \include "music.ily"
    }
}

\book {
    \bookOutputSuffix "viola"
    \score {
        \keepWithTag #'(viola)
        \include "music.ily"
    }
}

\book {
    \bookOutputSuffix "cello"
    \score {
        \keepWithTag #'(cello)
        \include "music.ily"
    }
}
