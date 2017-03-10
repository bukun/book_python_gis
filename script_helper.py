# -*- coding: utf-8 -*-

'''
管理脚本的一些工具
'''

import os


def create_init():
    '''
    生成 __init__.py 文件
    :return:
    '''
    for wroot, wdirs, wfiles in os.walk('./pygis_src'):
        for wdir in wdirs:

            inws = os.path.join(wroot, wdir)
            if '/ch' in inws and '__pycache__' not in inws:
                initfile = os.path.join(inws, '__init__.py')

                if os.path.exists(initfile):
                    pass
                else:
                    print(inws)
                    with open(initfile, 'w') as fo:
                        fo.write('# -*- coding: utf-8 -*-')


def file_sig(new_arr):
    '''
    Python文件的特征名称
    :param new_arr:
    :return:
    '''
    new_arr.reverse()
    out_aa = []
    for x in new_arr:
        try:
            int(x)
            out_aa.append(x)
            break
        except:
            out_aa.append(x)
    out_aa.reverse()

    return '_'.join([x for x in out_aa])


def clear_tmp_files():
    for wroot, wdirs, wfiles in os.walk('./'):
        for wfile in wfiles:
            if wfile.startswith('xx_'):
                if wfile.endswith('.py'):
                    continue
                os.remove(os.path.join(wroot, wfile))
                continue


def format_filename():
    '''
    对 Python 文件进行名称格式化
    :return:
    '''
    for wroot, wdirs, wfiles in os.walk('./pygis_src'):
        for wfile in wfiles:

            if (wfile.endswith('.py') or wfile.endswith('.sh') or wfile.endswith('.sql')) and wfile.startswith('test'):
                if wfile == '__init__.py':
                    continue
                print('-' * 80)
                # print(os.path.join(wroot, wfile))
                uu = wroot.split('/')
                ch_num = int(uu[2].split('_')[0][2:])
                sec_num = int(uu[3].split('_')[0][3:])

                new_arr = wfile.split('_')

                new_name = 'test_{ch}_{sec}_{res}'.format(ch=ch_num, sec=sec_num, res=file_sig(new_arr))

                from_file = os.path.join(wroot, wfile)
                to_file = os.path.join(wroot, new_name)
                if from_file == to_file:
                    pass
                else:
                    print(from_file)
                    print(to_file)

                    os.rename(from_file, to_file)


if __name__ == '__main__':
    clear_tmp_files()
    format_filename()
