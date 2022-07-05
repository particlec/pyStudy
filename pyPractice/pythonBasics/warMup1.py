import numpy as np

# 数学运算
var = 2 + 2
print(var)
print(7 - 2.5)
print(3 * 2.5)
print(8 / 2)
print(1 / 3)
# 字符串操作
s = "hello world"
print(s)
print(s[0])
print(s[-1])
print(s[:5])
# 字符串切割
print(s.split())
# 字符串长度 空格也有长度
print(len(s))

# 列表数组
a = [1, 2.0, 'hello', 5 + 1.0]
print(a)
# a [1, 2.0, 'hello', 6.0]

# 数组简单拼接
print(a + a)
print(a[1])
print(len(a))

# 集合(js里的对象)
s = {2, 3, 4, 2}
len(s)

# 集合偏数学
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
# 交集
print(a & b)
# 并集 有重复的自动去除-
print(a | b)

# 字典 js中的json对象
# {key:value}
d = {'dogs': 5, 'cats': 4}
print(d)
# len感觉啥长度都可以
print(len(d))
# 感觉跟对象没啥区别，语言的数据类型差不多
print(d["dogs"])
# 这个是不行的
d["pigs"] = 7

# NumPy数组 跟列表有啥区别吗
# import numpy as np
# a = np.array([1, 2, 3, 4])


# Matplotlib对数据进行可视化
# from matplotlib import pyplot as plt
# plt.plot(a, a**2)

# 循环
line = '1 2 3 4 5'
fields = line.split()
print(fields)

total = 0
for field in fields:
    total += int(field)
print(total)


# 函数 使用括号对函数进行调用： abs(-12.3)
# 用def定义函数：
def poly(x, a, b, c):
    y = a * x ** 2 + b * x + c
    return y


x = 1
print(poly(x, 1, 2, 3))

# 用Numpy数组做参数：还不会这个的运算

x = np.array([1, 2, 3])
print(poly(x, 1, 2, 3))


# array([6, 11, 18])


# 类
# 用class定义类
class Person(object):
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return self.first + ' ' + self.last


# 构建对象：
person = Person('Mertle', 'Sedgewick', 52)
print(person.first)
print(person.full_name())
