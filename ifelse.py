# -*- coding: utf-8 -*-
# ifelse.py
# 条件判断语句
# 通常两种形式
# if
# else
#
# if
# elif
# else
# 1、每个条件后面要使用冒号（:），表示接下来是满足条件后要执行的语句块。
# 2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
# 3、在Python中没有switch – case语句。
#
# if中常用的操作运算符:
# <	小于
# <=	小于或等于
# >	大于
# >=	大于或等于
# ==	等于，比较对象是否相等
# !=	不等于

# 例子：
# Python 判断奇数偶数
# 如果是偶数除于 2 余数为 0
# 如果余数为 1 则为奇数

# num = int(input("请输入一个数字："))
# if (num % 2) == 0:
#     print('{0}是偶数'.format(num))
# else:
#     print('{0}是奇数'.format(num))

# if 嵌套
# 在嵌套 if 语句中，可以把 if...elif...else
# 结构放在另外一个 if...elif...else 结构中。
# 例子：
# 判断是否是闰年
# 能被4整除却不能被100整除 或 能被400整除的年份是闰年.

year = int(input("请输入年份数字："))

# 第一步：判断能否给4整除
# 第二步：判断是否能给100整除
# 第三步，判断能否给400整除

if (year % 4) == 0:
    if (year % 100) == 0:
        if(year % 400) == 0:
            print("{0} 是闰年".format(year)) # 整百年能被400整除的是闰年
        else:
            print("{0} 不是闰年".format(year))
    else:
        print("{0} 是闰年".format(year)) # 非整百年能被4整除的为闰年
else:
    print("{0} 不是闰年".format(year))