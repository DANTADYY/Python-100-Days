'''
用户身份验证

Version：0.1
Author： daiyy
'''
username = input('请输入用户名：')
password = input('请输入口令：')

# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')

'''
分段函数求值1

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
Version：0.1
Author: daiyy

'''
X = float(input('X = '))
if X > 1:
    Y = 3 * X - 5
elif X >= -1 and X <= 1:
    Y = X + 2
else:
    Y =  5 * X + 3
print('f(%.2f) = %.2f' %(X,Y))

'''
分段函数求值2

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
Version：0.1
Author: daiyy
'''
X = float(input('X = '))
if X > 1:
    Y = 3 * X - 5
else:
    if X >= -1 and X < 1:
        Y = X + 2
    else:
        Y = 5 * X + 3
print('f(%.2f) = %.2f' % (X, Y))

