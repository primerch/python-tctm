import time

# boss属性字典
boss = {'atk': 300,
        'def': 50,
        'HP': 10000
        }
print(boss)
# player属性字典
player = {'HP': 1000,
          'maxHP': 1000,
          'atk': 100,
          'def': 50,
          'addHP': 200,
          'addAtk': 200,
          'addDef': 100,
          'magic': 1000}

while True:
    # 玩家选择提示信息
    print('请选择你的攻击招式序号')
    print('1.普通攻击，2.加血，3.魔法攻击，4.增加攻击力，5.增加防御力')
    # 输入变量
    n = input()
    # 普通攻击，计算player对boss伤害，并修改boss生命
    if n == '1':
        damage = player['atk'] - boss['def']
        boss['HP'] -= damage
        print('你发动普通攻击，伤害为', damage)
    # 加血，并修改player血量
    elif n == '2':
        player['HP'] += player['addHP']
        if player['HP'] >= player['maxHP']:
            player['HP'] = player['maxHP']
        print('你发动加血技能，增加血量', player['addHP'])
    # 魔法攻击，计算player对boss伤害，并修改boss生命
    elif n == '3':
        damage = player['magic'] - boss['def']
        boss['HP'] -= damage
        print('你发动魔法攻击，伤害为', damage)
    # 加攻，修改player攻击力
    elif n == '4':
        player['atk'] += player['addAtk']
        print('你发动增加攻击力技能，增加攻击力', player['addAtk'])
    # 加防，修改player防御力
    elif n == '5':
        player['def'] += player['addDef']
        print('你发动增加防御力技能，增加防御力', player['addDef'])
    # 跳过回合
    else:
        print('你跳过此回合')
    time.sleep(1)
    # boss伤害计算，修改player血量
    damage = boss['atk'] - player['def']
    player['HP'] -= damage
    if damage <= 0:
        damage = 0
    print('boss发动普通攻击，伤害为', damage)
    time.sleep(1)

    # 血量剩余提示信息及属性显示
    print('你的血量为：', player['HP'])
    print('player的属性：')
    for key in player:
        print(key, player[key])
    time.sleep(1)

    print('boss血量为：', boss['HP'])
    print('boss的属性：')
    print('atk:', boss['atk'])
    print('atk:', boss['def'])
    print('HP:', boss['HP'])
    time.sleep(1)

    # 游戏结果判断
    if player['HP'] <= 0 or boss['HP'] <= 0:
        print('游戏结束')
        break
