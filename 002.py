#!/usr/bin/python3

# 数据类型

# 整数类型 和 Java 并没有什么区别，只是没有 位数限制 Java 是32位整数，Python 无限大

# 浮点数(小数) 1.23x109 和12.3x108 （科学计数法）是完全相等的

# 字符串 有些特别
# 使用 r'' 表示 ''内部的字符串默认不转义

print('\\\t\\')

print(r'\\\t\\')

# 如果字符串内部有很多 换行 用 \n 写一行不好阅读 Python 允许使用 '''...''' 的格式表示多行内容

print('''
line1
line2
line3
''')

#布尔值


print(True)
print(False)

age = 30

if age >= 18:
    print('ault')
else:
    print('teenager')

# 空值

print(None)

# Python 是动态语言

a = 123
print(a)
a = 'ABC'
print(a)


