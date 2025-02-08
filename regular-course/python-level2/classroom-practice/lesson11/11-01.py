import time

# 人物属性
playerHP = 1000
playerMaxHP = 1000
playerAtk = 100
playerDef = 50
addHP = 200
addAtk = 200
addDef = 100
magic = 1000
# boss属性
bossHP = 10000
bossDef = 50
bossAtk = 300

while True:
    # 玩家选择提示信息
    print('请选择你的攻击招式序号')
    print('1.普通攻击，2.加血，3.魔法攻击，4.增加攻击力，5.增加防御力')
    # 输入变量
    n = input()
    # 普通攻击，计算player对boss伤害，并修改boss生命
    if n == '1':
        damage = playerAtk - bossDef
        bossHP -= damage
        print('你发动普通攻击，伤害为', damage)
    # 加血，并修改player血量
    elif n == '2':
        playerHP += addHP
        if playerHP >= playerMaxHP:
            playerHP = playerMaxHP
        print('你发动加血技能，增加血量', addHP)
    # 魔法攻击，计算player对boss伤害，并修改boss生命
    elif n == '3':
        damage = magic - bossDef
        bossHP -= damage
        print('你发动魔法攻击，伤害为', damage)
    # 加攻，修改player攻击力
    elif n == '4':
        playerAtk += addAtk
        print('你发动增加攻击力技能，增加攻击力', addAtk)
    # 加防，修改player防御力
    elif n == '5':
        playerDef += addDef
        print('你发动增加防御力技能，增加防御力', addDef)
    # 跳过回合
    else:
        print('你跳过此回合')
    time.sleep(1)
    # boss伤害计算，修改player血量
    damage = bossAtk - playerDef
    playerHP -= damage
    if damage <= 0:
        damage = 0
    print('boss发动普通攻击，伤害为', damage)
    time.sleep(1)

    # 血量剩余提示信息及属性显示
    print('你的血量为：', playerHP)
    time.sleep(1)
    print('boss血量为：', bossHP)
    time.sleep(1)

    # 游戏结果判断
    if playerHP <= 0 or bossHP <= 0:
        print('游戏结束')
        break
