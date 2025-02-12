'''
我想在生成的计算器界面中实现加减乘除运算
问题：点击按钮和按下键盘的操作都是将按钮文本显示到文本框，如何避免重复写两遍
解决：封装calc()函数，接收文本参数
问题：在程序运行时，无论输入多少，都在文本框中只显示最后的按钮文本
解决：将新输入的文本和旧文本拼接到一起
问题：在输入等号后，不但没有计算，还能继续往后输入
解决：在计算函数中添加判断条件，如果点击的是=，就执行计算
问题：文本框中的算式，是字符串类型，程序无法计算
解决：使用eval()函数来专门计算字符串类型的算式
问题：按下 c 无法清楚文本
解决：加判断条件，如果按下的是 c，则将文本显示为空字符串

这是我的授课代码：
# 将相同的代码逻辑封装在calc方法中
def calc(text):
    curr = ledit.text()
    # 1. 输入等号计算并显示结果
    if text == '=':
        new = str(eval(curr))
    # 2. 输入 c ，清空文本框
    elif text == 'c':
        new = ''
    # 3. 其他情况，拼接字符串
    else:
        new = curr + text
    ledit.setText(new)


def btn_click():
    btn = window.sender()
    text = btn.text()
    # 调用计算函数
    calc(text)

def keypress(event):
    key = event.key()
    text = event.text()
    # 判断是否按下的是回车或者换行符
    if key == Qt.Key_Enter or key == Qt.Key_Return:
        calc('=')
    # 如果按下的是规定内的文本则计算
    elif text in '0123456789+-*/.c=':
        calc(text)

请帮我使用中文，根据以上内容出5道单选题，帮助学员理解批量创建控件不需要答案。
'''
