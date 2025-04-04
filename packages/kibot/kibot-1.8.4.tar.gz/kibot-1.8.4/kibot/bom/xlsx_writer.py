# -*- coding: utf-8 -*-
# Copyright (c) 2020-2022 Salvador E. Tropea
# Copyright (c) 2020-2022 Instituto Nacional de Tecnología Industrial
# Copyright (c) 2016-2020 Oliver Henry Walters (@SchrodingersGat)
# License: MIT
# Project: KiBot (formerly KiPlot)
# Adapted from: https://github.com/SchrodingersGat/KiBoM
"""
XLSX Writer: Generates an XLSX BoM file.
"""
import io
import pprint
import os.path as op
import sys
import logging
import html
from textwrap import wrap
from base64 import b64decode
from .columnlist import ColumnList
from .kibot_logo import KIBOT_LOGO
from .. import log
from ..misc import W_NOKICOST, W_UNKDIST, KICOST_ERROR, W_BADFIELD
from ..gs import GS
from .. import __version__
# Init the logger first
logger = log.get_logger()
# XLSX Writer support
try:
    from xlsxwriter import Workbook
    XLSX_SUPPORT = True
except ModuleNotFoundError:
    XLSX_SUPPORT = False

    class Workbook():
        pass
# KiCost support
try:
    # Give priority to submodules
    rel_path = '../../submodules/KiCost/'
    if op.isfile(op.join(op.dirname(__file__), rel_path+'kicost/__init__.py')):
        rel_path = op.abspath(op.join(op.dirname(__file__), rel_path))
        if rel_path not in sys.path:
            sys.path.insert(0, rel_path)
    # Import all needed stuff
    from kicost import (PartGroup, KiCostError, query_part_info, solve_parts_qtys, configure_kicost_apis, ProgressConsole,
                        init_all_loggers, create_worksheet, Spreadsheet, get_distributors_list, get_dist_name_from_label,
                        set_distributors_progress, is_valid_api)
    from kicost import __version__ as kicost_version
    KICOST_SUPPORT = True
except ImportError:
    KICOST_SUPPORT = False
    ProgressConsole = object

BG_GEN = "#E6FFEE"  # "#C6DFCE"
BG_KICAD = "#FFE6B3"  # "#DFC693"
BG_USER = "#E6F9FF"  # "#C6D9DF"
BG_EMPTY = "#FF8080"
BG_GEN_L = "#F0FFF4"
BG_KICAD_L = "#FFF0BD"
BG_USER_L = "#F0FFFF"
BG_EMPTY_L = "#FF8A8A"
BG_COLORS = [[BG_GEN, BG_GEN_L], [BG_KICAD, BG_KICAD_L], [BG_USER, BG_USER_L], [BG_EMPTY, BG_EMPTY_L]]
GREY = "#dddddd"
GREY_L = "#f3f3f3"
HEAD_COLOR_R = "#982020"
HEAD_COLOR_G = "#009879"
HEAD_COLOR_B = "#0e4e8e"
DEFAULT_FMT = {'text_wrap': True, 'align': 'center_across', 'valign': 'vcenter'}
KICOST_COLUMNS = {'refs': ColumnList.COL_REFERENCE,
                  'desc': ColumnList.COL_DESCRIPTION,
                  'qty': ColumnList.COL_GRP_BUILD_QUANTITY}
SPECS_GENERATED = {ColumnList.COL_REFERENCE_L, ColumnList.COL_ROW_NUMBER_L, 'sep'}


# Progress bar for KiCost, we just add a filter to the logger
# This filter is needed because we have full debug enabled and we filter the log_level manually
# So we can generate a full log when in --quick-start mode (using a file)
class ProgressConsole2(ProgressConsole):
    def __init__(self, total, logger):
        super().__init__(total, logger)
        self.logTqdmHandler.addFilter(log.FilterNoInfo())


def bg_color(col):
    """ Return a background color for a given column title """
    col = col.lower()
    # Auto-generated columns
    if col in ColumnList.COLUMNS_GEN_L:
        return 0
    # KiCad protected columns
    elif col in ColumnList.COLUMNS_PROTECTED_L:
        return 1
    # Additional user columns
    return 2


def add_info(worksheet, column_widths, row, col_offset, formats, text, value):
    worksheet.write_string(row, col_offset, text, formats[0])
    if isinstance(value, (int, float)):
        worksheet.write_number(row, col_offset+1, value, formats[1])
        value = str(value)
    else:
        worksheet.write_string(row, col_offset+1, value, formats[1])
    column_widths[col_offset] = max(len(text)+1, column_widths[col_offset])
    column_widths[col_offset+1] = max(len(value), column_widths[col_offset+1])
    return row + 1


