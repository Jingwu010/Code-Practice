#!/bin/python3

import sys

def lilysHomework(n, ar):
    # Complete this function
    chaos = 0
    newAr = sorted(ar)
    for i, value in enumerate(ar):
    	check = newAr[i]
    	if value != check:
    		chaos += 1
    if chaos % 2 == 0:
    	return (int)(chaos/2)
    return (int)(chaos/2 +1)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = lilysHomework(n, ar)
print(result)

"""

6512

1562
1265
1256

"""