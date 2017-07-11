#!/usr/bin/python3
#-*- coding: utf-8 -*-

#============================
#    常规用法
# 元组与列表的区别就在于，元组是一种不可变序列。元组变量的赋值要在定义时就进行，
# 这就像C语言中的const变量或是C++的引用，定义时赋值之后就不允许有修改。元组存在的意义是：
# 元组在映射中可以作为键使用，因为要保证键的不变性。
# 元组作为很多内置函数和方法的返回值存在。
#============================

# 直接定义 [] 定义的是列表 ()定义的是元组
tul1 = ['a', 'b', 'c', 'd', 'e', 'f']
tul2 = ('a', 'b', 'c', 'd', 'e', 'f')

# 使用list函数
tul3 = tuple('abcdef')
print(tul1, tul2, tul3)
print( type(tul1), type(tul2), type(tul3), '\n' )

a = 10*(1)
b = 10*(1,)
print(a, type(a), b, type(b))

#============================
#    元组内置函数
#============================
# len(tuple)
print( 'tul2的长度：%d' % len(tul2) )
# max(tuple)
print( 'tul2的最大值：%s' % max(tul2) )
# min(tuple)
print( 'tul2的最小值：%s' % min(tul2) )
# tuple(seq)
# 将列表转换为元组。
tul4 = tuple(tul1)
print(tul1, type(tul1), '\n', tul4, type(tul4), '\n' )

print('元组里面存放列表')
tul5 = ('a', 'b', tul1)
print(tul5, '\n')

print('元组里面存放元组')
tul6 = ('a', 'b', tul2)
print(tul6, '\n')
