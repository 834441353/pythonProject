# -*- coding: utf-8 -*-
import requests

city = '北京'
key = '580c4cfd2d078baaf3b81e42bc76e582'
# rep = requests.get('http://apis.juhe.cn/simpleWeather/query?city=' + city + '&key=' + key)
rep = requests.get('http://apis.juhe.cn/simpleWeather/query?city=%s&key=%s' % (city, key))
rep.encoding = 'utf-8'
print('返回结果：%s\n' % rep.json())
print('温度：%s\n' % rep.json()['result']['realtime']['temperature'])
print('湿度：%s\n' % rep.json()['result']['realtime']['humidity'])
print('天气情况：%s\n' % rep.json()['result']['realtime']['info'])
print('风向：%s\n' % rep.json()['result']['realtime']['direct'])
print('风力：%s\n' % rep.json()['result']['realtime']['power'])
print('空气质量指数：%s\n' % rep.json()['result']['realtime']['aqi'])
