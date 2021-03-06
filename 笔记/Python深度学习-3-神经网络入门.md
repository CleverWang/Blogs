# 3.神经网络入门

## 3.1神经网络剖析

- 层，多个层组合成网络（或模型）
- 输入数据和相应的目标
- 损失函数，即用于学习的反馈信号
- 优化器，决定学习过程如何进行

![图1-9.png](https://upload-images.jianshu.io/upload_images/6411513-75efc6cef0f125d3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 3.1.1层：深度学习的基础组件

1. 层是一个数据处理模块，将一个或多个输入张量转换为一个或多个输出张量。有些层是无状态的，但大多数的层是有状态的，即层的权重
2. 简单的向量数据保存在形状为 (samples, features) 的 2D 张量中，通常用**密集连接层**［densely connected layer，也叫**全连接层（fully connected layer）**或**密集层**（dense layer），对应于 Keras 的 Dense 类］来处理
3. 序列数据保存在形状为 (samples, timesteps, features) 的 3D 张量中，通常用**循环层**（recurrent layer，比如 Keras 的 LSTM 层）来处理
4. 图像数据保存在 4D 张量中，通常用**二维卷积层**（Keras 的 Conv2D）来处理
5. 构建深度学习模型就是将相互兼容的多个层拼接在一起，以建立有用的数据变换流程。这里**层兼容性**（layer compatibility）具体指的是每一层只接受特定形状的输入张量，并返回特定形状的输出张量

### 3.1.2模型：层构成的网络

1. 深度学习模型是层构成的有向无环图
2. 一些常见的网络拓扑结构：
   - 双分支（two-branch）网络
   - 多头（multihead）网络
   - Inception 模块
3. 网络的拓扑结构定义了一个**假设空间（hypothesis space）**。选定了网络拓扑结构，意味着将可能性空间（假设空间）限定为一系列特定的张量运算，将输入数据映射为输出数据。然后，需要为这些张量运算的权重张量找到一组合适的值

### 3.1.3损失函数与优化器：配置学习过程的关键

1. **损失函数（目标函数）**—在训练过程中需要将其最小化。它能够衡量当前任务是否已成功完成
2. **优化器**—决定如何基于损失函数对网络进行更新。它执行的是随机梯度下降（SGD）的某个变体
3. 具有多个输出的神经网络可能具有多个损失函数（每个输出对应一个损失函数）。但是，梯度下降过程必须基于**单个标量损失值**。因此，对于具有多个损失函数的网络，需要将所有损失函数取平均，变为一个标量值
4. 一些简单的指导原则来选择正确的损失函数 ：
   - 二分类问题 -> 二元交叉熵（binary crossentropy）
   - 多分类问题 -> 分类交叉熵（categorical crossentropy）
   - 回归问题 -> 均方误差（mean-squared error）
   - 序列学习问题 -> 联结主义时序分类（CTC， connectionist temporal classification）

## 3.2二分类问题

- 通常需要对原始数据进行大量预处理，以便将其转换为张量输入到神经网络中。单词序列可以编码为二进制向量，但也有其他编码方式
- 带有 relu 激活的 Dense 层堆叠，可以解决很多种问题（包括情感分类），你可能会经常用到这种模型
- 对于二分类问题（两个输出类别），网络的最后一层应该是只有一个单元并使用sigmoid激活的 Dense 层，网络输出应该是 0~1 范围内的标量，表示概率值
- 对于二分类问题的 sigmoid 标量输出，你应该使用 binary_crossentropy 损失函数。无论你的问题是什么， rmsprop 优化器通常都是足够好的选择。这一点你无须担心
- 随着神经网络在训练数据上的表现越来越好，模型最终会过拟合，并在前所未见的数据上得到越来越差的结果。一定要一直监控模型在训练集之外的数据上的性能

## 3.3多分类问题

- 如果要对 N 个类别的数据点进行分类，网络的最后一层应该是大小为 N 的 Dense 层
- 对于单标签、多分类问题，网络的最后一层应该使用 softmax 激活，这样可以输出在 N个输出类别上的概率分布
- 这种问题的损失函数几乎总是应该使用分类交叉熵。它将网络输出的概率分布与目标的真实分布之间的距离最小化
- 处理多分类问题的标签有两种方法
  - 通过分类编码（也叫 one-hot 编码）对标签进行编码，然后使用 categorical_crossentropy 作为损失函数
  - 将标签编码为整数，然后使用 sparse_categorical_crossentropy 损失函数
- 如果你需要将数据划分到许多类别中，应该避免使用太小的中间层，以免在网络中造成
  信息瓶颈

## 3.4回归问题

- 回归问题使用的损失函数与分类问题不同。回归常用的损失函数是均方误差（MSE）
- 同样，回归问题使用的评估指标也与分类问题不同。显而易见，精度的概念不适用于回归问题。常见的回归指标是平均绝对误差（MAE）
- 如果输入数据的特征具有不同的取值范围，应该先进行预处理，对每个特征单独进行缩放
- 如果可用的数据很少，使用 K 折验证可以可靠地评估模型
- 如果可用的训练数据很少，最好使用隐藏层较少（通常只有一到两个）的小型网络，以避免严重的过拟合。

## 本章小结

- 在将原始数据输入神经网络之前，通常需要对其进行预处理
- 如果数据特征具有不同的取值范围，那么需要进行预处理，将每个特征单独缩放
- 随着训练的进行，神经网络最终会过拟合，并在前所未见的数据上得到更差的结果
- 如果训练数据不是很多，应该使用只有一两个隐藏层的小型网络，以避免严重的过拟合
- 如果数据被分为多个类别，那么中间层过小可能会导致信息瓶颈
- 回归问题使用的损失函数和评估指标都与分类问题不同
- 如果要处理的数据很少， K 折验证有助于可靠地评估模型
