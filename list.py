#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ============================
#    常规用法
# ============================
# 直接定义
var1 = ['H', 'e', 'l', 'l', 'o']
# 使用list函数
var2 = list('Hello')
print(var1, var2)

# 访问列表中的值
print('取前4个值：%s\n取前4个值：%s\n取2到4间的值：%s\n取从开头到倒数第二个值：%s ' % (var1[0:4], var1[:4], var1[1:4], var1[:-1]))

# 改变列表元素的值
var1[1] = '我是新的值'
print(var1, '\n')

# 删除列表元素
print('删除前', var2)
del var2[1]
print('删除后：', var2, '\n')

# Python列表脚本操作符
# len([1, 2, 3])	3	长度
print('var2的长度：', len(var2));
# [1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
var3 = var1 + var2
print('var1和var2组合后：', var3)
# ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
print('重复var2 4次 ：%s' % (var2 * 4))
# 3 in [1, 2, 3]	True	元素是否存在于列表中
print('H是否存在于var2中：', ('H' in var2))
# for x in [1, 2, 3]: print(x, end=" ")	1 2 3	迭代
for str in var2:
    # print(str, end=" ")
    print(str)
print('\n')
# ============================
#    列表函数
# ============================

# append
# 功能：用于在列表末尾追加新的元素
list1 = ['Baidu', 'Ali', 'Tencent']
print('BAT三巨头：%s' % list1)
list1.append('1024')
print('混入一个奇奇怪怪的网站后：%s' % list1, '\n')

# extend
# 功能：在列表末尾一次性追加另一个序列中的多个值
list2 = ['jd', 'xiaomi']
list1.extend(list2)
print('更多人加入了队伍：%s' % list1, '\n')

print('我要找到组织1024：', list1.index('1024'))

print('1024由于某种神秘原因要消失了：')
# 传递待删除元素，如果多个元素一样，默认删除第一个：
list1.remove('1024')
print(list1, '\n')

print('jd说我不跟你玩了！')
# pop()方法，传递的是待删除元素的index：
list1.pop(3)
print(list1, '\n')

print('时代变了，要换下顺序')
# 功能：该方法对序列方向存放
list1.reverse()
print(list1, '\n')

print('有人不同意上面的排队，需要重新排队')
list1.sort()
print(list1, '\n')
