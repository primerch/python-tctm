"""
第一段提示词：

我已经在Knife类中定义了collide方法实现了精准碰撞检测，
并且在FlyObject类中定义了bang方法用来实现碰撞后的功能，如切换图片。
现在有一个问题，如何加载并播放music文件夹下Bomb.mp3和Fruit.mp3声音呢？


第二段提示词：

由于Fruit类和Bomb类都有声音属性，所以需要在FlyObject中定义统一的music属性，
但是如何在父类中根据不同的类判断，如果是水果对象就赋值为Fruit.mp3，炸弹对象就赋值为Bomb.mp3呢？

"""
