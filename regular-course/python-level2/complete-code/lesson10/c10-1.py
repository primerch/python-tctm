import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.mouse.set_visible(0)

# 图片名称列表
names = ['bg0', 'door', 'bg1', 'layer', 'pwd_error', 'm0', 'm1']
# 图片存储列表
plist = []

# 定义变量存储破解谜题
t1 = '没想到还有人可以寻到这里...第一组关键字：'
t2 = '只有童程学院掌握破解的方法...接下来是第二组：'
t3 = '此秘宝于我族世代传承，只为等候有缘人开启...第三组:'
t4 = '答应我，请好好爱护这个世界...第四组：'
texts = [t1, t2, t3, t4]
# 定义变量存储秘宝话语
w1 = '亲爱的孩子们：'
w2 = ' 其实，所谓的秘宝，指的就是一颗善待'
w3 = '环境的心。'
w4 = ' 趁着环境还没有完全恶化，垃圾分类、'
w5 = '绿色出行、植树造林、杜绝浪费等一系列'
w6 = '行为迫在眉睫，快行动起来吧。'
w7 = ' 秘宝就在每个人的心中，具体如何使用，'
w8 = '就看你们的了！'
words = [w1, w2, w3, w4, w5, w6, w7, w8]

# 字体设置
font1 = pygame.font.SysFont('simhei', 25)
font2 = pygame.font.SysFont('simhei', 35)
font3 = pygame.font.SysFont('simhei', 20)
font4 = pygame.font.SysFont('simhei', 45)

# 图片加载
for name in names:
    pic = pygame.image.load('images/%s.png' % (name))
    plist.append(pic)
# 图片显示
for i in range(3):
    screen.blit(plist[i], (0, 0))

textX = 125


# 展示线索文字
def showText(text):
    global textX
    for t in text:
        word = font1.render(t, True, 'orange')
        screen.blit(word, (textX, 87))
        pygame.display.update()
        pygame.time.delay(100)
        textX += 25
    textX = 125


wordX = 330
wordY = 290


# 展示秘宝文字
def showWord():
    global wordX, wordY
    for word in words:
        for w in word:
            text = font3.render(w, True, 'darkgreen')
            screen.blit(text, (wordX, wordY))
            pygame.display.update()
            pygame.time.delay(180)
            wordX += 20
        wordX = 310
        wordY += 28


key = ''


# 随机生成密令
def createKey():
    global key
    binStr = ''
    for i in range(4):
        for j in range(3):
            binStr += random.choice(['0', '1'])
        texts[i] = texts[i] + binStr
        binStr = int(binStr, 2)
        key += str(binStr)
        binStr = ''


createKey()

# 鼠标区域标识
area = None
# 输入的密码
pwd = ''
# 木门的初始坐标
doorX = 0
doorY = 0
# 木门的移动状态
state = 'static'
# 是否点击石台
isclick = False
pwd_x = 385
while True:
    # 事件获取
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.MOUSEMOTION and state != 'finish':
            for i in range(3):
                screen.blit(plist[i], (0, 0))
            x = e.pos[0]
            y = e.pos[1]
            # 鼠标位置区域判断
            if 315 < x < 385 and 315 < y < 385:
                area = '1'
            elif 385 < x < 455 and 315 < y < 385:
                area = '2'
            elif 525 < x < 595 and 315 < y < 385:
                area = '3'
            elif 590 < x < 660 and 315 < y < 385:
                area = '4'
            elif 10 < x < 190 and 360 < y < 620:
                area = 'stone'
            else:
                area = None
            # 鼠标指针样式更改
            if area == None:
                screen.blit(plist[-2], (x, y))
            else:
                screen.blit(plist[-1], (x, y))
            pwd = ''
            pwd_x = 385
            isclick = False
        if e.type == pygame.MOUSEBUTTONDOWN and state != 'finish':
            # 人物线索显示
            if area != None:
                if area != 'stone':
                    aIndex = int(area)
                    showText(texts[aIndex - 1])
                else:
                    isclick = True
                    screen.blit(plist[2], (0, 0))
                    screen.blit(plist[3], (0, 0))
                pygame.display.update()
        if e.type == pygame.KEYDOWN and area == 'stone' and state != 'finish':
            # 非回车键，输入字母或者字符
            if e.key != 13:
                if isclick:
                    pwd += chr(e.key)
                    t = chr(e.key)
                    text = font4.render(t, True, 'white')
                    screen.blit(text, (pwd_x, 338))
                    pwd_x += 68
            # 回车键 判断密码
            else:
                if pwd == key:
                    state = 'move'
                else:
                    screen.blit(plist[0], (0, 0))
                    screen.blit(plist[1], (0, 0))
                    screen.blit(plist[2], (0, 0))
                    screen.blit(plist[-3], (0, 0))
                pwd = ''
                pwd_x = 385
                isclick = False
    if state == 'move':
        screen.blit(plist[0], (0, 0))
        screen.blit(plist[1], (doorX, doorY))
        screen.blit(plist[2], (0, 0))
        if doorY > -500:
            doorY -= 4
        else:
            state = 'finish'
            bgm = pygame.mixer.Sound("audio/bgm.ogg")
            bgm.set_volume(0.5)
            bgm.play()
            sound = pygame.mixer.Sound("audio/sound.ogg")
            sound.play()
            showWord()
    pygame.display.update()
