# 说明

Author: [Bu Kun](http://www.osgeo.cn)

本代码为《Python与开源GIS》一书的脚本。

代码是作为学习使用，大概复制、粘贴了来用最好。因为代码中用到了一些数据，
所以先行切换到数据目录下使用，免得找不到数据。

## 安装与配置

代码的编写与测试都是在 Debian Jessie下面。需要安装下面的工具：

    aptitude install python3-gdal
    aptitude install python3-shapely
    aptitude install python3-nose


## 使用单元测试 nose


    nosetests3  --exe -v -d

或者使用（会打印出来信息）： 

    nosetests3  --exe -v -d -s

## 注意
为了使 nosetests 能够对代码进行测试运行，文件需要按下面的要求进行组织：

* 所有的文件夹下面，都得有 `__init__.py` 文件，以使 nosetests 能够正确的遍历到文件夹下。
* 所有的文件，都以`test`开头进行命名。
* 文件的命名，不得含有中文字符、减号、空格、英文句号，及其他奇怪字符；需要进行分隔，可使用下划线`_`。
