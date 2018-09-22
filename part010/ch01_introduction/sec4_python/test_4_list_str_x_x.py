# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
list_val = [1, '3', 5 ,'4']
################################################################################
list_val = [1, '3', 5 ,'4']
list_val = range(5,0, -1)
print(list_val)
################################################################################
list_val = [1, '3', 5 ,'4']
list_val = list(range(5,0, -1))
print(list_val)
################################################################################
list_val = [1, '3', 5 ,'4']
list_val.append(6)
print(list_val)
list_val = [1, '3', 5 ,'4']
list_val = list_val + [7,8]
print(list_val)
################################################################################
list_val = [1, '3', 5 ,'4']
list_val.extend([9, 10])
list_val
################################################################################
list_val = [1, '3', 5 ,'4']
list_val.insert(7, 6)
print(list_val)
################################################################################
list_val = [1, '3', 5 ,'4']
tep_a = list_val.pop()
print(list_val)
print(tep_a)
list_val = [1, '3', 5 ,'4']
tep_a = list_val.pop(3)
print(list_val)
print(tep_a)
################################################################################
list_val = [1, '3', 5 ,'4','3']
val_index = list_val.index('4')
print(list_val)
print(val_index)
################################################################################
list_val = [1, '3', 5 ,'4']
list_val.remove('3')
list_val
################################################################################
list_val = ['1', '3', '5' ,'4']
list_val.sort()
print(list_val)
################################################################################
list_val = [1, '3', 5 ,'4']
list_val.reverse()
print(list_val)
################################################################################
a = range(8)
print(a)
b = tuple(a)
print(b)
c = list(b)
print(c)
################################################################################
list_val = range(8,0, -1)
print(list_val)
index_list = range(8)
for index in index_list:
    print('  Index: %d'%(index))
    print(list_val[index])
print(list_val[-2])
print(list_val[2:])
print(list_val[2:-2])
print(list_val[:])
################################################################################
dict_demo = {'GIS': 'Geographic Information System',
        'RS': 'Remote Sencing',
        'GPS': 'Global Positioning System',
        'DEM': 'Dynamic Effect Model'}
################################################################################
print(dict_demo['GPS'])
################################################################################
print(dict_demo.items())
################################################################################
dict_demo['DEM'] = 'Digital Elevation Model'
dict_demo['DEM']
################################################################################
print( 'RS' in dict_demo)
print( 'rs' in dict_demo)
dict_demo['rs'] = 'Remote Sencing'
print(dict_demo.keys())
del(dict_demo['rs'])
dict_demo.keys()
for s_name, l_name in dict_demo.items():
    print(('Short: %4s -> Long: %s') % (s_name, l_name))

