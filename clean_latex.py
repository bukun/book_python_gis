

import os
import sys

latex_ws = './part010'

for wroot, wdirs, wfiles in os.walk(latex_ws):
    wfiles = [x for x in wfiles if x.endswith('.tex')]
    for wfile in wfiles:
        tex_file = os.path.join(wroot, wfile)
        print(tex_file)
        cnts = open(tex_file).readlines()

        with open(tex_file, 'w') as file_o:
            for cnt in cnts:
                xx_cnt = cnt.strip()
                if xx_cnt.startswith('%'):
                    continue

                file_o.write(cnt)