def title_rows(cfg):
    return (1 if cfg.xlsx.title else 0)+len(cfg.xlsx.extra_info)


def compute_head_size(cfg):
    col_logo = 0 if cfg.xlsx.logo is None else 6
    col_info = title_rows(cfg)
    if not (cfg.xlsx.hide_pcb_info and cfg.xlsx.hide_stats_info):
        col_info += 5
        if len(cfg.aggregate) > 1:
            col_info += 6*len(cfg.aggregate)
    head_size = max(col_logo, col_info)
    if head_size:
        # To separate
        head_size += 1
    return head_size


def get_bg_color(style_name):
    head_color = None
    if style_name.startswith('modern-'):
        if style_name.endswith('green'):
            head_color = HEAD_COLOR_G
        elif style_name.endswith('blue'):
            head_color = HEAD_COLOR_B
        else:
            head_color = HEAD_COLOR_R
    return head_color


def create_fmt_head(workbook, style_name):
    fmt_head = workbook.add_format(DEFAULT_FMT)
    fmt_head.set_bold()
    if style_name.startswith('modern-'):
        fmt_head.set_bg_color(get_bg_color(style_name))
        fmt_head.set_font_color("#ffffff")
    return fmt_head


def get_logo_data(logo):
    if logo is not None:
        if logo:
            with open(logo, 'rb') as f:
                image_data = f.read()
        else:
            image_data = b64decode(KIBOT_LOGO)
    else:
        image_data = None
    return image_data


def create_fmt_title(workbook, title):
    if not title:
        return None
    fmt_title = workbook.add_format(DEFAULT_FMT)
    fmt_title.set_font_size(24)
    fmt_title.set_bold()
    fmt_title.set_font_name('Arial')
    fmt_title.set_align('left')
    return fmt_title


def create_fmt_subtitle(workbook):
    fmt_title = workbook.add_format(DEFAULT_FMT)
    fmt_title.set_font_size(18)
    fmt_title.set_bold()
    fmt_title.set_font_name('Arial')
    fmt_title.set_align('left')
    return fmt_title


def create_fmt_cols(workbook, col_colors):
    """ Create the possible column formats """
    fmt_cols = []
    if col_colors:
        for c in BG_COLORS:
            fmts = [None, None]
            fmts[0] = workbook.add_format(DEFAULT_FMT)
            fmts[1] = workbook.add_format(DEFAULT_FMT)
            fmts[0].set_bg_color(c[0])
            fmts[1].set_bg_color(c[1])
            fmt_cols.append(fmts)
    else:
        fmts = [None, None]
        fmts[0] = workbook.add_format(DEFAULT_FMT)
        fmts[1] = workbook.add_format(DEFAULT_FMT)
        fmts[0].set_bg_color(GREY)
        fmts[1].set_bg_color(GREY_L)
        fmt_cols.append(fmts)
    return fmt_cols


def create_col_fmt(col_fields, col_colors, fmt_cols):
    """ Assign a color to each column """
    col_fmt = []
    if col_colors:
        for c in col_fields:
            col_fmt.append(fmt_cols[bg_color(c)])
    else:
        for _ in col_fields:
            col_fmt.append(fmt_cols[0])
    # Empty color
    col_fmt.append(fmt_cols[-1])
    return col_fmt


def create_row_fmt(workbook, row_colors):
    """ Assign a color to each highlighted row """
    for r in row_colors:
        fmt = workbook.add_format(DEFAULT_FMT)
        fmt.set_bg_color(r.color)
        r.xlsx_fmt = fmt


def create_fmt_info(workbook, cfg):
    """ Formats for the PCB and stats info """
    if cfg.xlsx.hide_pcb_info and cfg.xlsx.hide_stats_info and not cfg.xlsx.extra_info:
        return None
    # Data left justified
    fmt_data = workbook.add_format({'align': 'left'})
    fmt_name = workbook.add_format(DEFAULT_FMT)
    fmt_name.set_bold()
    fmt_name.set_align('left')
    return [fmt_name, fmt_data]


