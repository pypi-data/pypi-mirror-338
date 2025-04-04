# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.DATABOX.
#
# SENAITE.DATABOX is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2018-2025 by it's authors.
# Some rights reserved, see README and LICENSE.

from bika.lims.api import get_portal
from senaite.databox import is_installed
from senaite.databox.setuphandlers import setup_navigation_types
from senaite.databox import logger


def afterUpgradeStepHandler(event):
    """Event handler that is executed after running an upgrade step of senaite.core
    """
    if not is_installed():
        return
    logger.info("Run senaite.databox.afterUpgradeStepHandler ...")
    portal = get_portal()
    setup_navigation_types(portal)
    logger.info("Run senaite.databox.afterUpgradeStepHandler [DONE]")
