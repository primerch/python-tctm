# 1. 定义插入排序函数insertSort和参数cards，接收待排序的列表
def insertSort(cards):
    # 2. 从列表的第二个元素开始遍历
    for i in range(1, len(cards)):
        # 3. 取出当前元素pick
        pick = cards[i]
        # 4. 定义一个变量pre，指向当前元素的前一个元素的位置
        pre = i - 1
        # 5. 循环判断pre是否不小于0且当前元素小于它前面的元素
        while pre >= 0 and pick < cards[pre]:
            # 6. 将前面的元素后移一位
            cards[pre + 1] = cards[pre]
            # 7. pre减一
            pre -= 1
        # 8. 将当前元素pick插入到正确的位置
        cards[pre + 1] = pick


# 9. 定义13张无序的扑克牌列表cards
cards = [2, 2, 7, 8, 10, 11, 3, 4, 6, 7, 9, 12, 1]
# 10. 输出初始扑克牌顺序
print('初始牌顺序：', cards)
# 11. 调用insertSort函数，对cards进行插入排序
insertSort(cards)
# 12. 输出排序后的扑克牌顺序
print('排序后牌顺序：', cards)
