# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 21:40:20 2018

@author: hp
"""

maze=[
      [1,1,1,1,1,1,1,1,1,1],
      [1,0,0,1,0,0,0,1,0,1],
      [1,0,0,1,0,0,0,1,0,1],
      [1,0,0,0,0,1,1,0,0,1],
      [1,0,1,1,1,0,0,0,0,1],
      [1,0,0,0,1,0,0,0,0,1],
      [1,0,1,0,0,0,1,0,0,1],
      [1,0,1,1,1,0,1,1,0,1],
      [1,1,0,0,0,0,0,0,0,1],
      [1,1,1,1,1,1,1,1,1,1],
      ]
dirs = [lambda x,y:(x+1,y),
        lambda x,y:(x-1,y),
        lambda x,y:(x,y-1),
        lambda x,y:(x,y+1)]

'''
一.列表:在其他语言中成为数组,是一种基本的数据结构类型
1.列表在内存中以一块连续的空间存放,列表中存放的是每个元素的引用
2.新增:insert,append;删除:remove,pop;修改:根据索引修改;遍历,查找
3.insert O(n),append O(1),remove O(n),pop O(1),修改 O(1),遍历 O(n),查找 O(n)
'''

'''
二.栈:栈是一种数据集合,可以理解为只在一端进行插入或删除操作的列表
特点:后进先出
基本操作:进栈:push,出栈:pop,取栈顶元素:gettop
在python中只需要用列表就可以实现栈
'''

# 栈的应用:括号匹配问题
def check_kuohao(s):
    stack = []
    for char in s:
        #判断字符串中如果有括号则放入栈中
        if char in {'(','[','{'}:
            stack.append(char)
        #如果匹配到括号,如果栈不为空,且栈顶有括号与之匹配,则将该元素出栈
        elif char == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif char == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif char == '}':
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                return False
    #如果栈为空表示所有括号匹配成功,否则失败
    if len(stack) == 0:
        return True
    else:
        return False

'''
三.队列:队列是一种数据集合,仅允许在列表的一端进行插入,另一端进行删除.
插入队列的一端称为队尾,动作称为入队;删除队列的一端称为对头,动作称为出队;性质:先进先出
算法实现:环形队列;当队尾指针front==Maxsize+1时,在前进一个位置就自动到0;实现方式求余运算
'''

'''
四.链表:链表中每一个元素都是一个对象,每个对象称为一个节点,包含数据域和指针域,通过各个节点的相互链接,最终串成一个链表
'''
class Node(object):
    #定义节点
    def __init__ (self,item):
        self.item = item
        self.next = None

def travel_sal(head):
    #遍历
    curNode = head
    while curNode is not None:
        print (curNode.item)
        curNode = curNode.next

def createLinkListF(data):
    # 头插法
    l = Node()
    for num in data:
        s = Node(num)
        s.next = l.next
        l.next = s
    return l

'''
五.集合和字典
集合和字典是基于哈希表来对元素进行查找
哈希表是一种线性存储结构,通过每个对象k的关键字作为自变量,通过一个哈希函数h(k),把k映射到下标h(k)处,并将该对象存储到这个位置
使用哈希表存储字典,通过哈希函数将字典的key映射为下标.
'''

'''
练习:给一个二维列表,表示迷宫,(0,通,1,阻) 给出算法,求出走出迷宫的路径
思路:从上一个节点开始,任意找下一个能走的节点,当找到不能走的节点时,退回到上一个节点,寻找是否有其他方向的点
方法:创建一个栈,首先将入口的位置进栈,当栈不空时候循环,获取栈顶元素,寻找下一个可走的相邻方块,如果找不到可走的相邻方块,说明当前是死路,
     进行回溯(将当前的点出栈,查看前面的点是否还有其他出路),体现深度优先的思想
'''
def mpath(x1,y1,x2,y2):
    stack = []
    stack.append((x1,y1))
    while len(stack) > 0:
        curNode = stack[-1]
        #找到终点
        if curNode[0] == x2 and curNode[1] == y2:
            for p in stack:
                print (p)
            return True
        for dir in dirs:
            nextNode = dir(*curNode)
            #print ('---\n',nextNode,'\n---\n')
            #此路通的
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                #标记已走过的方格
                maze[nextNode[0]][nextNode[1]] = -1
                break
        else:
        #处理遍历失败
            maze[nextNode[0]][nextNode[1]] = -1
            stack.pop()
    return False

if __name__ == '__main__':
    print(check_kuohao('ad{sda[ds]ds}]'))

    a = Node(10)
    b = Node(20)
    c = Node(30)
    a.next = b
    b.next = c
    print (a.item)
    print (a.next.item)
    print(a.next.next.item)
    
    mpath (1,1,8,8)