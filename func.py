# -*- coding: utf-8 -*-

# 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

# 定义函数
# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
# def 函数名（参数列表）:
#     函数体

# def sum_total(num1, num2):
#     return num1 + num2
#
# print('3+5 = %d' % sum_total(3, 5))
#

# 不可变对象
# def ChangeInt( a ):
#     a = 10
#
# b = 2
# ChangeInt(b)
# print( b ) # 结果是 2


# 可写函数说明
# def changeme(mylist):
#     "修改传入的列表"
#     mylist.append([1, 2, 3, 4]);
#     print("函数内取值: ", mylist)
#     return
#
#
# # 调用changeme函数
# mylist = [10, 20, 30];
# changeme(mylist);
# print("函数外取值: ", mylist)

# 关键字参数
# def square(width, height):
#     return width * height
#
# # 计算面积
# s = square(30, 40)
# # s = square(width=30, height=40)
# # s = square(height=40, width=30)
# # s = square(40, 30)
# # s = square(width=30)
#
#
# print('30 * 40的面积是：%d' % s )



# 不定长参数
# def sum_total(num, *args):
#     print(num)
#     print(type(args))
#
#     for var in args:
#         print('当前传进来的不定长参数：', var)
#
# sum_total(3, 5, 7, 9)


# 函数作用域
total = 0 # 这是一个全局变量

def sum( arg1, arg2 ):

    # global total # total使用global声明为全局变量.
    # nonlocal total # total使用nonlocal声明为非本地变量.
    total = arg1 + arg2# total在这里是局部变量.

    print ("函数内是局部变量 : ", total)
    return total

#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ", total)


# 当内部作用域想修改外部作用域的变量时，就要用到global
# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字

def outer():
    num = 10
    def inner():
        # global num   # nonlocal关键字声明
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)

outer()