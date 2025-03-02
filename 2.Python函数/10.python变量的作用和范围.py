#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :10.python变量的作用和范围.py
# @Time      :2024/04/14 14:39:35
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
"""
!全局变量和局部变量
全局变量:在整个程序范围内都可以访问,定义在函数外,拥有全局作用域的变量
局部变量:只能在其被声明的函数范围内访问,定义在函数内部,拥有局部作用域的变量
"""
# n1就是全局变量
# n1 = 100

# # 定义函数
# def f1():
#     # n2就是局部变量
#     n2 = 200
#     print(n2)
#     # 可以访问全局变量n1
#     print(n1)

# # 调用
# f1()
# # 访问全局变量n1
# print(n1)
# # 不能访问局部变量n2
# # print(n2)

# !注意事项:
# !1.未在函数内部重新定义n1,那么默认使用全局变量n1
# n1 = 100

# def f1():
#     print(n1)

# f1()

# !在函数内部重新定义了n1,那么根据就近原则,使用的就是函数内部重新定义的n1
# n1 = 100

# def f1():
#     # n1重新定义了
#     n1 = 200
#     print(n1)

# f1()
# print(n1)

# !在函数内部使用global关键字,可以标明指定使用全局变量
n1 = 100


def f1():
    # global关键字,可以标明指定使用全局变量n1
    # 此时使用全局变量n1但是n1的值发生改变为200
    global n1
    n1 = 200
    print(n1)  # 200


f1()
print(n1)  # 200
