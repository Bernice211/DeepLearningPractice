图像风格迁移

原理：
为了将风格图的风格和内容图的内容进行融合，所生成的图片，在内容上应当尽可能接近内容图，在风格上应当尽可能接近风格图
因此需要定义内容损失函数和风格损失函数，经过加权后作为总的算是函数

实现步骤如下：
1、随机产生一张图片
2、在每轮迭代中，根据总的损失函数，调整图片的像素值
3、经过多轮迭代，得到优化后的图片

内容损失函数
两张图片在内容上相似，不能仅仅靠简单的纯像素比较
CNN具有抽象和理解图像的能力，因此可以考虑将各个卷积层的输出作为图像的内容
