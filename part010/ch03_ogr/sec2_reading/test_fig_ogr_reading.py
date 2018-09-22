# -*- coding: utf-8 -*-

'''
注意，使用的是：  `pygraphviz`， 另外，还有  `graphviz`
'''
import os
# from pygraphviz import Digraph

# from graphviz import Digraph, Graph

import pygraphviz as pgv

G = pgv.AGraph(directed=True)
# g = Graph(format='png')
# dot = Digraph()
# dot.format = 'png'
#
#
# dot = Digraph(comment='The Round Table')

G.add_edge('driver', 'datasource')
G.add_edge('datasource', 'layer')
G.add_edge('layer', 'feature')
G.add_edge('feature', 'geometry')
G.add_edge('geometry', 'wkt')
G.add_edge('shapefile', 'datasource')
G.add_edge('layer', 'layerdef')
G.add_edge('layerdef', 'fieldfn')
G.add_edge('feature', 'field')

G.layout(prog='dot')  # default to neato
outpdf = os.path.join(
    os.path.join(
        os.path.dirname(__file__),
        'xx{bname}.pdf'.format(
            bname=os.path.splitext(os.path.basename(__file__))[0][4:]
        )))
print(outpdf)
G.draw(outpdf)

outpng = os.path.join(os.path.join(
    os.path.dirname(__file__),
    'xx{bname}.png'.format(bname=os.path.splitext(os.path.basename(__file__))[0][4:])))
G.draw(outpng)
