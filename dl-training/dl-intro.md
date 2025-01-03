---
@import "newrizon.less"

id: "newrizon-id"
# class: "my-class1 my-class2"
title: "veos system assessment"
author: 
- Binjian Xin 
date: "Sep. 16, 2021"

presentation:
  enableSpeakerNotes: true
  # width: 800px
  # height: 450px
  width: 1600
  height: 900
  shoNotes: true
  output: 
    beamer_presetnation:
      path: ./Exports/veos system assessment.pdf
      toc: true
toc:
  depth_from: 1
  depth_to: 1
  ordered: false
---


<!-- slide data-background-image="./Horizontal-Sea.jpg" -->

<img src="./newrizon.logo.png" alt="drawing" width="200"/>
<span style="color:#004394; font-size:40pt;">深度学习极简介绍</span>
<span style="color:#004394; font-size:30pt;">A Whirlwind Tour</span>
---
[<span style="color:#004394; font-size:25pt;"> &nbsp; &emsp; 忻斌健</span>](#VEOS系统评估)
<span style="color:#004394; font-size:25pt;"> 2021年09月29日 </span>



<!-- #+title: dl intro -->

<!-- slide id="newrizon-id" -->
[TOC]

<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->

@import "newrizon.less"

- 不介绍
  - 编程
  - 设计
- 介绍
  - 思想
  - 应用

<!-- slide id="newrizon-id"　style="text-align: center;" class="my-class1 my-class2" -->

<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="fig/dotcat.png">
    <source src="fig/dotcat.mp4" type="video/mp4">
  </video>
</figure>

<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->

- 如何识别,分类?
- 图像 --> 识别目标?
- 哪些特征帮助识别目标?
- 目标的姿态是怎样?
- 需要多少特征能确定识别的结论?
- 图像产生了那些动态印象?
- 识别的过程有多久?

<!-- - 经验知识 
- 机器学习与人类学习
- 模型 -->

<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->
[手势识别与跟踪](https://loicmagne.github.io/air-drawing/)
<!-- slide id="newrizon-id"　style="text-align: right;" class="my-class1 my-class2" -->
> **Gradient descent can write code better than you. 
> I'm sorry**
>                                             -- Andrej  Karpathy


<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->
# 深度学习

## 目标识别

imagenet 2009: 
- 22000个类
- 1400万样本 

alexnet 2012: 
- subset: 1000个类, 120万训练样本, 5万验证样本, 15万测试样本
- 5个卷积层,3个全连接层
- [参数个数6200万](https://learnopencv.com/number-of-parameters-and-tensor-sizes-in-convolutional-neural-network/)

[AlexNet](https://en.wikipedia.org/wiki/AlexNet)
[LeNet 可视化](https://www.cs.ryerson.ca/~aharley/vis/conv/)

<!-- slide id="newrizon-id"　style="text-align: center;" class="my-class1 my-class2" -->
卷积网动物园


|![](fig/lenet_data2.png)|
|:--:|
|<b>LeNet 1989</b>|

<!-- slide id="newrizon-id"　style="text-align: center;" class="my-class1 my-class2" -->

|![](fig/alexnet_data.png)|
|:--:|
|<b>AlexNet 2012</b>|

<!-- slide id="newrizon-id"　style="text-align: center;" class="my-class1 my-class2" -->
|![](fig/resnet.png)|
|:--:|
|<b>ResNet</b>|
<!-- slide id="newrizon-id"　style="text-align: center;" class="my-class1 my-class2" -->

|![](fig/u-net.png)|
|:--:|
|<b>U-Net</b>|
<!-- slide id="newrizon-id"　style="text-align: right;" class="my-class1 my-class2" -->

> If you have **a large big dataset大数据** and you train **a very big neural network深度学习**, then success is guaranteed!  
> --Ilya Sutskever*


<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->
## 方法理解

- 数据不是像素! 整幅图像看成一个集合中的一个对象
- 巨大的参数空间和高维度:
  - ImageNet样本 向量$224\cdot 224\cdot 3=15028$个整数  
  - Imagenet潜在样本数量($((224\cdot224)^{256^3}$ $\gg$ 宇宙中的原子数量$10^{82}$
**自然图像是非常非常稀疏的!!!**
  - 高维度中的低维度集合(聚类)
  - 提取/利用低维度特征

- 机器学习中的误差来源
  - 数据不够多 (统计误差)
  - 模型不够大 (近似误差)
  - 求解不够准 (优化误差)
  - 模型太大 (过拟合)

<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->

- 归纳偏置Inductive Bias:
  - 局部特性(图像):
    - 平移不变
    - 多尺度不变
  - 自然界compositionality of the nature
  - 对称性,不变性
  - 另一个例子:激光雷达数据处理

<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->

需要知识:

 - 线性代数
   - 矩阵基本运算
   - 矩阵梯度
 - 微积分
   - 微分,梯度
 - 概率论
   - 熵
   - KL散度
   - 群论

<!-- slide id="newrizon-id"　style="text-align: right;" class="my-class1 my-class2" -->
> **Deep Learning  is  a science of sloppiness.**
> --Yann Lecun

<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->
# 应用 

## 计算机视觉

分类, 分割, 追踪
|![](fig/detectron2.png)|
|:--:|
|<b>Facebook AI Detectron2 </b>|

<!-- slide id="newrizon-id"　style="text-align: center;" class="my-class1 my-class2" -->

3D信息推理

|![](fig/mesh-rcnn.gif)|
|:--:|
|<b>Mesh R-CNN</b>|



<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->
##  自然语言处理

单词向量化 - 单词内嵌(Word Embedding)


|![](fig/embedding.png)|
|:--:|
|<b>对象映射到向量 </b>|

<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->

|<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="fig/seq_model.png">
    <source src="fig/sequence-modeling.mp4" type="video/mp4">
  </video>
</figure>|
|:--:|
|<b>序列模型 (Sequence Modeling)</b>|

[Jay Alammar](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)

- RNN &rarr; LSTM &rarr; Transformer
- Transformer (注意力机制) 变形金刚模型
- GPT &rarr; Codex
- AGI争议

<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->
图像处理中变形金刚模型
|![](fig/Detection-transformer.png)|
|:--:|
|<b>Facebook AI DETR</b>|

<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->
## 生成模型

|![](fig/vae.png)|
|:--:|
|<b>VAE 2014</b>|

<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->

|![](fig/vae-examples.png)|
|:--:|
|<b>VAE Results 2014</b>|

<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->

|![](fig/gan.png)|
|:--:|
|<b>GAN 2014</b>|
<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->

|![](fig/stylegan-woman.jpg)|
|:--:|
|<b>StyleGAN 2018</b>|
<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->
|![](fig/deepfake-detect.png)|
|:--:|
|<b>检测StyleGAN-V2 </b>|
<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->
## 图神经网络

|![](fig/pagerank.png)|
|:--:|
|<b>PageRank</b>|

<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->
PageRank
- 网页链接 &rarr; 有向图
- 排序按相互引用的次数确定重要性
- 整个互联网模型: 随机邻近矩阵(Stochastic Adjacent Matrix) $M$
  - 稳态分布: $1 \cdot r=M\cdot r$ &rarr; flow equation
- 用随机游走(random walk)采样,避免求解一个大矩阵的奇异值
- 2019年过期

<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->
|![](fig/discovering_symbolic_eqn_gn.png)|
|:--:|
|<b>[发现物理定律](https://github.com/MilesCranmer/symbolic_deep_learning)</b>| 哦
- Google地图 预计到达时间(ETA)估计
- AlphaFold

<!-- slide id="newrizon-id"　style="text-align: center;" class="my-class1 my-class2" -->
NeRF
[<img src="fig/nerf.png" alt="drawing" width="600"/>](fig/nerf.mp4)

<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->
## 图像编码和语言模型的结合
CLIP, DALL-E 
[DALL-E](https://openai.com/blog/dall-e/)

clip
https://clip.backprop.co/
https://www.clipplayground.co/


<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->
## 强化学习
- 通过与环境交互学习最优策略（基于大数据）
- 积累经验（缓存在状态/行动价值函数中）
- 可以是无模型或动态建模
- 可以是在线算法
- 动态调整策略

<img src="fig/drl-dl.jpg" alt="drawing" width="300"/>

<!-- slide id="newrizon-id"　style="text-align: center;" class="my-class1 my-class2" -->
AlphaGo
[<img src="fig/alphago1.jpg" alt="drawing" width="600"/>](fig/alphago.mp4)

<!-- slide id="newrizon-id"　style="text-align: center;" class="my-class1 my-class2" -->
OpenAI魔方(OpenAI 5 DOTA2)
[<img src="fig/openai.png" alt="drawing" width="600"/>](fig/openai.mp4)

<!-- slide id="newrizon-id"　style="text-align: left;" class="my-class1 my-class2" -->
# 总结与展望

总结:
  - 学习为基本机制
  - 大数据驱动
  - 数据分布为对象(大数据)
  - 实践驱动


展望
  - 自监督学习LeCake
  - 几何深度学习(图神经网络)
  - 通用强化学习(通用任务)
  - 终身学习(lifelong learning)
  - 灾难性遗忘 Catastrophic forgetting