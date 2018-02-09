#!/bin/python3

import sys

def sockMerchant(n, ar):
    # Complete this function
    sortedar = sorted(ar)
    num = 0
    highest = len(sortedar)-1
    i = 0
    while i < highest:
    	if sortedar[i] == sortedar[i+1]:
    		num += 1
    		i += 1
    	i += 1
    return num

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
