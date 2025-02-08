# 课堂练习2
# 将字典game中的内容以如下格式输出
'''
小派vs童童,
游戏精灵vs小海龟,
列表精灵vs字典精灵
'''
game = {
    '小派': '童童',
    '游戏精灵': '小海龟',
    '列表精灵': '字典精灵',
}
for x, y in game.items():
    word = x + 'vs' + y
    print(word)
