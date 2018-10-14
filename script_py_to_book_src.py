# -*- coding: utf-8 -*-

'''
从Latex 源文件中，只把 Python 代码提取出来。
'''

import os
import sys

# basews = 'part010'
basews = os.path.abspath('./part010')
outws = os.path.abspath('./book_python_gis/pygis_src')

py_header_str = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''


def extractit(infile, outfile):
    has_code = False
    with open(outfile, 'w') as fo:
        fo.write(py_header_str)

        # indx = 1
        with open(infile) as fi:
            cnts = fi.readlines()
        in_code = False
        for cnt in cnts:
            if cnt.strip().startswith('%'):
                continue

            if '''begin{lstlisting}''' in cnt:
                has_code = True
                in_code = True
                fo.write('#' * 79 + '\n')
                # continue
            if '''end{lstlisting}''' in cnt:
                in_code = False

            if in_code:
                # print(cnt)
                if cnt.startswith('>>> ') or cnt.startswith('... '):
                    # print(cnt[4:])
                    the_code = cnt[4:]
                    fo.write(the_code)
                if cnt.strip() == '...':
                    fo.write('\n')

    if has_code:
        pass
    else:
        os.remove(outfile)


for wroot, wdirs, wfiles in os.walk(basews):

    for wfile in wfiles:
        if wfile.startswith('test') and wfile.endswith('.tex'):

            outdir = os.path.join(outws, wroot[len(basews) + 1:])
            if os.path.exists(outdir):
                pass
            else:
                os.makedirs(outdir)

            infile = os.path.join(wroot, wfile)
            outfile = os.path.join(outdir, wfile[:-4] + '_x_x' + '.py')
            dirname = os.path.dirname(outfile)
            if os.path.exists(dirname):
                pass
            else:
                os.makedirs(dirname)
            # initfile = os.path.join(dirname, '__init__.py')
            # if os.path.exists(initfile):
            #     pass
            # else:
            #     with open(initfile, 'w') as fo:
            #         pass

            extractit(infile, outfile)
            # print(outfile)
