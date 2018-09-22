# # -*- coding: utf-8 -*-
# '''
# 生成绘图的图标
# pip3 install canvasvg
# pip install canvasvg
#
# aptitude install -y python-cairosvg python3-cairosvg
# '''
# from helper.textool import get_tmp_file
# import canvasvg
# import cairosvg
#
# import turtle
#
# turtle.ht()
# turtle.color("purple")
# turtle.pensize(2)
# turtle.goto(4, 8)
# turtle.goto(8, 0)
# turtle.goto(0, 0)
#
# ts = turtle.getscreen()
#
# ts = turtle.getscreen().getcanvas()
#
# tmpfile = 'xx_tmp.svg'
#
# result_png = get_tmp_file(__file__, 't', file_ext='png')
#
# canvasvg.saveall(tmpfile, ts)
# with open(tmpfile) as svg_input, open(result_png, 'wb') as png_output:
#     cairosvg.svg2png(bytestring=svg_input.read(), write_to=png_output)
#
#
# # canvasvg.saveall(get_tmp_file(__file__, 't', file_ext='svg'), ts)
