#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time, threading

# def loop():
#     print ('线程 %s 正在运行...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n += 1
#         print('线程 %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('线程 %s 结束' % threading.current_thread().name)
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop)
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


# 多线程局部变量冲突

# 假定这是你的银行存款:
# balance = 0
#
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000):
#         change_it(n)
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

print(multipro.cpu_count())