# -*- coding: utf-8 -*-

'''
从Latex 源文件中，只把标题，图片提取出来 。
'''

import os
import sys
import shutil

inws = os.path.abspath('./part010')
outws = os.path.abspath('./part010_pdf')


def extract_it(in_tex):
    out_str = ''
    with open(in_tex) as f_in:
        cnts = f_in.readlines()
        is_figure = False

        for cnt in cnts:
            cnt_clean = cnt.strip()

            if is_figure:
                # out_str = out_str + cnt
                if cnt_clean.startswith('\end{figure}'):
                    is_figure = False
            else:
                if cnt_clean.startswith('\chapter'):
                    pass
                elif cnt_clean.startswith('\section'):
                    pass
                elif cnt_clean.startswith('\subsection{'):
                    pass
                # elif cnt_clean.startswith('\subsubsection{'):
                #     pass
                elif cnt_clean.startswith('\input{'):
                    pass
                elif cnt_clean.startswith(r'%%%% ==== %%%% ==== %%%% ==== %%%%'):
                    pass
                elif cnt_clean.startswith(r'\begin{figure}'):
                    is_figure = True


                else:
                    continue

            out_str = out_str + cnt

    return out_str


for wroot, wdirs, wfiles in os.walk(inws):
    for wfile in wfiles:

        outdir = os.path.join(outws, wroot[len(inws) + 1:])
        if os.path.exists(outdir):
            pass
        else:
            os.makedirs(outdir)

        in_tex_file = os.path.join(wroot, wfile)
        out_text_file = os.path.join(outdir, wfile)

        if wfile.endswith('.tex'):
            pass

            with open(out_text_file, 'w') as f_out:
                f_out.write(extract_it(in_tex_file))
        elif wfile.endswith('.pdf'):
            shutil.copy(in_tex_file, out_text_file)

        print(outdir)
