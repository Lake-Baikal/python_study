#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :03.var_example.py
# @Time      :2024/03/16 10:49:34
# @Author    :Baikal
""" 
1.不论是使用那种高级程序语言编写程序,变量都是其程序的基本组成单位
2.变量有基本三要素(类型+名称+值)
!3.变量相当于内存中一个数据存储空间的表示
!4.你可以把变量看作一个房间的门牌号,通过门牌号我们可以找到房间,而通过变量名可以访问到变量的值
"""

"""
!内存(Memory)是计算机的重要部件,它用于暂时存放CPU中的运算数据,以及与硬盘外部存储交换的数据.
!他是外存与CPU进行沟通的桥梁, 计算机中所有程序的允许都在内存中进行.

"""
# 定义了一个变量，变量名称a,变量值是1，1是int类型(整数类型)
a = 1
# 定义了一个变量，变量名称b,变量值是2，2是int类型(整数类型)
b = 2
# 变量b的值修改为8,变量b的值为8,8是int类型(整数类型)
b = 8
# 输出变量的值
print("a的值是", a, "\n a的类型是", type(a))
print("b的值是", b, "\n b的类型是", type(b))

# 变量使用的基本步骤
# ?定义变量
a = 10
# 使用
print(a)
# 变量的错误使用
# print(c)
# c = 33
# !变量一定要先定义后使用,不能先使用后定义，否则会提示not defined
