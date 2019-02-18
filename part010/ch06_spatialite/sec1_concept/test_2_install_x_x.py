# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import sqlite3
con = sqlite3.connect(":memory:")
con.enable_load_extension(True)

################################################################################

################################################################################
import sqlite3
con = sqlite3.connect(":memory:")
con.enable_load_extension(True)
con.execute('SELECT load_extension("mod_spatialite.so.7")')
