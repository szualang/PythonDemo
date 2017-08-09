# -*- coding: utf-8 -*-
import math, random

def loop_merge_sort(list_a, list_b):
    tmp_list = []
    while len(list_a) > 0 and len(list_b) > 0:
        if list_a[0] < list_b[0]:
            tmp_list.append(list_a[0])
            del list_a[0]
        else:
            tmp_list.append(list_b[0])
            del list_b[0]
    tmp_list.extend(list_a)
    tmp_list.extend(list_b)
    return tmp_list


def gen_list(num = 10, start=1, end=100, step=1):
    list = []
    count = 0
    while count < num:
        list.append(random.randrange(start, end, step))
        count += 1
    list.sort()
    return list

# 随机生成两个队列
list_a = gen_list(20)
list_b = gen_list(35)
print('随机生成两个列表，并排序')
print('列表list_a', list_a)
print('列表list_a', list_b)
print()

# 合并排序
mix_list = loop_merge_sort(list_a, list_b)
print('合并后的列表', mix_list)