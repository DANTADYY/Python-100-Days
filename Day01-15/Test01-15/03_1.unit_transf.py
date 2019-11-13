'''
英制单位英寸和公制单位厘米转换
Version：0.1
Author: daiyy
'''
value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value,value * 2.54)) 
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value,value / 2.54))
else:
    print('请输入有效单位')

#**要求**：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
#参考答案：

'''Python
"""
百分制成绩转换为等级制成绩

Version: 0.1
Author: daiyy
"""
'''
score = float(input('请输入成绩：'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >=70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)     