# -*- coding: utf-8 -*-
# Copyright (c) 2021-2024 Salvador E. Tropea
# Copyright (c) 2021-2024 Instituto Nacional de Tecnología Industrial
# License: AGPL-3.0
# Project: KiBot (formerly KiPlot)
"""
Dependencies:
  - from: Git
    role: Find commit hash and/or date
  - from: Bash
    role: Run external commands to create replacement text
"""
import os
from .gs import GS
from .kiplot import load_sch
from .pre_any_replace import TagReplaceBase, Base_ReplaceOptions, Base_Replace
from .macros import macros, document, pre_class  # noqa: F401
from . import log

logger = log.get_logger()


class TagReplaceSCH(TagReplaceBase):
    """ Tags to be replaced for an SCH """
    def __init__(self):
        super().__init__()
        self._help_command += (".\nKIBOT_SCH_NAME variable is the name of the current sheet."
                               "\nKIBOT_TOP_SCH_NAME variable is the name of the top sheet")


class SCH_ReplaceOptions(Base_ReplaceOptions):
    """ SCH replacement options """
    def __init__(self):
        super().__init__()
        self._help_date_command = self._help_date_command.replace('PCB', 'SCH')
        self.replace_tags = TagReplaceSCH


@pre_class
class SCH_Replace(Base_Replace):  # noqa: F821
    """ SCH Replace (**Deprecated**)
        Replaces tags in the schematic. I.e. to insert the git hash or last revision date.
        This is useful for KiCad 5, use `set_text_variables` when using KiCad 6.
        This preflight modifies the schematics. Even when a back-up is done use it carefully """
    _context = 'SCH'

    def __init__(self):
        super().__init__()
        with document:
            self.sch_replace = SCH_ReplaceOptions
            """ [dict={}] Options for the `sch_replace` preflight """

    def apply(self):
        o = self.sch_replace
        if o.date_command:
            # Convert it into another replacement
            t = TagReplaceSCH()
            if GS.ki5:
                t.tag = r'^Date ("(?:[^"]|\\")*")$'
                t.before = 'Date "'
                t.after = '"'
            else:
                t.tag = r'\(date ("(?:[^"]|\\")*")\)'
                t.before = '(date "'
                t.after = '")'
            t.command = o.date_command
            t._relax_check = True
            o.replace_tags.append(t)
        load_sch()
        os.environ['KIBOT_TOP_SCH_NAME'] = GS.sch_file
        for file in GS.sch.get_files():
            self.replace(file, o)
        # Force the schematic reload
        GS.sch = None
