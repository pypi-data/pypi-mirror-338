# -*- coding: utf-8 -*-
# Copyright (c) 2020-2024 Salvador E. Tropea
# Copyright (c) 2020-2024 Instituto Nacional de Tecnología Industrial
# License: AGPL-3.0
# Project: KiBot (formerly KiPlot)
import json
import os
from . import __version__
from .bom.kibot_logo import KIBOT_LOGO, KIBOT_LOGO_W, KIBOT_LOGO_H
from .error import KiPlotConfigurationError
from .gs import GS
from .kicad.config import KiConf
from .kiplot import load_board, load_sch, run_command
from .misc import (ERC_ERROR, DRC_ERROR, W_ERCJSON, W_DRCJSON, STYLE_COMMON, TABLE_MODERN, HEAD_COLOR_B, HEAD_COLOR_B_L,
                   TD_ERC_CLASSES, GENERATOR_CSS)
from .optionable import Optionable
from .pre_base import BasePreFlight
from .pre_filters import FilterOptions, FiltersOptions
from .macros import macros, document  # noqa: F401
from . import log
logger = log.get_logger(__name__)


class FilterOptionsXRC(FilterOptions):
    def __init__(self):
        super().__init__()
        with document:
            self.change_to = 'ignore'
            """ [error,warning,ignore] The action of the filter.
                Changing to *ignore* is the default and is used to suppress a violation, but you can also change
                it to be an *error* or a *warning*. Note that violations excluded by KiCad are also analyzed,
                so you can revert a GUI exclusion """
        # number is for KiCad 5, remove it
        del self.number
        del self.error_number
        # Avoid mentioning KiCad 5/6 in the "error" help
        self.set_doc('error', " [string=''] Error id we want to exclude")


class ERCOptions(FiltersOptions):
    """ ERC options """
    def __init__(self):
        with document:
            self.enabled = True
            """ Enable the check. This is the replacement for the boolean value """
            self.dir = ''
            """ Sub-directory for the report """
            self.output = GS.def_global_output
            """ *Name for the generated archive (%i=erc %x=according to format) """
            self.format = Optionable
            """ [string|list(string)='HTML'] [RPT,HTML,CSV,JSON] {comma_sep} Format/s used for the report.
                You can specify multiple formats """
            self.warnings_as_errors = False
            """ Warnings are considered errors, they still reported as warnings """
            self.dont_stop = False
            """ Continue even if we detect errors """
            self.units = 'millimeters'
            """ [millimeters,inches,mils] Units used for the positions. Affected by global options """
            self.force_english = True
            """ Force english messages. KiCad 8.0.4 introduced translation, breaking filters for previous versions.
                Disable it if you prefer using the system wide language """
            self.category = Optionable
            """ [string|list(string)=''] {comma_sep} The category for this preflight. If not specified an internally defined
                category is used.
                Categories looks like file system paths, i.e. **PCB/fabrication/gerber**.
                The categories are currently used for `navigate_results` """
        super().__init__()
        self.filters = FilterOptionsXRC
        self.set_doc('filters', " [list(dict)=[]] Used to manipulate the violations. Avoid using the *filters* preflight")
        self._unknown_is_error = True
        self._format_example = 'HTML,RPT'

    def config(self, parent):
        super().config(parent)
        if not self.format:
            self.format = ['HTML']
        if not self.category:
            self.category = self.force_list(parent._category)


class DRCOptions(ERCOptions):
    """ DRC options """
    def __init__(self):
        with document:
            self.schematic_parity = True
            """ Check if the PCB and the schematic are coincident """
            self.all_track_errors = False
            """ Report all the errors for all the tracks, not just the first """
            self.ignore_unconnected = False
            """ Ignores the unconnected nets. Useful if you didn't finish the routing """
        super().__init__()
        self.set_doc('output', self.get_doc('output')[0].replace('erc', 'drc'))


