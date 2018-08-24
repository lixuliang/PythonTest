# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 20:19:11 2018

@author: hp
"""

'''
1.给定一个升序列表和一个整数,返回该整数在列表中的下标范围.例如:列表[1,2,3,3,3,4,4,5],若查找3,则返回(2,4),查找1,返回(0,0)
'''
def binary_list_search(data, val):
    low = 0 
    high = len(data) - 1
    while low <= high:
        mid = (low+high) //2
        #如果找到val的值
        if data[mid] == val:
            #创建两个指针
            left = mid
            right = mid
            #如果左边指针的值等于val,则指针向左移
            while left >= 0 and data[left] == val:
                left -=1
            #右边指针的值等于val,则指针向右移
            while right <= high and data[right] == val:
                right += 1
            return (left+1, right-1)
        elif data[mid] < val:
            low = mid + 1
        else:
            high = mid - 1

'''
2.给定一个列表和一个整数,设计算法找到两个数的下标,使得两个数之和为给定的整数,保证仅有一个结果.例如列表[1,2,5,4]与目标整数3,结果为(0,1)
时间复杂度：O(n)
'''
def sum_lists(data, val):
    num = len(data)
    max_loc = max(max(data), val)
    a = [None for i in range(max_loc)]
    for i in range(num):
        a[data[i]] = i
        if (a[val - data[i]] != None) :
            return (a[data[i]],a[val - data[i]])
        
'''
3.现在有一个列表,列表中数的范围在0-100之间,列表的长度大概为100万,设计算法在O(n)的复杂度内将列表进行排序
'''
import random

def count_sort(data, max_val):
    res = [0 for i in range(len(data))]
    count = [0 for i in range(max_val+1)]
    for i in data:
        count[i] += 1
    loc = 0
    for num,n in enumerate(count):
        for j in range (n):
            res[loc] = num
            loc += 1
    return (res)

'''
4.现在有n个数(n>10000),设计算法,按照大小顺序得到前10大的数
'''
def insert (data,i):
    tmp = data[i]
    j = i - 1
    while j >= 0 and data[j] > tmp:
        data[j+1] = data[j]
        j -= 1
    data[j+1] = tmp

def insert_sort(data):
    for i in range(1,len(data)):
        insert(data,i)

def topk(data,k):
    top = data[0:k+1]
    insert_sort(top)
    for i in range(k+1,len(data)):
        top[k] = data[i]
        insert(top, k)
    return (top[:-1])

if __name__ == '__main__':
    lists = [1,2,3,4,5,5,5,6]
    print (binary_list_search(lists,4))
    
    lists2 = [1,2,5,4,5,6,7,8]
    print (sum_lists(lists2, 9))
    
    lists3 = [random.randint(0,100) for x in range(10000)]
    res = count_sort(lists3,100)
    
    lists4 = list(range(10000))
    random.shuffle(lists4)
    print(topk(lists4, 10))
