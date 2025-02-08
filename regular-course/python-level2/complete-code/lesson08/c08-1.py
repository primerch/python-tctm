import pygame
import sys

# 初始化及窗口设置
pygame.init()
screen = pygame.display.set_mode((1000, 700))
# 鼠标指针显示设置
pygame.mouse.set_visible(0)
# 图片名称列表
names = ['bg', 'for', 'list', 'random', 'function', 'box', 'lose', 'win', 'm0', 'm1']
# 建立变量存字符串
t1 = '我找到了一张粉色纸条：'
t2 = '这有一张蓝色卡片：'
t3 = '绿色卡片给你：'
t4 = '和我衣服一样颜色的卡片：'
talks = [t1, t2, t3, t4]
# 提示信息的字体字号选择
font = pygame.font.SysFont('kaiti', 40)
# 宝箱输入文字的字体字号选择
font1 = pygame.font.SysFont('fangsong', size=120)
# 图片存储列表
plist = []
# 加载所有图片
for name in names:
    pic = pygame.image.load('images/%s.png' % (name))
    plist.append(pic)
# 游戏资源加载
screen.blit(plist[0], (0, 0))
pygame.display.update()

offset = 0


# 文字显示
def showTalk(words):
    global offset
    for i in words:
        text = font.render(i, True, 'black')
        screen.blit(text, (330 + offset * 40, 570))
        pygame.display.update()
        pygame.time.delay(100)
        offset += 1
    offset = 0


actor = None
pwd = ''
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        # 鼠标移动更改鼠标图标样式
        if e.type == pygame.MOUSEMOTION:
            screen.blit(plist[0], (0, 0))
            x = e.pos[0]
            y = e.pos[1]
            print('鼠标的x坐标是: % d, y坐标是 % s' % (x, y))
            if 130 < x < 200 and 300 < y < 400:
                actor = 'for'
            elif 220 < x < 320 and 80 < y < 180:
                actor = 'list'
            elif 650 < x < 750 and 150 < y < 210:
                actor = 'random'
            elif 720 < x < 820 and 320 < y < 420:
                actor = 'function'
            elif 400 < x < 620 and 300 < y < 450:
                actor = 'box'
            else:
                actor = None

            print(actor)

            # 鼠标图标更改
            if actor == None:
                screen.blit(plist[-2], (x, y))
            else:
                screen.blit(plist[-1], (x, y))
            pygame.display.update()
            pwd = ''
        # 按下鼠标按键事件
        if e.type == pygame.MOUSEBUTTONDOWN:
            if actor in names:
                screen.blit(plist[0], (0, 0))
                aIndex = names.index(actor)
                screen.blit(plist[aIndex], (0, 0))
                if actor != 'box':
                    showTalk(talks[aIndex - 1])
                pygame.display.update()
        # 使用键盘输入密码
        if e.type == pygame.KEYDOWN:
            if actor == 'box':
                pwd += chr(e.key)
                text = font1.render(pwd, True, 'white')
                screen.blit(plist[5], (0, 0))
                screen.blit(text, (250, 280))
                pygame.display.update()
