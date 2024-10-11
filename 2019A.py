#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:41:18 2024

@author: mdiktushar
"""


t = int(input())

while t:
    
    n = int(input())
    arr = input()
    arr = list(map(int, arr.split()))

    even = []
    odd = []
    
    
    for i in range(n):
        if i % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    
    
    evenSize = len(even)
    oddSize = len(odd)
    if evenSize and oddSize:
        evenMax = max(even)
        oddMax = max(odd)
        
        evenSum = evenSize + evenMax;
        oddSum = oddSize + oddMax;
        
        print(max(evenSum, oddSum))
    else:
        evenMax = max(even)
        evenSum = evenSize + evenMax;
        print(evenSum)
    
    t -= 1