# GPLv3 License
#
# Copyright (C) 2020 Ubisoft
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
This module defines the global variables used in the addon.
"""

import bpy

import os
from pathlib import Path
import bpy.utils.previews


def init_global_variables():

    # icons ############
    global icons_col

    pcoll = bpy.utils.previews.new()
    my_icons_dir = os.path.join(os.path.dirname(__file__), "./icons")
    for png in Path(my_icons_dir).rglob("*.png"):
        pcoll.load(png.stem, str(png), "IMAGE")

    icons_col = pcoll


def release_global_variables():

    global icons_col

    bpy.utils.previews.remove(icons_col)
    icons_col = None
