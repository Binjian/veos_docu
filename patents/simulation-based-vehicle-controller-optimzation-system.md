---
title: 发明和实用新型技术交底书-软硬结合案 
author: 忻斌健
mainfont: Noto Sans Mono CJK SC
CJKoptions: BoldFont=STHeiti, ItalicFont=STKaiti, PunctStyle=kaiming, XeTexlinebreaklocale "zh" 
---

# 基于仿真的车辆控制参数优化系统
## 背景技术

### 技术领域,背景以及相关技术发展

在工业领域和汽车电子领域对控制器自适应调节能力和适应复杂多变工况要求日益增长, 仿真技术的发展对于控制器的正向开发变得十分重要,仿真工具有利于便捷地提供测试控制器所需的各种工况,快速验证相关控制参数和控制器系统结构的调整,帮助设计完备的测试用例,动态有针对性调整环境参数,并为实现快速并行化测试提供了技术基础.

另外常规的控制器设计往往只考虑单一的控制指标,仿真工具通常用于单一控制指标的评估.高性能仿真工具有助于设计和验证复杂多目标系统,通过不同时间尺度和独立的内外环控制验证独立于现有设计指标的其他控制器指标,比如能耗,舒适性等,是实现复杂工况自适应调节的基础.

控制器设计对生成复杂工况的要求就需要仿真环境能便捷地改变环境参数,车辆参数和控制器参数,产生测试需要的大量随机工况数据.

### 发明最接近的现有技术
应用软件Prescan,Carsim, Carmaker等,主要用于车辆动态控制性能的仿真.

## 现有技术的问题
1. 局限于车辆运动控制和动态性能的仿真,对车辆控制器对不同工况的适应性评估没有系统的评价. 这里“不同工况”的意思包含控制器本身的控制参数设置，环境差异（比如天气，测试道路几何属性），不同的车辆负载情况（空载，满载，半载等）
2.	能生成确定的和已设计的工况,环境和车辆参数,无法系统性产生大量随机参数,模拟车辆在真实世界中的随机工况. 没有利用仿真系统的参数设置接口，不能结合参数随机采样实验和自动化测试脚本，产生大量随机控制参数和随机环境工况。
3.	只能用于系统验证和测试,不适应基于大数据和机器学习的算法开发

## 技术方案的发明概述

本专利技术方案提供了工业控制器,特别是车辆控制器通过仿真进行开发设计和验证以及多目标控制器设计开发验证的方法和环境.它提供了如下的功能 
1. 辅助车辆控制器设计中重要参数的开发和验证 
2. 在仿真环境中可以灵活调整工况，路况，比如可设计道路，车辆负载，变更天气，路面阻尼，交通拥堵情况等等,可产生大量随机工况,适应控制器设计开发需要的大数据需求 
3. 参数优化模块是独立与常规控制模块上层控制模块，可将和工况相关优化考虑到控制器的实时调整策略中 
4. 具备完整的基准数据，可以获取准确的反馈数据和环境数据以及车辆数据，为精准评估控制和优化策略提供依据。这里“基准数据”泛指车辆的准确状态（车速，位置等），道路的准确属性（曲率，长度等），克服了道路测试中的测量误差和处理误差带来的不确定性。基准数据可用于完全精确评估算法的性能及其变化。
5. 模块化设计的平台具备灵活的可扩展性，便于添加环境感知数据，车辆横纵向控制系统，驱动系统，底盘系统等模型，可通过灵活的通信接口迅速集成相关子系统
6. 精确评估车辆控制器对不同工况的适应性评估，可分为如下步骤：
   i. 随机采样控制器参数空间， 天气参数空间（如光照，降水量），道路参数空间（如曲率，路阻）
   ii. 编写脚本利用通过仿真系统接口把随机采样得到的参数设置到仿真环境里
   iii. 对每一种参数配置启动仿真实验
   iv. 通过仿真系统接口记录车辆和环境的真实状态以及控制器的观测数据和控制状态，并且比较控制偏差和评估控制性能
   v. 返回i)进行下一次实验







## 技术方案的详细阐述

```plantuml
caption 图1

repeat :操作者;
:人机交互;
repeat :控制器;
:仿真环境;
backward: 参数优化模块;
```

上图为基于仿真与车辆控制器参数优化系统的流程。操作者通过人机接口,比如方向盘,加速踏板和刹车踏板与仿真系统连接,将方向盘转角,加速和刹车踏板开度等机械信号转换成电信号,仿真系统的设备驱动将上述电信号转化成软件输入信号.控制器接受到控制信号和仿真环境产生道路和车辆状态,按既定的控制参数和运动控制策略产生仿真系统中车辆的控制信号.仿真系统接受到控制器的控制信号后,通过道路,车辆动力学模型,道路参与者的控制规律和它们各自的动力学模型计算仿真系统的变化,影响反馈给控制器的观测量,实现控制器闭环控制.同时操作者感受到的仿真系统视觉上和力反馈等方面的变化,实时调整方向盘,加速和刹车踏板的开度,这样系统模拟了仿真环境下人对车辆的操控. 本系统的第二个环路主要有参数优化模块构成,这个模块会从仿真环境中从独立的角度获得足够的观测量,就独立于现有控制器性能指标(比如运动控制精度等)的其他性能指标,比如能耗,舒适性等进行评估,通过这些观测量独立进行决策,对这些指标进行优化.这样的系统主要由四方面的特点构成:

