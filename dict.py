#!/usr/bin/python3
#-*- coding: utf-8 -*-
#
# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
#
# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

# 普通定义
dict01 = { 'time':'3600s', 'name':'Jack', 'name':'Tom' }
print(dict01, '\n')

# 列表，元组转换
dict02 = dict( a='a', b='b', t='t' )
print(dict02, '\n')

# 列表 键 / 值 对
list = [ ('name', 'Jack') , [ 'role', 'Admin' ] ]
dict03 = dict( list );
print(dict03, '\n')

# 访问字典里的值
print( dict03['name'], dict03['role'] , '\n')

# 修改字典
dict03['name'] = 'Tom'
print(dict03, dict03['name'], '\n')

# 增加字典键值对
dict03['money'] = 1000
print(dict03, '\n')

# 删除键值对
del dict03['money']
print(dict03, '\n')

# 清空字典
dict03.clear()
print(dict03, '\n')

# 删除字典
# del dict03
# print(dict03, '\n')

# 字典键的特性
# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住

# 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
# dict = {['Name']: 'Zara', 'Age': 7}
# print( "dict['Name']: ", dict['Name'])

#============================
#    字典内置函数
#============================
# 查找
print(dict01)
print( "键name对应的值 : %s" % dict01.get('name') )
#  Python 3.X 里不包含 has_key() 函数，被 __contains__(key) 替代:
print( "键name是否存在于字典中：%s" % dict01.__contains__('name'), '\n')

print("遍历字典中所有的元素")
for key, values in dict01.items():
    print(key, values)

print("删除字典中的键对应的值")
time  = dict01.pop('time')
print('删除的值：', time, '删除后的字典：', dict01 )

