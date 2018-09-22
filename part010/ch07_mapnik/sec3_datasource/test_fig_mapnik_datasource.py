'''
'''

import os

from helper.textool import get_tmp_file
# from pygraphviz import Digraph

# from graphviz import Digraph, Graph

import pygraphviz as pgv

G = pgv.AGraph(directed=True, rankdir="LR", size=[8, 5], concentrate=True)
# g = Graph(format='png')
# dot = Digraph()
# dot.format = 'png'
#
#
# dot = Digraph(comment='The Round Table')

cfg = {
    'shape': 'box',
    'fixedsize': True,
    'style': 'rounded,filled',
    'width': 2,
    'fontname': 'Arial',
    'fontsize': 10,
    'concentrate': True,
}
# for node_name in ['python3-shapely', 'python3-mapnik', 'python3-pyproj', 'python3-fiona', 'python3-mpltoolkits.basemap',
#                   'python3-gdal']:
#     G.add_node(node_name, fillcolor="#a0ffa0", **cfg)
#
# cfg['style'] = 'filled'
# for node_name in ['spatialite-bin', 'mapnik-utils', 'proj-bin', 'gdal-bin']:
#     G.add_node(node_name, fillcolor="#ffa0a0", **cfg)
#
# for node_name in ['libgdal20', 'libproj12', 'libgeos-c1v5', 'libspatialite7', 'libmapnik3.0']:
#     G.add_node(node_name, fillcolor="#eeeeee", **cfg)

G.add_edge('Mapnik', 'datasource')
G.add_edge('datasource', 'Geospatial Data/Database')

G.layout(prog='dot')  # default to neato
G.draw(get_tmp_file(__file__, '1', file_ext='pdf'))
G.draw(get_tmp_file(__file__, '1', file_ext='png'))
