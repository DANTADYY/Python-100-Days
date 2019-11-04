# 温度转换 华氏温度转换摄氏温度
"""
Version: 0.1
Author: daiyy 
"""
f = float(input('请输入华氏温度： ')) 
g = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' %(f,g))

#输入半径，计算圆的面积与周长
"""
输入半径计算圆的周长和面积
"""
import math

radius = float(input('请输入圆的半径： '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长：%.2f' % perimeter)
print('面积： %.2f' % area)

#输入年份判断是否闰年
"""
输入年份 如果是闰年则输出：True 否则输出：False
"""
year = int(input('请输入年份： '))
#如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
is_leap = (year % 4 == 0 and year % 100 != 0) or \
               year % 400 == 0
print(is_leap)