def insert_logo(worksheet, image_data, scale):
    """ Inserts the logo, returns how many columns we used """
    if image_data:
        # Note: OpenOffice doesn't support using images in the header for XLSXs
        # worksheet.set_header('&L&[Picture]', {'image_left': 'logo.png', 'image_data_left': image_data})
        options = {'image_data': io.BytesIO(image_data),
                   'x_scale': scale,
                   'y_scale': scale,
                   'object_position': 1,
                   'decorative': True}
        worksheet.insert_image('A1', 'logo.png', options)
        return 2
    return 0


def create_color_ref(workbook, col_colors, hl_empty, fmt_cols, do_kicost, kicost_colors, row_colors):
    if not (col_colors or row_colors or do_kicost):
        return
    row = 0
    worksheet = workbook.add_worksheet('Colors')
    max_w = 50
    if col_colors:
        worksheet.write_string(0, 0, 'Columns colors')
        worksheet.write_string(1, 0, 'KiCad Fields (default)', fmt_cols[1][0])
        worksheet.write_string(2, 0, 'Generated Fields', fmt_cols[0][0])
        worksheet.write_string(3, 0, 'User Fields', fmt_cols[2][0])
        row = 5
        if hl_empty:
            worksheet.write_string(4, 0, 'Empty Fields', fmt_cols[3][0])
            row = 6
        max_w = 22
    if row_colors:
        worksheet.write_string(row, 0, 'Row colors')
        row += 1
        for r in row_colors:
            worksheet.write_string(row, 0, r.description, r.xlsx_fmt)
            max_w = max(max_w, len(r.description))
            row += 1
        row += 1
    if do_kicost:
        worksheet.write_string(row, 0, 'Costs sheet colors')
        for label, format in kicost_colors.items():
            row += 1
            worksheet.write_string(row, 0, label, format)
            max_w = max(max_w, len(label))
    worksheet.set_column(0, 0, max_w)


def get_spec(part, name):
    if name[0] != '_':
        return part.specs.get(name, ['', ''])
    name = name[1:]
    for v in part.dd.values():
        val = v.extra_info.get(name, None)
        if val:
            return [name, val]
    return ['', '']


def create_meta(workbook, name, columns, parts, fmt_head, fmt_cols, max_w, rename, levels, comments, join):
    worksheet = workbook.add_worksheet(name)
    col_w = []
    row_h = 1
    for c, col in enumerate(columns):
        name = rename.get(col.lower(), col) if rename else col
        worksheet.write_string(0, c, name, fmt_head)
        text_l = max(len(col), 6)
        if text_l > max_w:
            h = len(wrap(col, max_w))
            row_h = max(row_h, h)
            text_l = max_w
        col_w.append(text_l)
    if row_h > 1:
        worksheet.set_row(0, 15.0*row_h)
    for r, part in enumerate(parts):
        # Add the references as another spec
        part.specs[ColumnList.COL_REFERENCE_L] = (ColumnList.COL_REFERENCE, part.collapsed_refs)
        # Also add the row
        part.specs[ColumnList.COL_ROW_NUMBER_L] = (ColumnList.COL_ROW_NUMBER, str(r+1))
        row_h = 1
        for c, col in enumerate(columns):
            col_l = col.lower()
            if col_l == 'sep':
                col_w[c] = 0
                continue
            v = get_spec(part, col_l)
            text = v[1]
            # Append text from other fields
            if join:
                for j in join:
                    if j[0] == col_l:
                        for c_join in j[1:]:
                            v = part.specs.get(c_join, None)
                            if v:
                                text += ' ' + v[1]
            text_l = len(text)
            if not text_l:
                continue
            fmt_kind = 0 if col_l in SPECS_GENERATED else 2
            text = html.unescape(text)
            logger.debugl(3, 'Spec ({},{}): `{}`'.format(r, c, text))
            worksheet.write_string(r+1, c, text, fmt_cols[fmt_kind][r % 2])
            if text_l > col_w[c]:
                if text_l > max_w:
                    h = len(wrap(text, max_w))
                    row_h = max(row_h, h)
                    text_l = max_w
                col_w[c] = text_l
        if row_h > 1:
            worksheet.set_row(r+1, 15.0*row_h)
    for i, width in enumerate(col_w):
        ops = {'level': levels[i] if levels else 0}
        if not width:
            ops['hidden'] = 1
        if comments and comments[i]:
            worksheet.write_comment(0, i, comments[i])
        worksheet.set_column(i, i, width, None, ops)


def adjust_widths(worksheet, column_widths, max_width, levels):
    c_levels = len(levels)
    for i, width in enumerate(column_widths):
        if width > max_width:
            width = max_width
        if i < c_levels:
            worksheet.set_column(i, i, width, None, {'level': levels[i]})


