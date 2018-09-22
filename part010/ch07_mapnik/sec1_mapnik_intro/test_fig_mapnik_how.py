# -*- coding: utf-8 -*-
'''
注意，使用的是：  `pygraphviz` ， 另外，还有  `graphviz`
'''

'''
Raw codes in Rest.
.. graphviz::

   digraph G{
      Symbol -> Rule [label = "r.symbols.append()", style="dash"];
      Rule -> Style [label = "s.rules.append()", style="dash"];
      Style -> Map [label = "m.append_style()", style="dash"]
      Map -> NamedStyle ;
      NamedStyle -> Layer [label = "lyr.styles.append()" ] ;
      Layer -> Map [label = "m.layers.append()" ];
      Map -> Output [label = "render()" ];
   }

Version, with Mapnik
.. digraph G{
      Symbol -> Rule [label = "s.rules.append()", style="dash"];
      Rule -> Style [label = "r.styles.append()", style="dash"];
      Style -> NamedStyle;
      Map -> NamedStyle ;
      NamedStyle -> Layer -> Map ;
      Map -> Output [label = "render()" ];
      Mapnik -> Map ;
      Mapnik -> Layer;
      Mapnik -> Style ;
      Mapnik -> Rule ;
      Mapnik -> Symbol ;
   }
'''

import os
# from pygraphviz import Digraph

# from graphviz import Digraph, Graph
from helper.textool import get_tmp_file
import pygraphviz as pgv

G = pgv.AGraph(directed=True)
# g = Graph(format='png')
# dot = Digraph()
# dot.format = 'png'
#
#
# dot = Digraph(comment='The Round Table')

G.add_edge('Symbol', 'Rule', label=" r.symbols.append()", style="dash")
G.add_edge('Rule', 'Style', label=" s.rules.append()", style="dash")
G.add_edge('Style', 'Map', label=" m.append_style()", style="dash")
G.add_edge('Map', 'NamedStyle')
G.add_edge('NamedStyle', 'Layer', label=" lyr.styles.append()")
G.add_edge('Layer', 'Map', label=" m.layers.append()")
G.add_edge('Map', 'Output', label=" render()")

G.layout(prog='dot')  # default to neato
outpng = get_tmp_file(__file__)
G.draw(outpng)

outpdf = get_tmp_file(__file__, file_ext='pdf')
G.draw(outpdf)
