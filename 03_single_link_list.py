#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 2:12 PM
# @Author  : LXR
# @File    : 03_single_link_list.py
# @Software: PyCharm

# 单链表的实现
class Node(object):
    '''节点'''

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class Single_link_list(object):
    def __init__(self, node=None):
        self.__head = None

    def is_empty(self):
        # 链表是否为空
        # cur游标，用来遍历节点
        return self.__head == None
        # 计数
        count = 0
        if  cur != None:
            count += 1
            cur = cur.next
        else:
            return count


    def length(self):
        # 链表长度
        cur = self.__head
        count = 1
        while cur != None:
            cur = cur.next
            count += 1
        return count



    def travel(self):
        # 遍历链表
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next

    def add(self, item):
        # 链表头部添加元素，"头插法"
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = None
        else:
            node.next = self.__head
            self.__head = node

    def append(self, item):
        # 链表尾部添加，"尾插法"
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node  # 游标指针next指向节点

    def insert(self, pos, item):
        # 指定位置添加元素
        '''param：pos从0开始
        '''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            while count < (pos - 1):
                pre = pre.next
                count += 1
            # 当循环退出后pre指向pos-1位置
            node.next = pre.next
            pre.next = node

    def remove(self, item):

        # 删除节点
        pass

    def search(self, item):

        # 查找节点是否存在
        pass


if __name__ == '__main__':
    ls = Single_link_list()
    print(ls.is_empty())
    print(ls.length())

    ls.append(1)
    print(ls.is_empty())
    print(ls.length())
    ls.append(2)
    ls.add(6)
    ls.append(3)
    ls.append(4)
    #6 1 2 3 4
    ls.insert(-1,7)#7 6 1 2 3 4
    ls.insert(4,8) #7 6 1 2 8 3 4
    ls.insert(10,10)# 7 6 1 2 8 3 4 10
    ls.travel()
