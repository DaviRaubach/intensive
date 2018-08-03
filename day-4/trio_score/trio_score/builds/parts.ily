\book {
    \bookOutputSuffix "violin"
    \header {
        subtitle = "Violin Part"
    }
    \score {
        \keepWithTag #'(violin)
        \include "../segments.ily"
    }
}

\book {
    \bookOutputSuffix "viola"
    \header {
        subtitle = "Viola Part"
    }
    \score {
        \keepWithTag #'(viola)
        \include "../segments.ily"
    }
}

\book {
    \bookOutputSuffix "cello"
    \header {
        subtitle = "Cello Part"
    }
    \score {
        \keepWithTag #'(cello)
        \include "../segments.ily"
    }
}
