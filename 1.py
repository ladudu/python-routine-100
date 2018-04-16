# -*- coding: UTF-8 -*-
"""
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
"""
for a in range(100,999):
    flag = 1
    b,c,d = str(a)
    if b != c and b != d and c !=d :
        if b > '0' and b < '5' :
            if c > '0' and c < '5' :
                if d > '0' and d < '5':
                    print(a)
"""
a = [1,2,3,4]
for b in range(0,4):
    for c in range (0,4):
        for d in range(0,4):
            if b != c and b != d and c != d:
                print(str(a[b])+str(a[c])+str(a[d]))