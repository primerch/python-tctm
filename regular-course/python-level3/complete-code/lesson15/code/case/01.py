# 获取今天的日期
import datetime

from utils import CSVHandler

today = datetime.datetime.now()
# 科目
subject_list = ['语文', '数学', '英语'] * 4
# 作业内容
subject_content_list = ['背诵课文第二段', '做10道题', '听英语诗朗诵', '写作文', '做10道题', '预习单词'] * 2
# 作业状态
states_list = ['未完成'] * 12
# 生成二维列表
data = [[today.strftime('%Y-%m-%d'), subject_list[i], subject_content_list[i], states_list[i]] for i in range(12)]
# 写入到文件
CSVHandler.save('homeworks.csv', data)