def adjust_heights(worksheet, rows, max_width, head_size):
    for rn, r in enumerate(rows):
        max_h = 1
        for c in r:
            if len(c) > max_width:
                h = len(wrap(c, max_width))
                max_h = max(h, max_h)
        if max_h > 1:
            worksheet.set_row(head_size+rn, 15.0*max_h)


def write_info(cfg, r_info_start, worksheet, column_widths, col1, fmt_info, fmt_subtitle, compact=False):
    vname = cfg.variant.name if cfg.variant else 'default'
    if len(cfg.aggregate) == 1:
        # Only one project
        rc = r_info_start
        if not cfg.xlsx.hide_pcb_info:
            prj = cfg.aggregate[0]
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Schematic:", prj.name)
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Variant:", vname)
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Revision:", prj.sch.revision)
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Date:", prj.sch.date)
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "KiCad Version:", cfg.kicad_version)
            col1 += 2
        rc = r_info_start
        if not cfg.xlsx.hide_stats_info:
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Component Groups:", cfg.n_groups)
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Component Count:", cfg.total_str)
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Fitted Components:", cfg.fitted_str)
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Number of PCBs:", cfg.number)
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Total Components:", cfg.n_build)
    else:
        # Multiple projects
        # Global stats
        old_col1 = col1
        rc = r_info_start
        if not cfg.xlsx.hide_pcb_info:
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Variant:", vname)
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "KiCad Version:", cfg.kicad_version)
            col1 += 2
        rc = r_info_start
        if not cfg.xlsx.hide_stats_info:
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Component Groups:", cfg.n_groups)
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Component Count:", cfg.total_str)
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Fitted Components:", cfg.fitted_str)
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Number of PCBs:", cfg.number)
            rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Total Components:", cfg.n_build)
        # Individual stats
        # No need to waste space for a column with no data
        r_info_start += 3 if cfg.xlsx.hide_stats_info and compact else 5
        for prj in cfg.aggregate:
            col1 = old_col1
            worksheet.set_row(r_info_start, 24)
            worksheet.merge_range(r_info_start, col1, r_info_start, len(column_widths)-1, prj.sch.title, fmt_subtitle)
            r_info_start += 1
            rc = r_info_start
            if not cfg.xlsx.hide_pcb_info:
                rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Schematic:", prj.name)
                rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Revision:", prj.sch.revision)
                rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Date:", prj.sch.date)
                if prj.sch.company:
                    rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Company:", prj.sch.company)
                if prj.ref_id:
                    rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "ID:", prj.ref_id)
                col1 += 2
            rc = r_info_start
            if not cfg.xlsx.hide_stats_info:
                rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Component Groups:", prj.comp_groups)
                rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Component Count:", prj.total_str)
                rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Fitted Components:", prj.fitted_str)
                rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Number of PCBs:", prj.number)
                rc = add_info(worksheet, column_widths, rc, col1, fmt_info, "Total Components:", prj.comp_build)
            r_info_start += 5


def adapt_extra_cost_columns(cfg):
    if not cfg.columns_ce:
        return
    user_fields = []
    for i, col in enumerate(cfg.columns_ce):
        data = {'field': col}
        comment = cfg._column_comments_ce[i]
        if comment:
            data['comment'] = comment
        level = cfg._column_levels_ce[i]
        if level:
            data['level'] = level
        col = col.lower()
        if col in cfg._column_rename_ce:
            data['label'] = cfg._column_rename_ce[col]
        user_fields.append(data)
    Spreadsheet.USER_FIELDS = user_fields


def apply_join_requests(join, adapted, original):
    if not join:
        return
    for join_l in join:
        # Each list is "target, source..." so we need at least 2 elements
        elements = len(join_l)
        target = join_l[0]
        append = ''
        if elements > 1:
            # Append data from the other fields
            for source in join_l[1:]:
                v = source.get_text(original.get)
                if v:
                    append += v
        if append:
            adapted[target] = original.get(target, '') + append


def remove_unknown_distributors(distributors, available, silent):
    new_distributors = []
    for d in distributors:
        d = d.lower()
        if d not in available:
            # Is the label of the column?
            new_d = get_dist_name_from_label(d)
            if new_d is not None:
                d = new_d
        if d not in available:
            if not silent:
                logger.warning(W_UNKDIST+'Unknown distributor `{}`'.format(d))
        else:
            new_distributors.append(d)
    return new_distributors


