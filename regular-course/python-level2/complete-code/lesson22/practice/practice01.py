# 课堂练习一
# 已知嵌套结构的字典weather_data，里面存储了某一天上海和北京的天气信息，请获取当天北京的最高温度并输出
# 提示： temperature-温度 、 high-最高温 、 low-最低温   

weather_data = {
    'Shanghai': {'date': '2023-xx-xx',
                 'weather': 'Sunny',
                 'temperature': {
                     'high': '28°C',
                     'low': '18°C'
                 },
                 },
    'Beijing': {
        'date': '2023-xx-xx',
        'weather': 'Cloudy',
        'temperature': {
            'high': '23°C',
            'low': '13°C'
        },
    },
}
# 请在下方编写输出北京最高温度的代码
t = weather_data['Beijing']['temperature']['high']
print('北京的最高温度为：', t)
