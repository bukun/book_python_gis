# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
cvs_text = '''Author,Book,Lang,Price
"Magnus Lie Hetland","Python基础教程(第3版)","中文","75.3"
"Bill Kropla","Beginning MapServer","English","344"
"Jake VanderPlas","Python数据科学手册","中文","83.9"
"Osvaldo Martin","Python贝叶斯分析","中文","54.4"
'''

################################################################################
with open('xx_out.txt', 'w') as fo:
    fo.write(cvs_text)

################################################################################

import sqlite3 as sqlite
con = sqlite.connect(':memory:')
con.enable_load_extension(True)
con.execute('SELECT load_extension("mod_spatialite.so.7")')
cur = con.cursor()
sql = '''CREATE VIRTUAL TABLE books USING VirtualText(
    xx_out.txt, utf8, 1, COMMA, DOUBLEQUOTE, ',')'''

cur.execute(sql)

################################################################################
cur.execute('PRAGMA table_info(books)')
for rec in cur: print(rec)


################################################################################
cur.execute('''SELECT Book, Author FROM Books
    WHERE Lang = '中文' ''')

for rec in cur: print(rec)

