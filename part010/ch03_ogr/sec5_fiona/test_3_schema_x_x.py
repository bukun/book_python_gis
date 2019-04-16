#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from pprint import pprint
import fiona
c = fiona.open('/gdata/GSHHS_c.shp')
pprint(c.schema)
###############################################################################
rec = next(c)
set(rec.keys()) - set(c.schema.keys())
set(rec['properties'].keys()) == set(
    c.schema['properties'].keys())
###############################################################################
type(rec['properties']['source'])
c.schema['properties']['source']
###############################################################################
from fiona import prop_width
prop_width('str:25')
prop_width('str')
###############################################################################
from fiona import prop_type
prop_type('int')
prop_type('float')
prop_type('str:25')
###############################################################################
c = fiona.open('/gdata/GSHHS_c.shp')
rec = c.next()
pprint(rec)
###############################################################################
c.close()
rec['id']
###############################################################################
c = fiona.open('/gdata/GSHHS_c.shp')
rec = next(c)
rec['id']
###############################################################################
pprint(rec['properties'])
###############################################################################
pprint(rec['geometry'])
