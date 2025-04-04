# -*- coding: utf-8 -*-
# Copyright (c) 2020 Salvador E. Tropea
# Copyright (c) 2020 Instituto Nacional de Tecnologïa Industrial
# License: Apache 2.0
# Project: KiAuto (formerly kicad-automation-scripts)
"""
Tests for eeschema_do bom_xml.

For debug information use:
pytest-3 --log-cli-level debug

"""

import os
import sys
import logging
# Look for the 'utils' module from where the script is running
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(script_dir))
# Utils import
from utils import context

PROG = 'eeschema_do'


def test_bom_xml(test_dir):
    prj = 'good-project'
    ctx = context.TestContextSCH(test_dir, 'BoM_XML', prj)
    bom = ctx.board_file.replace(ctx.sch_ext, '.xml')
    if os.path.isfile(bom):
        os.remove(bom)
    cmd = [PROG, '-vv', '-r', '--time_out_scale', '0.9', 'bom_xml']
    ctx.run(cmd)
    ctx.expect_out_file(bom)
    logging.debug(bom)
    ctx.clean_up()
