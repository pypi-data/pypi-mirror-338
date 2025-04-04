# -*- coding: utf-8 -*-
# Copyright (c) 2021-2024 Salvador E. Tropea
# Copyright (c) 2021-2024 Instituto Nacional de Tecnología Industrial
# License: AGPL-3.0
# Project: KiBot (formerly KiPlot)
# Description: Implements a field renamer
from .gs import GS
from .misc import W_EMPTYREN
from .macros import macros, document, filter_class  # noqa: F401
from .fil_base import FieldRename
from . import log

logger = log.get_logger()


@filter_class
class Field_Rename(BaseFilter):  # noqa: F821
    """ Field Renamer
        This filter implements a field renamer.
        The internal `_kicost_rename` filter emulates the KiCost behavior """
    def __init__(self):
        super().__init__()
        self._is_transform = True
        with document:
            self.rename = FieldRename
            """ [list(dict)=[]] Fields to rename """

    def config(self, parent):
        super().config(parent)
        self.rename = {f.field: f.name for f in self.rename}

    def filter(self, comp):
        """ Change the names of the specified fields """
        if not self.rename:
            logger.warning(W_EMPTYREN+'Nothing to rename in filter `{}`'.format(self.name))
            return
        for f in set(comp.get_field_names()).intersection(self.rename):
            new_name = self.rename[f]
            if GS.debug_level > 2:
                logger.debug('ref: {} field: {} -> {}'.format(comp.ref, f, new_name))
            comp.rename_field(f, new_name)
