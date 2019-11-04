# print('hello world').

'''
Python
'''

"""
使用变量保存数据并进行算术运算

Version: 0.1
Author: 戴琰
"""

# a = 321
# b = 123
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)


e = 123
f = 123.456
g = 1 + 3j 
h = 'hello world'
i = False
print(type(e)),# <class 'int'> 
print(type(f)),# <class 'float'>
print(type(g)),# <class 'complex'>
print(type(h)),# <class 'string'>
print(type(i)),# <class 'bool'>

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))