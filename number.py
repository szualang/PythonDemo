#!/usr/bin/python3
#-*- coding: utf-8 -*-
import math

import math, random
#============================
#    数字常规用法
#============================

num = 1024
print (num)

# 除法 python 2.7 / // 取整数， python 3.6 / 浮点 // 取整数
print ('/ :' , 7 / 5)
print (' // :', 7 // 5)

# Python 数字类型转换
# int(x) 将x转换为一个整数。
# float(x) 将x转换到一个浮点数。
# complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
# complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
print ('二进制:', bin(num) )
print ('八进制:', oct(num) )
print ('十六进制:', hex(num) )
print('\n')

# Python 可以使用 ** 操作来进行幂运算：
print( 2 ** 10 )
print('\n')


#============================
#    数学函数
#============================

# 函数	返回值 ( 描述 )
# abs(x)	返回数字的绝对值，如abs(-10) 返回 10
# fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
print( '-1024的绝对值：', abs(-1024) )
print( '-1024的绝对值：', math.fabs(-1024) )
print('\n')
# ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
# floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
print( ' 10.24向上取整：', math.ceil(10.24) ) # 要引入math类库
print( ' 10.24向下取整：', float(10.24) )
print('\n')


# max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
# min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
list = [1, 2, 3, 4, 5, 6, 7 ]
print('最大值是%d' % max(list) )
print('最小值是%d' % min(list) )
print('\n')
# pow(x, y)	x**y 运算后的值。
# sqrt(x)	返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j
print('2的10次方是：%d' % pow(2, 10) )
print('1024平凡根是：%d' % math.sqrt(1024) )
print('\n')
# round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
print('浮点数 10.24 的四舍五入值：%d' % round(10.24) )
print('浮点数 6.66 的四舍五入值：%d' % round(6.66) )
print('\n')
#============================
#    随机数函数
#============================

# choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
count = 0
while count < 10:
    print('序列0到99中随机抽取：%d', random.choice( range(100) ) )
    count += 1
print('\n')

# randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
count = 0
while count < 10:
    print('从0到9范围内随机获取：%d',  random.randrange(0, 9, 1) )
    count += 1
print('\n')

# random()	随机生成下一个实数，它在[0,1)范围内。
print('随机生成一个随机数：%d',  random.random() )
print('随机生成一个随机数：%d',  random.random() )
print('\n')

# seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
random.seed(100)
print('种子100，生成一个随机数：%d',  random.random() )
print('\n')

# shuffle(lst)	将序列的所有元素随机排序
print(list)
random.shuffle(list)
print(list)