class XRC(BasePreFlight):
    def __init__(self, cls):
        super().__init__()
        self._opts_cls = cls
        self._files_to_remove = []

    def __str__(self):
        return f'{self.type}: {self._enabled} ({self._format})'

    def config(self, parent):
        super().config(parent)
        ops = self.erc if self._sch_related else self.drc
        if isinstance(ops, bool):
            new_ops = self._opts_cls()
            new_ops.config(self)  # Get the defaults
            new_ops.enabled = ops
            ops = new_ops
        # Transfer the options to this class
        for k, v in dict(ops.get_attrs_gen()).items():
            setattr(self, '_'+k, v)
        self._format = ops.format
        self._filters = ops.filters
        self._expand_ext = self._format[0].lower()
        self.dir = self._dir

    def get_targets(self):
        """ Returns a list of targets generated by this preflight """
        if self._sch_related:
            load_sch()
        else:
            load_board()
        out_dir = self.expand_dirname(GS.out_dir)
        if GS.global_dir and GS.global_use_dir_for_preflights:
            out_dir = os.path.join(out_dir, self.expand_dirname(GS.global_dir))
        names = []
        for f in self._format:
            self._expand_ext = f.lower()
            name = Optionable.expand_filename_both(self, self._output, is_sch=self._sch_related)
            names.append(os.path.abspath(os.path.join(out_dir, self._dir, name)))
        return names

    def get_navigate_targets(self, _):
        kind = 'erc' if self._sch_related else 'drc'
        icons = [os.path.join(GS.get_resource_path('images'), kind+'.svg')
                 if f in {'HTML', 'RPT'} else None for f in self._format]
        return self.get_targets(), icons

    @staticmethod
    def get_conf_examples(name):
        if not GS.ki8:
            return None
        return {name: {'dont_stop': True, 'format': 'HTML,RPT,JSON,CSV'}}

    def get_item_txt(self, item, indent=4, sep='\n'):
        desc = item.get('description', '')
        pos = item.get('pos', None)
        if pos:
            x = pos.get('x', 0)
            y = pos.get('y', 0)
            pos_txt = f'@({x} {self.units}, {y} {self.units}): '
        else:
            pos_txt = ''
        return (' '*indent)+f'{pos_txt}{desc}'+sep

    def add_html_violation(self, violation):
        severity = violation.get('severity', 'error')
        excluded = violation.get('excluded', False)
        type = violation.get('type', '')
        description = violation.get('description', '')
        details = ''
        for item in violation.get('items', []):
            details += self.get_item_txt(item, indent=0, sep='<br>')
        html = f'  <tr id="{self.html_id}">\n'
        cl = 'td-excluded' if excluded else ('td-error' if severity == 'error' else 'td-warning')
        html += f'   <td class="{cl}">{type}</td>\n'
        html += f'   <td>{description}</td>\n'
        html += f'   <td>{details}</td>\n'
        html += '  </tr>\n'
        self.html_id += 1
        return html

    def create_json(self, data):
        return json.dumps(data, indent=4)

    def create_html_top(self, data):
        # HTML Head
        html = '<html>\n'
        html += '<head>\n'
        html += ' <meta charset="UTF-8">\n'  # UTF-8 encoding for unicode support
        if self._sch_related:
            title = 'ERC report for '+(GS.pro_basename or GS.sch_basename or '')
        else:
            title = 'DRC report for '+(GS.pro_basename or GS.pcb_basename or '')
        html += f' <title>{title}</title>\n'
        # CSS
        html += '<style>\n'
        style = STYLE_COMMON
        style += TABLE_MODERN.replace('@bg@', HEAD_COLOR_B)
        style += TABLE_MODERN.replace('@bgl@', HEAD_COLOR_B_L)
        style += TD_ERC_CLASSES
        style += GENERATOR_CSS
        style += ' .head-table { margin-left: auto; margin-right: auto; }\n'
        style += ' .content-table { margin-left: auto; margin-right: auto }\n'
        html += style
        html += '</style>\n'
        html += '</head>\n'
        html += '<body>\n'

        img = 'data:image/png;base64,'+KIBOT_LOGO
        img_w = KIBOT_LOGO_W
        img_h = KIBOT_LOGO_H
        html += '<table class="head-table">\n'
        html += '<tr>\n'
        html += ' <td rowspan="3">\n'
        html += f'  <img src="{img}" alt="Logo" width="{img_w}" height="{img_h}">\n'
        html += ' </td>\n'
        html += ' <td colspan="2" class="cell-title">\n'
        html += f'  <div class="title">{title}</div>\n'
        html += ' </td>\n'
        html += '</tr>\n'
        html += '<tr>\n'
        html += ' <td class="cell-info">\n'
        if self._sch_related:
            html += f'   <b>Schematic</b>: {GS.sch_basename}<br>\n'
            html += f'   <b>Revision</b>: {GS.sch.revision}<br>\n'
        else:
            html += f'   <b>PCB</b>: {GS.pcb_basename}<br>\n'
            html += f'   <b>Revision</b>: {GS.pcb_rev}<br>\n'
        dt = data.get('date', '??')
        html += f'   <b>Date</b>: {dt}<br>\n'
        kv = data.get('kicad_version', GS.kicad_version)
        html += f'   <b>KiCad Version</b>: {kv}<br>\n'
        html += ' </td>\n'
        html += ' <td class="cell-stats">\n'
        txt_error = f'<b>Errors</b>: {self.c_err}'+(f' (+{self.c_err_excl} excluded)' if self.c_err_excl else '')
        txt_warn = f'<b>Warnings</b>: {self.c_warn}'+(f' (+{self.c_warn_excl} excluded)' if self.c_warn_excl else '')
        txt_total = f'<b>Total</b>: {self.c_tot}'+(f' (+{self.c_tot_excl} excluded)' if self.c_tot_excl else '')
        html += f'   {txt_error}<br>\n'
        html += f'   {txt_warn}<br>\n'
        html += f'   {txt_total}<br>\n'
        html += ' </td>\n'
        html += '</tr>\n'
        html += '</table>\n'
        self.html_id = 0
        return html

    def create_html_bottom(self):
        html = ('<p class="generator">Generated by <a href="https://github.com/INTI-CMNB/KiBot/">KiBot</a> v{}</p>\n'.
                format(__version__))
        html += '</body>\n'
        html += '</html>\n'
        return html

    def create_html_violations(self, violations):
        html = '<table class="content-table">\n'
        html += ' <thead>\n'
        html += '  <tr>\n'
        for h in ['Type', 'Description', 'Details']:
            html += f'   <th>{h}</th>\n'
        html += '  </tr>\n'
        html += ' </thead>\n'
        html += ' <tbody>\n'
        # Errors
        for violation in violations:
            if violation.get('severity', 'error') == 'error' and not violation.get('excluded', False):
                html += self.add_html_violation(violation)
        # Warnings
        for violation in violations:
            if violation.get('severity', 'error') == 'warning' and not violation.get('excluded', False):
                html += self.add_html_violation(violation)
        # Excluded
        for violation in violations:
            if violation.get('excluded', False):
                html += self.add_html_violation(violation)
        html += ' </tbody>\n'
        html += '</table>\n'
        return html

    def create_html_ok(self):
        """ Put a big checkmark to indicate all went ok """
        return '<div class="centered-checkmark">&#x2714;</div>\n'

    def run(self):
        # Differences between ERC and DRC
        if GS.sch_file:
            # May be needed by DRC when checking parity?
            KiConf.check_sym_lib_table()
        if GS.pcb_file:
            KiConf.check_fp_lib_table()
        if self._sch_related:
            nm = 'ERC'
            err = ERC_ERROR
            erc_warnings = BasePreFlight.get_option('erc_warnings')
            wjson = W_ERCJSON
        else:
            nm = 'DRC'
            err = DRC_ERROR
            erc_warnings = False
            wjson = W_DRCJSON
        nml = nm.lower()
        # Now do the run
        if not GS.ki8:
            raise KiPlotConfigurationError(f'The `{nml}` preflight needs KiCad 8 or newer, use `run_{nml}` instead')
        # Compute the output name and make sure the path exists
        outputs = self.get_targets()
        output = outputs[0]
        os.makedirs(os.path.dirname(output), exist_ok=True)
        # Run the xRC from the CLI
        cmd = self.get_command(output)
        logger.info(f'- Running the {nm}')
        # Introduced in 8.0.4: translated messages
        if self._force_english:
            old_lang = os.environ.get('LANG')
            if old_lang:
                os.environ['LANG'] = 'en'
        run_command(cmd)
        if self._force_english and old_lang:
            os.environ['LANG'] = old_lang
        # Remove temporals
        logger.debug('Removing temporal files')
        for f in self._files_to_remove:
            if os.path.isfile(f):
                logger.debug('- File `{}`'.format(f))
                os.remove(f)
        # Read the result
        with open(output, 'rt') as f:
            raw = f.read()
            try:
                data = json.loads(raw)
            except json.decoder.JSONDecodeError:
                raise KiPlotConfigurationError(f"Corrupted {nm} report `{output}`:\n{raw}")
        if data.get('$schema', '') != f'https://schemas.kicad.org/{nml}.v1.json':
            logger.warning(f'{wjson}Unknown JSON schema, {nm} might fail')
        self.units = data.get('coordinate_units', 'mm')
        # Apply KiBot filters
        self.apply_filters(data)
        # Generate the desired output format
        for (f, output) in zip(self._format, outputs):
            if f == 'CSV':
                res = self.create_csv(data)
            elif f == 'HTML':
                res = self.create_html(data)
            elif f == 'JSON':
                res = self.create_json(data)
            else:
                res = self.create_txt(data)
            # Write it to the output file
            with open(output, 'wt') as f:
                f.write(res)
        # Sanity check
        if self._dont_stop and self.c_warn and log.stop_on_warnings:
            logger.error("Inconsistent options, asked to don't stop, but also to stop on warnings")
        # Report the result
        revert_stop_on_warnings = False
        if self.c_warn and log.stop_on_warnings:
            revert_stop_on_warnings = True
            log.stop_on_warnings = False
        self.report('warning', self.c_warn, data)
        if revert_stop_on_warnings:
            log.stop_on_warnings = True
            logger.check_warn_stop()
        self.report('error', self.c_err, data)
        # Check the final status
        error_level = -1 if self._dont_stop else err
        if self.c_err:
            GS.exit_with_error(f'{nm} errors: {self.c_err}', error_level)
        elif self.c_warn and (self._warnings_as_errors or erc_warnings):  # noqa: F821
            GS.exit_with_error(f'{nm} warnings: {self.c_warn}, promoted as errors', error_level)
