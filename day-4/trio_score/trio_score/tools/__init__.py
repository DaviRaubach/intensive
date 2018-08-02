# -*- coding: utf-8 -*-
import abjad.system


abjad.system.ImportManager.import_structured_package(
    __path__[0],
    globals(),
    )