def solve_distributors(cfg, silent=True):
    # List of distributors to scrape
    available = get_distributors_list()
    include = remove_unknown_distributors(cfg.distributors, available, silent)
    exclude = remove_unknown_distributors(cfg.no_distributors, available, silent)
    # Default is to sort the entries
    Spreadsheet.SORT_DISTRIBUTORS = True
    if not include:
        # All by default
        dist_list = available
    else:
        # Requested to be included
        dist_list = include
        # Keep user sorting
        Spreadsheet.SORT_DISTRIBUTORS = False
    # Requested to be excluded
    for d in exclude:
        dist_list.remove(d)
    Spreadsheet.DISTRIBUTORS = dist_list
    return dist_list


def compute_qtys(cfg, g):
    if len(cfg.aggregate) == 1:
        return str(g.get_count())
    return [str(g.get_count(sch.name)) for sch in cfg.aggregate]


def create_meta_sheets(workbook, used_parts, fmt_head, fmt_cols, cfg, ss):
    if cfg.xlsx.specs:
        meta_names = ['Specs', 'Specs (DNF)']
        for ws in range(2):
            spec_cols = {}
            spec_cols_l = set()
            parts = used_parts[ws]
            for part in parts:
                for name_l, v in part.specs.items():
                    spec_cols_l.add(name_l)
                    spec = v[0]
                    if spec in spec_cols:
                        spec_cols[spec] += 1
                    else:
                        spec_cols[spec] = 1
            if len(spec_cols):
                columns = cfg.xlsx.s_columns
                if columns is None:
                    # Use all columns, sort them by relevance (most used) and alphabetically
                    c = len(parts)
                    columns = sorted(spec_cols, key=lambda k: (c - spec_cols[k], k))
                    columns.insert(0, ColumnList.COL_REFERENCE)
                else:
                    # Inform about missing columns
                    for c in columns:
                        col = c.lower()
                        if ((col[0] == '_' and col[1:] not in ss.extra_info_display) or
                           (col[0] != '_' and col not in spec_cols_l and col not in SPECS_GENERATED)):
                            logger.warning(W_BADFIELD+'Invalid Specs column name `{}` {}'.format(c, col[1:]))
                create_meta(workbook, meta_names[ws], columns, parts, fmt_head, fmt_cols, cfg.xlsx.max_col_width,
                            cfg.xlsx.s_rename, cfg.xlsx.s_levels, cfg.xlsx.s_comments, cfg.xlsx.s_join)


def adapt_column_names(cfg):
    for id, v in Spreadsheet.GLOBAL_COLUMNS.items():
        if id in KICOST_COLUMNS:
            # We use another name
            new_id = KICOST_COLUMNS[id]
            v['label'] = new_id
            id = new_id.lower()
        if id in cfg._column_rename:
            v['label'] = cfg._column_rename[id]


def dis_enable_apis(api_options, cfg):
    """ Callback used during KiCost initialization to dis/enable APIs """
    # Filter which APIs we want
    for api in cfg.xlsx.kicost_api_disable:
        if is_valid_api(api):
            api_options[api]['enable'] = False
    for api in cfg.xlsx.kicost_api_enable:
        if is_valid_api(api):
            api_options[api]['enable'] = True


def do_title(cfg, worksheet, col1, length, fmt_title, fmt_info):
    r_extra = 0
    if cfg.xlsx.title:
        worksheet.set_row(0, 32)
        worksheet.merge_range(0, col1, 0, length, cfg.xlsx.title, fmt_title)
        r_extra = 1
    for c, text in enumerate(cfg.xlsx.extra_info):
        worksheet.merge_range(c+r_extra, col1, c+r_extra, length, text, fmt_info)


def copy_specs_to_components(parts, groups):
    """ Link the KiCost information in the components.
        So we can access to the specs for the components.
        This can be used by filters. """
    for p in parts:
        for c in p.kibot_group.components:
            c.kicost_part = p
            if hasattr(c, 'original_copy'):
                c.original_copy.kicost_part = p


