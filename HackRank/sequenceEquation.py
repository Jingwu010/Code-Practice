#!/bin/python3

import sys

def sequenceEquation(n, ar):
    # Complete this function
    ans = []
    for i in range(1, n+1):
        print(i)
        x1 = ar.index(i) + 1
        x2 = ar.index(x1) + 1
        ans.append(x2)
    return ans

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sequenceEquation(n, ar)
for ele in ans:
    print(ele)