1. 仿真环境的可调节参数包括
   - 道路静态几何参数,如曲率,高程,拓扑性质
   - 道路阻抗
   - 天气和光照条件
   - 道路参与者比如目标车辆,行人的数量,它们的随机运动轨迹,可视化特征如亮度,颜色,表面反射率,
   - 控制器参数,如运动规划控制器,动力系统和底盘系统控制器的PID控制参数


2. 系统由两个环路组成, 一个是常规车辆控制环路,另一个是控制器参数优化环路.常规车辆控制环路由操作者发起对车辆控制的指令，经人机交互平台输出至车辆动态控制器，控制器接收人机接口的信号导入仿真环境对车辆进行控制,操作者通过仿真系统人机接口比如反馈和仿真视频得到车辆控制的反馈并自行调整自己对车辆的动态操控。这个常规的控制环路保持了原来仿真环境下的控制器测试验证接口,同时开放了新的接口给参数优化模块进行独立的控制器调整策略.系统由两个环路组成, 一个是常规车辆控制环路,另一个是控制器参数优化环路.常规车辆控制环路由操作者控制油门踏板，方向盘和刹车踏板，经仿真平台的人机交互接口输出至车辆动态控制算法模块，车辆动态控制算法模块集成在仿真平台上，控制算法模块通过仿真平台人机接口接收到输入信号，通过算法得到车辆控制信号，输出到仿真环境的道路模型和车辆动态模型， 仿真平台综合这些信号计算出下一个完整的系统状态。,仿真系统有完整的道路模型，环境模型，传感器模型和车辆动力学模型，可以产生任意的观测数据，比如司机视角的道路视频等。这样操作者通过仿真系统人机接口比如力反馈和司机视角的道路仿真视频得到车辆控制的反馈并自行调整自己对车辆的动态操控。这个常规的控制环路保持了原来仿真环境下的控制器测试验证接口,同时开放了新的接口给参数优化模块进行独立的控制器调整策略.
   
3. 控制器参数优化模块独立于常规控制模块,通过仿真环境基于车辆控制效果反馈按照独立于常规控制器控制指标的参数进行二级目标的控制评估,可参考的二级目标包括舒适性,节能和环保等。具体操作方法如下 
    - 按照常规控制器设计目标比如车辆的横向或纵向控制精度进行控制器参数设计，得到一组符合设计目标的参数，对应于满足要求的一组控制方案
    - 将这组控制方案中的每一个方案集成到仿真平台的车辆动态控制算法模块，按设定的一个或一组场景进行测试并收集基准数据和实时控制数据。
    - 按二级目标定义的指标从收集的测试数据中计算相应的参数
    - 同工况下比较这组控制方案在二级目标下的优劣，确定二级目标下的最优方案。 
   
4. 控制器参数优化模块可按照独立的时间周期和二级目标策略对现存控制器参数进行评估,经过并行的优化策略参数对控制器参数进行动态实时更新,并导入控制器，由于参数优化模块和常规控制器算法的观测量不同，算法独立，可以将参数优化的部分形成一个独立的模块，见图1中的参数优化模块。这个参数优化反馈环路通过从结构上将相互独立的控制指标分配给不同的调节模块,可以评估和支持设计控制器参数的动态工况调整策略,同时借助于仿真环境的大数据生成能力,使此仿真系统具备了超越传统控制器测试和验证的功能，不仅在单一的控制指标上进行评估和测试，还可以就多目标进行协同的验证和设计
   
5. 各主要软件模块之间通过通用快速的以太网接口连接,软件接口可以为基于TCP或UDP的套接字接口,可保证整个系统的可靠通信和分布式标准化接口,便于灵活的系统模块切换

## 上述技术方案产生了什么技术效果

 - 基于仿真环境的控制器测试验证环境
 - 在现有控制器开发设计上可叠加其他独立设计指标,以实现控制器参数针对复杂和动态工况的自适应调节
 - 可灵活调整环境,车辆和控制器参数的调节,具备开发控制器所需的大数据生成能力
 - 可通过模块化分布式的通信接口进行模块的集成,更新和升级

## 上述技术方案中可以替代的地方

各模块本身,比如控制器,人机交互,仿真环境以及参数优化模块,分布式模块接口都可以用等同功能的模块替代.

## 术语解释

## 参考文献