Source codes for book ``Python in open source GIS``
===========================================================

Author: [Bu Kun](http://www.osgeo.cn)

The reposity hosts the source codes for my book ``Python in open source GIS`` (In Chinese language).
The book is being translated into English, which could be found at https://www.gislite.com/catalog/opensource-python-gis .

Installation and Setup
-----------------------------------------
The source code is written and tested under Debian Jessie.
The following tools for libs should be installed first.

::

   aptitude install python3-gdal
   aptitude install python3-shapely
   aptitude install python3-nose

Build database:

::

    ogr2ogr -f SQLite -dsco SPATIALITE=YES xx_china.db /gdata/stats_county.shp -nlt polygon

中文说明
---------------------------------
 
本代码为《Python与开源GIS》一书的脚本。
书中的大部分内容，发布在网站： [http://www.osgeo.cn/pygis/](http://www.osgeo.cn/pygis/) 。

代码是作为学习使用，提供了作为测试。在学习的时候，最好还是仔细键入运行来查看效果。
因为代码中用到了一些数据，
所以需要先行切换到数据目录下使用，免得找不到数据。


使用单元测试 nose
^^^^^^^^^^^^^^^^^^^^^^^^^

首先获取 `helper`

    git clone https://github.com/bukun/tex_helper.git helper

单元测试，使用下面命令：

    nosetests3 -v -d --exe part010

或者使用（会打印出来信息）：

    nosetests3 -v -d -s --exe part010

注意
^^^^^^^^^^^^^^^^^^^^^^^^^

为了使 nosetests 能够对代码进行测试运行，文件需要按下面的要求进行组织：

* 所有的文件夹下面，都得有 `__init__.py` 文件，以使 nosetests 能够正确的遍历到文件夹下。
* 所有的文件，都以`test`开头进行命名。
* 文件的命名，不得含有中文字符、减号、空格、英文句号，及其他奇怪字符；需要进行分隔，可使用下划线`_`。

Updating notes
^^^^^^^^^^^^^^^^^^^^^^^^^

* 20190416: 第二次校稿更新4
* 20181014: 第二次校稿更新3
* 20181008: 第二次校稿更新2
* 20180922: 第二次校稿更新1
* 20171222: Clean the codes.
* 20170808: The Latex files were merged into the codes.