def _create_kicost_sheet(workbook, groups, image_data, fmt_title, fmt_info, fmt_subtitle, fmt_head, fmt_cols, cfg):
    if not KICOST_SUPPORT:
        logger.warning(W_NOKICOST+'KiCost sheet requested but failed to load KiCost support')
        return
    logger.debug("Using KiCost v"+kicost_version)
    if cfg.debug_level > 2:
        logger.debug("Groups exported to KiCost:")
        for g in groups:
            logger.debug(pprint.pformat(g.__dict__))
            logger.debug("-- Components")
            for c in g.components:
                logger.debug(pprint.pformat(c.__dict__))
    # Force KiCost to use our logger
    init_all_loggers(log.get_logger('kicost', indent=1), log.get_logger('kicost.dist', indent=1),
                     log.get_logger('kicost.eda', indent=1))
    set_distributors_progress(ProgressConsole2)
    if GS.debug_enabled:
        logger.setLevel(logging.DEBUG+1-GS.debug_level)
    # Load KiCost config (includes APIs config)
    configure_kicost_apis(cfg.xlsx.kicost_config, True, dis_enable_apis, cfg)
    # Create the projects information structure
    prj_info = [{'title': p.name, 'company': p.sch.company, 'date': p.sch.date, 'qty': p.number} for p in cfg.aggregate]
    # Create the worksheets
    ws_names = ['Costs', 'Costs (DNF)']
    Spreadsheet.PRJ_INFO_ROWS = 5 if len(cfg.aggregate) == 1 else 6
    Spreadsheet.PRJ_INFO_START = (1 if len(cfg.aggregate) == 1 else 4)+len(cfg.xlsx.extra_info)
    Spreadsheet.ADJUST_ROW_AND_COL_SIZE = True
    Spreadsheet.MAX_COL_WIDTH = cfg.xlsx.max_col_width
    Spreadsheet.PART_NSEQ_SEPRTR = cfg.ref_separator
    Spreadsheet.SUPPRESS_DIST_DESC = not cfg.xlsx.kicost_dist_desc
    # Keep our sorting
    Spreadsheet.SORT_GROUPS = False
    # Make the version less intrusive
    Spreadsheet.WRK_FORMATS['about_msg']['font_size'] = 8
    # Don 't add project info, we add our own data
    Spreadsheet.INCLUDE_PRJ_INFO = False
    # Move the date to the bottom, and make it less relevant
    Spreadsheet.ADD_DATE_TOP = False
    Spreadsheet.ADD_DATE_BOTTOM = True
    Spreadsheet.WRK_FORMATS['proj_info_field']['font_size'] = 11
    Spreadsheet.WRK_FORMATS['proj_info']['font_size'] = 11
    Spreadsheet.DATE_FIELD_LABEL = 'Created:'
    # Set the color for the global section (using the selected theme)
    bg_color = get_bg_color(cfg.xlsx.style)
    if bg_color:
        Spreadsheet.WRK_FORMATS['global']['bg_color'] = bg_color
        Spreadsheet.WRK_FORMATS['header']['bg_color'] = bg_color
        Spreadsheet.WRK_FORMATS['header']['font_color'] = 'white'
    Spreadsheet.WRK_FORMATS['global']['font_size'] = 12
    Spreadsheet.WRK_FORMATS['header']['font_size'] = 11
    # Avoid the use of the same color twice
    Spreadsheet.WRK_FORMATS['order_too_much']['bg_color'] = '#FF4040'
    Spreadsheet.WRK_FORMATS['order_min_qty']['bg_color'] = '#FF6060'
    # Project quantity as the default quantity
    Spreadsheet.DEFAULT_BUILD_QTY = cfg.number
    # Add version information
    Spreadsheet.ABOUT_MSG += ' + KiBot v'+__version__
    # References using ranges
    Spreadsheet.COLLAPSE_REFS = cfg.use_alt
    # Pass any extra column
    adapt_extra_cost_columns(cfg)
    # Adapt the column names
    adapt_column_names(cfg)
    used_parts = []
    for ws in range(2):
        # Second pass is DNF
        dnf = ws == 1
        # Should we generate the DNF?
        if dnf and (not cfg.xlsx.generate_dnf or cfg.n_total == cfg.n_fitted):
            used_parts.append([])
            break
        # Create the parts structure from the groups
        parts = []
        multi_prj = len(prj_info) > 1
        for g in groups:
            if (cfg.ignore_dnf and not g.is_fitted()) != dnf:
                continue
            part = PartGroup()
            part.refs = [c.ref for c in g.components]
            part.fields = g.fields
            part.fields['manf#_qty'] = compute_qtys(cfg, g)
            # Internally used to make copy_specs_to_components simpler
            part.kibot_group = g
            parts.append(part)
            # Process any "join" request
            apply_join_requests(cfg._join_ce, part.fields, g.fields)
        # Fill the quantity members of the parts
        solve_parts_qtys(parts, multi_prj, prj_info)
        # Distributors
        dist_list = solve_distributors(cfg)
        # Get the prices
        query_part_info(parts, dist_list)
        # Put the specs in the components
        copy_specs_to_components(parts, groups)
        # Distributors again. During `query_part_info` user defined distributors could be added
        solve_distributors(cfg, silent=False)
        # Create a class to hold the spreadsheet parameters
        ss = Spreadsheet(workbook, ws_names[ws], prj_info)
        wks = ss.wks
        # Page head
        # Logo
        col1 = insert_logo(wks, image_data, cfg.xlsx.logo_scale)
        if col1:
            col1 += 1
        # PCB & Stats Info
        if not (cfg.xlsx.hide_pcb_info and cfg.xlsx.hide_stats_info):
            r_info_start = title_rows(cfg)
            column_widths = [0]*5  # Column 1 to 5
            old_stats = cfg.xlsx.hide_stats_info
            cfg.xlsx.hide_stats_info = True
            write_info(cfg, r_info_start, wks, column_widths, col1, fmt_info, fmt_subtitle, compact=True)
            cfg.xlsx.hide_stats_info = old_stats
            ss.col_widths[col1] = column_widths[col1]
            ss.col_widths[col1+1] = column_widths[col1+1]
        # Add a worksheet with costs to the spreadsheet
        create_worksheet(ss, parts)
        # Title
        do_title(cfg, wks, col1, ss.globals_width, fmt_title, fmt_info[0])
        used_parts.append(parts)
    # Specs sheets
    create_meta_sheets(workbook, used_parts, fmt_head, fmt_cols, cfg, ss)
    colors = {}
    colors['Best price'] = ss.wrk_formats['best_price']
    colors['No manufacturer or distributor code'] = ss.wrk_formats['not_manf_codes']
    colors['Not available'] = ss.wrk_formats['not_available']
    colors['Purchase quantity is more than what is available'] = ss.wrk_formats['order_too_much']
    colors['Minimum order quantity not respected'] = ss.wrk_formats['order_min_qty']
    colors['Total available part quantity is less than needed'] = ss.wrk_formats['too_few_available']
    colors['Total purchased part quantity is less than needed'] = ss.wrk_formats['too_few_purchased']
    colors['This part is obsolete'] = ss.wrk_formats['part_format_obsolete']
    colors['This part is listed but is not normally stocked'] = ss.wrk_formats['not_stocked']
    return colors


