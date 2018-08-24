# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 17:24:03 2018

@author: hp

Python常用排序算法：从小到大排序
"""

import numpy as np
import pandas as pd

'''
1.冒泡排序
思路:将左右元素两两相比较，将值小的放在列表的头部，值大的放到列表的尾部
效率:O(n²)
'''
def bubble_sort (data):
    inputdata = data.copy()
    for i in range(len(inputdata)-1):
        for j in range(len(inputdata)-i-1):
            if inputdata[j] > inputdata[j+1]:
                inputdata[j],inputdata[j+1] = inputdata[j+1],inputdata[j]
    return (inputdata)

'''
2.选择排序
思路:遍历列表，挑出一个最小的数字，放到列表的第一个索引位。在一趟遍历剩余列表中的最小数，继续放置。
效率:O(n²)
'''
def select_sort (data):
    inputdata = data.copy()
    for i in range(len(inputdata)-1):
        mim_loc = i
        for j in range(i+1,len(inputdata)):
            if inputdata[j] < inputdata[mim_loc]:
                mim_loc = j
        if mim_loc != i:
            inputdata[mim_loc],inputdata[i] = inputdata[i],inputdata[mim_loc]
    return (inputdata)

'''
3.插入排序
思路：列表分为有序区和无序区两个部分，最初有序区只有一个元素。每次从无序区选择一个元素，插入到有序区的位置，直到无序区变空
效率:O(n²)
'''
def insert_sort (data):
    inputdata = data.copy()
    for i in range(1, len(inputdata)):
        temp = inputdata[i]
        j=i-1
        while j>=0 and temp < inputdata[j]:
            inputdata[j+1] = inputdata[j]
            j=j-1
        inputdata[j+1]=temp
    return (inputdata)

'''
4.快速排序
思路:取一个元素P,使元素P归位,列表被P分为两个部分,左边的比P小,右边比P大,递归完成排序。
效率:O(nlogn)
'''
def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid-1)
        quick_sort(data, mid+1, right)

def partition(data, left, right):
    temp = data[left]
    while left < right:
        #如果遇到比tmp大的数,右指针向左移动,否则将右边的值放到左边
        while left < right and data[right] >= temp:
            right -= 1
        data[left] = data[right]
        #如果遇到比tmp小的数,左指针向右移动,否则将左边的值放到右边　
        while left < right and data[left] <= temp:
            left += 1
        data[right] = data[left]
    data[left] = temp
    return (left)

'''
5.堆排序
思路:建立堆,得到堆顶元素为最大元素,去掉堆顶元素,将堆的最后一个元素放到堆顶,此时通过一次调整使得堆有序.堆顶元素为第二大元素,重复步骤直到堆变空
效率:O(nlogn)
若想得到升序，则建立大顶堆，若想得到降序，则建立小顶堆
'''
def adjust_heap (lists, root, size):
    left = 2*root + 1
    right = 2*root + 2
    larger = root
    if left < size and lists[larger] < lists[left]:
        larger = left
    if right < size and lists[larger] < lists[right]:
        larger = right
    if larger != root:
        lists[larger],lists[root] = lists[root],lists[larger]
        adjust_heap(lists, larger, size)

def build_heap(lists, size):
    for i in range(size//2-1,-1,-1):
        adjust_heap(lists, i, size)

def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(size-1,-1,-1):
        lists[0],lists[i] = lists[i],lists[0]
        adjust_heap(lists,0,i)
        
'''
6.归并排序
思路：使用递归的方式，将列表越分越小，直至一个元素，然后将列表组合成一个有序的列表
效率:O(nlogn)
'''
def merge(left, right):
    i,j=0,0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return (result)

def merge_sort(data):
    if len(data) <= 1:
        return (data)
    num = len(data) // 2
    left = merge_sort(data[:num])
    right = merge_sort(data[num:])
    return (merge(left, right))

'''
7.希尔排序
思路:首先取一个整数d1=n/2,将列表中的元素分成d1个组,每组相邻两元素的之间的距离为d1,在各组内直接进行插入排序.取第二个整数d2=d1/2,重复上述的分组过程,直到di=1,然后在同一组内进行插入排序
效率:O(1.3n)
'''
def shell_sort(data):
    inputdata = data
    gap = len(inputdata)//2
    while gap > 0:
        for i in range(gap, len(inputdata)):
            tmp = inputdata[i]
            j = i - gap
            while j >= 0 and tmp < inputdata[j]:
                inputdata[j+gap] = inputdata[j]
                j -= gap
            inputdata[j+gap] = tmp
        gap //= 2
    return (inputdata)

if __name__ == '__main__':
    x = np.random.rand(100)
    y1 = bubble_sort (x)
    y2 = select_sort (x)
    y3 = insert_sort (x)
    
    y4 = x.copy()
    quick_sort(y4, 0, len(x2)-1)
    
    y5 =x.copy()
    heap_sort(y5)
    
    tmp = list(x.copy())
    y6 = merge_sort(tmp)
    
    y7 = shell_sort(x)