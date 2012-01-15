# Volatility
# Copyright (c) 2008 Volatile Systems
# Copyright (c) 2008 Brendan Dolan-Gavitt <bdolangavitt@wesleyan.edu>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details. 
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA 
#

import copy
import volatility.plugins.overlays.basic as basic
import volatility.plugins.overlays.windows.windows as windows

class AbstractWindowsX64(windows.AbstractWindowsX86):
    """ A Profile for Windows systems """
    _md_os = 'windows'
    _md_memory_model = '64bit'
    native_types = basic.x64_native_types
    object_classes = copy.deepcopy(windows.AbstractWindows.object_classes)
