#!/bin/python3

import sys

def gridSearch(G, P):
    upperI = len(G)-len(P)+1
    upperJ = len(G[0])-len(P[0])+1
    i = 0
    j = 0
    while i < upperI:
        addI = 1
        j = 0
        while j < upperJ:
            addJ = 1
            flag = True
            for k in range(len(P)):
                if flag is False:
                    break
                for l in range(len(P[k])):
                    if flag is False:
                        break
                    if G[i+k][j+l] != P[k][l]:
                        if k == 0: addJ = max(addJ, l+1)
                        flag = False
            if flag is True:
                return "YES"
            j += addJ
        i += addI
    return "NO"
    # Complete this function

t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)
    print(gridSearch(G, P))