def create_kicost_sheet(workbook, groups, image_data, fmt_title, fmt_info, fmt_subtitle, fmt_head, fmt_cols, cfg):
    try:
        return _create_kicost_sheet(workbook, groups, image_data, fmt_title, fmt_info, fmt_subtitle, fmt_head, fmt_cols, cfg)
    except KiCostError as e:
        GS.exit_with_error('KiCost error: `{}` ({})'.format(e.msg, e.id), KICOST_ERROR)


def write_xlsx(filename, groups, col_fields, head_names, cfg):
    """
    Write BoM out to a XLSX file
    filename = path to output file (must be a .csv, .txt or .tsv file)
    groups = [list of ComponentGroup groups]
    col_fields = [list of headings to search for data in the BoM file]
    head_names = [list of headings to display in the BoM file]
    cfg = BoMOptions object with all the configuration
    """
    if not XLSX_SUPPORT:
        logger.non_critical_error('Python xlsxwriter module not installed')
        return False

    link_datasheet = -1
    if cfg.xlsx.datasheet_as_link and cfg.xlsx.datasheet_as_link in col_fields:
        link_datasheet = col_fields.index(cfg.xlsx.datasheet_as_link)
    link_digikey = cfg.xlsx.digikey_link
    link_mouser = cfg.xlsx.mouser_link
    link_lcsc = cfg.xlsx.lcsc_link
    hl_empty = cfg.xlsx.highlight_empty

    workbook = Workbook(filename)
    ws_names = ['BoM', 'DNF']
    row_headings = head_names

    # Leave space for the logo, title and info
    head_size = compute_head_size(cfg)
    # First row for the information
    r_info_start = title_rows(cfg)
    max_width = cfg.xlsx.max_col_width

    # #######################
    # Create all the formats
    # #######################
    # Headings
    # Column names format
    fmt_head = create_fmt_head(workbook, cfg.xlsx.style)
    # Column formats
    fmt_cols = create_fmt_cols(workbook, cfg.xlsx.col_colors)
    col_fmt = create_col_fmt(col_fields, cfg.xlsx.col_colors, fmt_cols)
    create_row_fmt(workbook, cfg.xlsx.row_colors)
    # Page head
    # Logo
    image_data = get_logo_data(cfg.xlsx.logo)
    # Title
    fmt_title = create_fmt_title(workbook, cfg.xlsx.title)
    fmt_subtitle = create_fmt_subtitle(workbook)
    # Info
    fmt_info = create_fmt_info(workbook, cfg)

    # #######################
    # Fill the cells
    # #######################
    # Normal BoM & DNF
    for ws in range(2):
        # Second pass is DNF
        dnf = ws == 1
        # Should we generate the DNF?
        if dnf and (not cfg.xlsx.generate_dnf or cfg.n_total == cfg.n_fitted):
            break

        worksheet = workbook.add_worksheet(ws_names[ws])
        row_count = head_size

        # Headings
        # Create the head titles
        column_widths = [0]*max(len(col_fields), 6)
        rows = [row_headings]
        for i in range(len(row_headings)):
            # Title for this column
            column_widths[i] = len(row_headings[i]) + 10
            worksheet.write_string(row_count, i, row_headings[i], fmt_head)
            if cfg._column_comments[i]:
                worksheet.write_comment(row_count, i, cfg._column_comments[i])

        # Body
        row_count += 1
        for i, group in enumerate(groups):
            if (cfg.ignore_dnf and not group.is_fitted()) != dnf:
                continue
            # Get the data row
            row = group.get_row(col_fields)
            rows.append(row)
            if link_datasheet != -1:
                datasheet = group.get_field(ColumnList.COL_DATASHEET_L)
            # Check if the user wants a color for this row
            row_fmt = None
            for r_color in cfg.xlsx.row_colors:
                c = group.components[0]
                if r_color.filter.filter(c):
                    row_fmt = r_color.xlsx_fmt
                    break
            # Fill the row
            for i in range(len(row)):
                cell = row[i]
                if row_fmt is not None:
                    fmt = row_fmt
                elif hl_empty and (len(cell) == 0 or cell.strip() == "~"):
                    fmt = col_fmt[-1][row_count % 2]
                else:
                    fmt = col_fmt[i][row_count % 2]
                # Link this column to the datasheet?
                if link_datasheet == i and datasheet.startswith('http'):
                    worksheet.write_url(row_count, i, datasheet, fmt, cell)
                # A link to Digi-Key?
                elif link_digikey and col_fields[i] in link_digikey:
                    url = 'https://www.digikey.com/products/en?keywords=' + cell
                    worksheet.write_url(row_count, i, url, fmt, cell)
                # A link to Mouser?
                elif link_mouser and col_fields[i] in link_mouser:
                    url = 'https://www.mouser.com/ProductDetail/' + cell
                    worksheet.write_url(row_count, i, url, fmt, cell)
                # A link to LCSC?
                elif link_lcsc and col_fields[i] in link_lcsc:
                    url = 'https://www.lcsc.com/product-detail/' + cell + '.html'
                    worksheet.write_url(row_count, i, url, fmt, cell)
                else:
                    worksheet.write_string(row_count, i, cell, fmt)
                if len(cell) > column_widths[i] - 5:
                    column_widths[i] = len(cell) + 5
            row_count += 1

        # Page head
        # Logo
        col1 = insert_logo(worksheet, image_data, cfg.xlsx.logo_scale)
        # Title
        do_title(cfg, worksheet, col1, len(column_widths)-1, fmt_title, fmt_info[0] if fmt_info else None)
        # PCB & Stats Info
        if not (cfg.xlsx.hide_pcb_info and cfg.xlsx.hide_stats_info):
            write_info(cfg, r_info_start, worksheet, column_widths, col1, fmt_info, fmt_subtitle)

        # Adjust cols and rows
        adjust_widths(worksheet, column_widths, max_width, cfg._column_levels)
        adjust_heights(worksheet, rows, max_width, head_size)

        worksheet.freeze_panes(head_size+1, 0)
        worksheet.repeat_rows(head_size+1)
        worksheet.set_landscape()

    # Optionally add KiCost information
    kicost_colors = None
    if cfg.xlsx.kicost:
        kicost_colors = create_kicost_sheet(workbook, groups, image_data, fmt_title, fmt_info, fmt_subtitle, fmt_head,
                                            fmt_cols, cfg)
    # Add a sheet for the color references
    create_color_ref(workbook, cfg.xlsx.col_colors, hl_empty, fmt_cols, cfg.xlsx.kicost and KICOST_SUPPORT, kicost_colors,
                     cfg.xlsx.row_colors)

    workbook.close()

    return True
