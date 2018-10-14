# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import sqlite3
conn = sqlite3.connect(":memory:")
conn.enable_load_extension(True)

################################################################################

################################################################################

################################################################################
import sqlite3
conn = sqlite3.connect(":memory:")
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
