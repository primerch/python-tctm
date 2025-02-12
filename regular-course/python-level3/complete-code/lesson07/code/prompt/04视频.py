"""
第一段提示词：

```
def drawText(text, pos):
    font = pygame.font.Font('fonts/WRYH.ttf', 40)
    textImg = font.render(str(text), True, 'orange')
    screen.blit(textImg, pos)
```
上面是我定义在pygame界面上绘制文字的函数，但是面向对象编程规定，
类外定义的函数也应该定义在类中成为方法，我已经学了类方法和对象方法，该定义成什么方法呢？

"""

"""
第二段提示词：

我发现drawText方法既不需要访问类变量，也不需要访问对象属性，那该把它定义成什么方法呢？

"""
