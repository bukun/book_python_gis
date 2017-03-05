# -*- coding: utf-8 -*-
import os
import sys

fo = open('xx_run.sh', 'w')
cws = os.getcwd()
for wroot, wdirs, wfiles in os.walk(cws):
    for wfile in wfiles:
        if wfile.endswith('.py'):
            if wfile == '__init__.py':
                continue
            pyfile = os.path.join(wroot, wfile)[len(cws) + 1:]
            print(pyfile)

            uu = pyfile.split('/')
            print(uu)
            if len(uu) > 1:
                outstr = '/'.join(uu)
                fo.write( 'python3 {0}\n'.format(outstr))

fo.close()
