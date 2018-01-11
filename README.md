00000000---
title: 2018111_Caltech行人数据集转换成VOC格式脚本 
grammar_cjkRuby: true
---

### 下载Caltech 格式数据集
数据集地址：http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/datasets/USA/

> Caltech 行人检测数据集，时长10小时， 分辨率为640×480的30Hz视频。包含约250,000帧（137个长片段），350,000个标定框，2300个独立行人。
> set00~set05 是训练集，set06~set10是测试集。annotation是包含set00~set100的标注文件。

下载后将文件放在相应的文件夹里，主要是seq和annotations。

### 下载转换脚本

``` haskell
|-- caltech-database
    |-- data
	    |-- seq                下载好解压后的 .seq 文件，set00~set05
	    |-- annotations        标注文件 .vbb  ，set00~set05
	    |-- img_file           存储处理好的jpg图像，可以没有，自动生成
	    |-- xml_file           存储处理好的xml文件，可以没有，自动生成
    |-- scripts                转换用的脚本文件
	    |-- seq2jpgs.py
	    |-- vbb2voc.py
	    |-- convert_caltech.py 运行这个可以同时生成jpg和xml文件。
```

		
### 使用脚本
在 caltech-database目录下执行convert_caltech.py文件


>lalala@ubuntu : ~/caltech-database$python ./scripts/convert_caltech.py

然后在上述的 img_file 文件夹和 xml_file 文件夹里就可以看到相应的文件了

### 如需要更改
在convert_caltech.py 文件中可以修改文件输入和输出的路径。
seq2jgp.py 文件包含.seq 文件转化jpg 文件的代码，vbb2voc.py 文件中包含.vbb文件转化为.xml 文件的代码。


























