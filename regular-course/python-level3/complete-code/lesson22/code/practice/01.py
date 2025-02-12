addrs = [
    "北京交通大学篮球场 行知大道北京交通大学",
    "中国政法大学篮球场 海淀区西土城路25号",
    "丰台区数字空间篮球场 马家堡路与西马场路交叉口鑫利后市场北",
    "首都经贸大学篮球场 丰台区张家路口121号",
    "北京经贸学院篮球场 房山区长虹东路29号",
    "海淀区活力赛场篮球场 西城区展览路街道大钱市胡同新兴东港11号",
    "海淀区博乐篮球场 海淀区中信大厦一楼",
    "优肯国际篮球场 海淀实验中学校区",
    "UC篮球场万柳基地中心 海淀区万柳中路6号院4号"
]


# 1. 定义一个名为find的函数，用于在给定的字符串中查找特定的子串
def find(fullstr, target):
    # 2. 获取目标子串的长度
    n = len(target)
    # 3. 遍历整个给定的字符串
    for i in range(len(fullstr)):
        # 4. 如果找到与目标子串的第一个字符相匹配的字符
        if fullstr[i] == target[0]:
            # 5. 检查从当前位置开始的子串是否与目标子串匹配
            if fullstr[i: i + n] == target:
                # 6. 如果匹配，返回True
                return True
        # 7. 如果剩余的字符数量少于目标子串的长度，结束循环
        if i == len(fullstr) - n:
            break
    # 8. 如果没有找到匹配的子串，返回False
    return False


# 9. 请求用户输入关键词
keyword = input("请输入地点：")
# 10. 如果关键词中包含空格，说明用户输入了两个关键词
if ' ' in keyword:
    # 11. 根据空格分割关键词
    word1, word2 = keyword.split(' ')
    # 12. 遍历地址列表，在地址列表中查找包含两个关键词的地址, 并输出找到的地址
    for addr in addrs:
        if find(addr, word1) and find(addr, word2):
            print(addr)
# 13. 如果只有一个关键词，直接在地址列表中查找，并输出找到的地址
else:
    for addr in addrs:
        if find(addr, keyword):
            print(addr)
