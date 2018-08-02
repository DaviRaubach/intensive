# -*- coding: utf-8 -*-
import abjad.system

abjad.system.ImportManager.import_material_packages(
    __path__[0],
    globals(),
    )
