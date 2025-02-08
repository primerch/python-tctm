keys = ['HP', 'maxHP', 'atk', 'def', 'addHP',
        'addAtk', 'addDef', 'magic']
values = [1000, 1000, 100, 50, 200, 200, 100, 1000]

player = dict.fromkeys(keys)
print(player)

i = 0
for k in keys:
    player[k] = values[i]
    i = i + 1
print(player)
