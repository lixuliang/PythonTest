# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 22:29:58 2018

@author: hp
"""

'''
约瑟夫问题
n个人围成一个圈，每个人分别标注为1、2、...、n，要求从1号从1开始报数，报到k的人出圈，接着下一个人又从1开始报数，如此循环，直到只剩最后一个人时，该人即为胜利者。例如当n=10,k=4时，依次出列的人分别为4、8、2、7、3、10，9、1、6、5，则5号位置的人为胜利者。给定n个人，请你编程计算出最后胜利者标号数。
'''

#列表
def Joseph_1(n, m):
    people = [i for i in range(1,n+1)]
    x = 0
    while len(people)>0:
        # 每次取出对总人数的余数就是要找的人 
        dead_loc = (x+m-1)%len(people)
        # yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值
        # 下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行
        yield people.pop(dead_loc)
        x = dead_loc

#链表
class LinkList:
    #自定义链表实现类
    class Node:
        def __init__(self,item=None):
            self.item = item
            self.next = None

    class LinkListIterator:
        def __init__(self,node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
        def __iter__(self):
            return self

    def __init__(self,iteratbe=None):
        self.head = LinkList.Node(0)
        self.tail = self.head
        self.extend(iteratbe)
    
    #链表添加
    def append(self,obj):
        s = LinkList.Node(obj)
        self.tail.next = s
        self.tail = s
    
    #链表扩展
    def extend(self,iterable):
        for obj in iterable:
            self.append(obj)
        self.head.item += len(iterable)

    def remove_nth_node(self,node,m):
        #删除链表第n个元素
        for i in range(m-2):
            node = node.next
        p = node.next
        node.next = p.next
        self.head.item -= 1
        return p


    def __iter__(self):
        return self.LinkListIterator(self.head.next)

    def __len__(self):
        return self.head.item

    def __str__(self):
        return '<<'+", ".join(map(str,self)) +">>"

def Joseph_link(n,m):
    people = LinkList([i for i in range(1,n+1)])
    people.tail.next = people.head.next
    x = people.head.next
    while len(people)>0:
        p = people.remove_nth_node(x,m)
        x = p.next
        yield p.item      

print (list(Joseph_1(9,4)))
print(list(Joseph_link(9,4)))  
