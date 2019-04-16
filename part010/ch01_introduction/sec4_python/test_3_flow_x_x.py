#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
a = 13
b = 50
if a > b:
     print('A is greater than B.')
else:
    print('B is greater than A.')

###############################################################################
rangs = range(1, 3)
for val in rangs:
    print(val)
else:
    print('The for loop is over')

###############################################################################
for i in range(1, 5):
    if i > 2:
        break
    print(i)

###############################################################################
for i in range(0, 5):
    if i % 2 == 1:
        print(i)
    else:
        continue

