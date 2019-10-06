# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:26:09 2019

@author: witty
"""

# 动态规划法 
## 加法几乎不占用时间，预先存好变量关系，再运算。
output = [None]*200000
def FibonacciNew(n):
    result = output[n]
    if output[n] == None:
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = FibonacciNew(n-1)+FibonacciNew(n-2)
        output[n] = result
    return result

FibonacciNew(4)