#!/bin/python3

import sys

def howManyToInvite(A, B, a):
	return a*A/B
    # Return the number of people Leha should invite to his party

if __name__ == "__main__":
    A, B, a = input().strip().split(' ')
    A, B, a = [int(A), int(B), int(a)]
    b = howManyToInvite(A, B, a)
    print(b)
