#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 5:11 PM
# @Author  : LXR
# @File    : oop.py
# @Software: PyCharm
class DemoClass:
    def __init__(self,name):
        self.name = name
    def lucky(self):
        s = 0
        for c in self.name:
            s += ord(c) % 100
        return s
dc1 = DemoClass("刘珀霖")
dc2 = DemoClass("刘小溶")
print(dc1.name,"的幸运数字为：",dc1.lucky())
print(dc2.name,"的幸运数字为：",dc2.lucky())

