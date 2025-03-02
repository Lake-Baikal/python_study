#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :27.if嵌套分支.py
# @Time      :2024/03/29 23:06:57
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
"""
!嵌套分支:在一个分支结构中又嵌套了另一个分支
!里面的分支结构称为内分支,外面的分支结构称为外分支
!规范:不要超过三层(可读性不好)
语法:
if:
   if:
      #if-else...
   else:
      #if-else...
"""

# 案例:参加初赛,如果初赛成绩大于8.0进入决赛,否则提示淘汰,并且根据性别提示进入男子组或者女子组.输入成绩和性别,进行判断和输出信息.
# 思路分析
# 1.输入成绩和性别，input()函数,float类型
# 2.score接收成绩,然后使用if-else判断是否进入决赛
# 3.如果进入决赛在接收性别在使用if-else判断是进入男子组还是女子组

# score = float(input('请输入您的成绩'))
# if score > 8.0:
#     gender = input("请输入您的性别男|女")

#     if gender == "男":
#         print("进入男子组")
#     else:
#         print("进入女子组")
# else:
#     print("成绩目前不达标,淘汰")

# 案例2:出票系统,根据淡旺季的月份和年龄, 打印票价.
"""
4-10月是旺季
  成人(18-60):60元
  儿童(<18):半价
  老人(>60):3/1
淡季:
成人:40
老人:20
"""
# 思路分析
# 定义两个变量month,age接收月份和用户年龄
# 淡季和旺季使用if-else双分支判断
# 如果是旺季使用多分枝来判断给出相应价格
# 5.如果是淡季,使用双分支判断age，给出相应价格
month = int(input("请输入月份"))
age = int(input("请输入年龄"))
if 4 <= month <= 10:
    print('旺季')
    if age >= 60:
        print("价格为20")
    elif age >= 18:
        print("价格为60")
    else:
        print("票价为30")

else:
    print("淡季")
    if 18 <= age <= 60:
        print("成人票价40")
    else:
        print("票价20")
