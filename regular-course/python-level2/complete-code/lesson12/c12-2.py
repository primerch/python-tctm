player = {'HP': 1000,
          'maxHP': 1000,
          'atk': 100,
          'def': 50,
          'addHP': 200,
          'addAtk': 200,
          'addDef': 100,
          'magic': 1000}
# 遍历字典中的键和值
for key in player.keys():
    print(key)
for value in player.values():
    print(value)
for key, value in player.items():
    print(key, value)
