# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2014, 2015 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Change JSON data type from TEXT to LONGTEXT."""

from invenio_upgrader.api import op

import sqlalchemy as sa

from sqlalchemy.dialects import mysql
from sqlalchemy.exc import OperationalError

depends_on = []


def info():
    """Return information about the upgrade recipe."""
    return __doc__


def do_upgrade():
    """Perform the update recipe."""
    try:
        op.alter_column(
            u'bibrec', 'additional_info',
            existing_type=mysql.TEXT(),
            type_=mysql.LONGTEXT(),
            nullable=True
        )
    except OperationalError:
        op.add_column('bibrec',
                      sa.Column('additional_info',
                                mysql.LONGTEXT(),
                                nullable=True)
                      )


def estimate():
    """Estimate running time of upgrade in seconds (optional)."""
    return 1
