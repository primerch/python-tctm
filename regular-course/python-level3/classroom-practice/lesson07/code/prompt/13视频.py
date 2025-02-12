"""

这是我今天编写的代码：
```
class Utils:
    @staticmethod
    def drawText(text, pos):
        font = pygame.font.Font('fonts/WRYH.ttf', 40)
        textImg = font.render(str(text), True, 'orange')
        screen.blit(textImg, pos)


while True:
    if Game.life == 0:
        screen.blit(Game.endBg, (0, 0))
        with open('score.txt', 'r') as f:
            highScore = f.read()
        if Game.score > int(highScore):
            with open('score.txt', 'w') as f:
                f.write(str(Game.score))
                highScore = Game.score
        Utils.drawText(highScore, (600, 330))
        Utils.drawText(Game.score, (600, 390))
        pygame.display.update()
        pygame.time.delay(3000)
        exit()
    screen.blit(Game.scoreBoard, (0, 0))
    Utils.drawText(Game.score, (115, 20))
    screen.blit(Game.heart, (970, 40))
    Utils.drawText(Game.life, (1050, 30))

```
请根据代码详细总结今天学习的有关类，文件读写和pygame的所有知识点


"""
