'''
我现在要讲图片在pygame窗口中按照中心旋转的知识。这是我的授课思路：
问题: 引入：生活中我投篮球时，篮球在空中都是一边移动一边旋转。而我们程序中的水果在空中只移动没有旋转，看着很不自然呀？
解决：为水果炸弹图片增加旋转效果
问题：因为每个水果和炸弹旋转是都有自己旋转的角度，所以需要在父类中定义angle属性，并在draw方法中每次旋转增加5度

解决：想要实现水果和炸弹旋转运动，需要使用图片旋转方法：pygame.transform.rotate，这个方法需要两个参数，第一个参数是图片，self.img,
第二个参数是旋转的角度，但是发现图片没有旋转

问题：使用rotate()方法旋转后，绘制原图片，图片不旋转
解决：pygame.transform.rotate会返回旋转后的图片，不改变原来的，图片，所以要使用img变量接收旋转后的新图片，并绘制新图片，不过发现图片选中过程中有抖动
原因 ： 旋转后的图片是倾斜的，pygame无法直接绘制，它会自动用一个更多的正矩形包裹图片。当图片旋转后依然按左上角绘制，会导致图片中心点偏移，就会出现抖动。
解决 ： 之后需要旋转图片，都按照中心点坐标绘制
问题 ： 现在绘制和移动，都是用左上角坐标
解决 ： 根据传入的左上角坐标，求中心点坐标，步骤是1：使用get_size方法获取图片宽和高，2：求中心点坐标，3：删除x和y坐标。
4.需要把move方法中的xy坐标改为中心点坐标
问题 ： 但是现在screen.blit方法如何按中心点绘制图片？
解决 ： 讲解使用get_rect方法，获取旋转后新图片的矩形区域，在这个矩形内绘制旋转后图片

这是我的代码：
class FlyObject:
  def _ _init_ _(self, img, x, y):
    w,h = self.img.get_size()
    self.centerX = x+w/2
    self.centerY = y + h/2
    ...
    # 1. 定义angle属性
    self.angle = 0

  def draw(self):
    # 2. 实现图像每次旋转5度
    self.angle += 5
    self.newImg=pygame.transform.rotate(self.img, self.angle)
    # 3. 把self.img修改为img
    screen.blit(self.newImg, (self.x, self.y))

def draw(self):
        self.angle += 5
        self.newImg = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.newImg.get_rect(center=(self.centerX,self.centerY))
        canvas.blit(img,self.rect)
def move(self):
        self.centerY -= self.speedY
        self.speedY -= 2
        self.centerX += self.speedX

请帮我使用中文，根据以上知识点出5道单选题，帮助学生理解图片在pygame窗口旋转的步骤，图片旋转的主要函数使用，不需要答案.
'''
