'''
我现在要文件读写这个知识点，用来写入项目中的游戏得分和读取历史记录得分。这是我的授课思路：
问题:  历史记录不能保存在变量中，因为即使关闭游戏它也需要一直存储，那该如何保存历史记录呢？
解决：需要使用一个文件保存历史记录，创建文件score.txt，默认保存的历史记录为0
问题 ：如何在程序中打开一个文件，并获取score.txt文件中的历史记录呢？
解决：读取文件内容，分为3步。第一步：使用open函数以可读模式‘r’，打开文件；第二步：使用read方法读取文件内容；第三步：读取文件后，使用close关闭文件
问题：总是忘记调用close关闭文件怎么办
解决：可以使用with open打开文件，操作完成后会自动关闭文件
讲完读文件再讲写文件
问题：现在无论游戏得分是多少，历史记录一直显示0，并没有更新历史记录
解决：因为还要更新历史记录，当本次得分大于从文件中获取的历史记录时，就需要把本次得分写入到score.txt文件
问题： 如何把获得的新历史记录，写入到score.txt文件中呢？
解决： 首先需要使用with open以可写模式打开score.txt文件，然后调用write方法把新历史记录写入文件
问题： write方法需要传入一个字符串类型的数据，而显示贼的score是一个整数类型
解决：使用str方法把score转为字符串类型。注意：新写入的内容会覆盖之前的内容。更新了文件中的最高分后，也需要及时更新程序中highScore存储的历史记录，
这样才能立刻把新的历史记录绘制出来

这是我的代码：
while True:
    if Game.life <= 0:
        screen.blit(Game.endBg, (0, 0))
        with open('score.txt', 'r') as f:
            highScore = f.read()
        Game.drawText(highScore, (600, 330))
        Game.drawText(Game.score, (600, 390))

while True:
    if Game.life <= 0:
        screen.blit(Game.endBg, (0, 0))
        with open('score.txt', 'r') as f:
            highScore = f.read()
        if Game.score > int(highestScore):
            with open('score.txt', 'w') as f:
                f.write(str(Game.score))
                highScore = Game.score

请帮我使用中文，根据以上知识点出5道单选题，帮助学生理解文件读写的方法，包括文件读写的步骤、文件的读写的重要函数、with语句、注意事项等，不需要答案.
'''
