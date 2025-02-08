player = {'HP': 1000,
          'maxHP': 1000,
          'atk': 100,
          'def': 50,
          'addHP': 200,
          'addAtk': 200,
          'addDef': 100,
          'magic': 1000}

# 练习删除元素
player.pop('magic')
print(player)

del player['def']
print(player)

player.clear()
print(player)

del player
print(player)
