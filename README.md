# yolov4_face_mask_detection
基于yolov4实现口罩佩戴检测，在验证集上做到了0.954的mAP。本项目是在 https://github.com/bubbliiiing/yolov4-keras 的基础上进行修改得到。

### 环境要求

​	keras==2.1.6
​	tensorflow-gpu==1.10.0

### 训练

1. 要完成训练步骤需要下载yolo_weights.h5到model_data文件夹下。

   百度云链接: https://pan.baidu.com/s/1FF79PmRc8BzZk8M_ARdMmw 提取码: dc2j

2. 下载AIZOO数据集。数据来源是AIZOO的微信公众号。

   百度云链接: https://pan.baidu.com/s/1nsQf_Py5YyKm87-8HiyJeQ 提取码: eyfz

3. 通过VOCdevkit/split.py将AIZOO数据集的图片和标注分开放到两个文件夹，然后将划分好的数据移动到VOC2007文件夹下。

4. 运行VOCdevkit/VOC2007/voc2yolo4.py生成数据的索引文件。

5. 运行voc_annotation.py生成训练文件（默认为2007_voc.txt）。

6. 运行train.py。单张2080ti耗时约20h。

### 预测

​	要检测图片需要有一个模型权重文件，然后直接运行predict.py，只需要输入图片路径即可实现对图片的检测。
​	要获取模型权重文件有两种方法，一个是跑一遍训练过程，另一个是直接下载我训练好的模型权重。
​	百度云链接：https://pan.baidu.com/s/1QT-TTleIG6E8WmwHP6xnjg 提取码：zd0z

### 效果展示

请见img文件夹下的图片。

### 结果分析

请见result文件夹下的图片。

### 参考资料

[AIZOO公众号](https://mp.weixin.qq.com/s?__biz=MzIyMDY2MTUyNg==&mid=2247483755&idx=1&sn=102c178eeb359617c67aa8cc615a90ce&chksm=97c9d312a0be5a04935c63857e05b1b00a8b5c298d6fa0ffca35e8d026c09169c3ca62e620a2&mpshare=1&scene=1&srcid=&sharer_sharetime=1585995397229&sharer_shareid=cfe18de94f3a847e5ada278bbc490577&exportkey=AQVINroZXgLbi%2BgTqyA1uG8%3D&pass_ticket=mWIVA3QAV6s8RB5LXrZtstiHlu59hNAG7UDhJOnA43G9Pe8xmbQCr%2FksIbtTbVUi#rd)

https://github.com/bubbliiiing/yolov4-keras