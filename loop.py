# -*- coding: utf-8 -*-

# 循环有两种形式：
# for循环
# while循环

# for...in循环，依次把list或tuple中的每个元素迭代出来
# 例子
# 求和
# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum + x
# print(sum)

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
# 例子
# 求和

# sum = 0
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# count = 0
#
# while count < len(list):
#     sum = sum + list[count]
#     count = count + 1
# print(sum)

# 例子
# 偶数求和

# sum = 0
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# index = 0
#
# while index < len(list):
#     if (index % 2) != 0:
#         sum = sum + list[index]
#     index = index + 1
# print(sum)



# pass 语句
# Python pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句
# break和continue
# break 语句，可以跳出 for 和 while 的循环体。
# continue语句，跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
# 如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行

for num in range(1, 10):
    if (num % 2) == 0: # 如果是偶数
        # continue
        break
        pass
    print('当前字母{0}'.format(num))