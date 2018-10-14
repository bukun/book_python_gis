#!/usr/bin/env bash

pdftk build/py3gis.pdf cat 227-275 output build/py3gis_cnt.pdf

# Basemap
# pdftk build/py3gis.pdf cat 337-389 output build/py3gis_cnt.pdf

