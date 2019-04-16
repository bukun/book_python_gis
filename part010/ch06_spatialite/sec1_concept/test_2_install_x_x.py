#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import sqlite3
con = sqlite3.connect(":memory:")
con.enable_load_extension(True)
###############################################################################
###############################################################################
import sqlite3
con = sqlite3.connect(":memory:")
con.enable_load_extension(True)
con.execute('SELECT load_extension("mod_spatialite.so.7")')
