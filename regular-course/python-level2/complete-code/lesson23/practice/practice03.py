# 课堂练习3
# 获取当前时间，并以 时：分：秒 的格式输出，要求时间是以12小时制呈现的，且能显示PM或AM
"""
    %Y  - 年份位置
    %m  - 月份位置
    %d  - 日期位置
    %H  - 小时位置
    %M  - 分钟位置
    %S  - 秒钟位置
    %I  - 小时位置（12小时制）
    %p  Locale's equivalent of either AM or PM.
"""
import time

t = time.strftime("%I:%M:%S %p", time.localtime())
print(t)
