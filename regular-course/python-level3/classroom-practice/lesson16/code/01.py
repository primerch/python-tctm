from datetime import datetime, timedelta

from utils import CSVHandler

today = datetime.now()
# 使用列表推导式生成日期字符串列表 日期范围是从60天前到今天为止
date_list = [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(60)]
date_list.reverse()
# 科目为语文数学英语重复20次
subject_list = ['语文', '数学', '英语'] * 20
# 作业内容重复10次
subject_content_list = ['背诵课文第二段', '做10道题', '听英语诗朗诵', '写作文', '做10道题', '预习单词'] * 10
# 作业状态列表重复10次
states_list = ['已完成', '已完成', '未完成', '未完成', '已完成', '已完成', '已完成', '未完成', '已完成'] * 10
data = [[date_list[i], subject_list[i], subject_content_list[i], states_list[i]] for i in range(60)]
CSVHandler.save('homeworks.csv', data)
