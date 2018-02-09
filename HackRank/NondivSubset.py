# https://www.hackerrank.com/challenges/non-divisible-subset

def nondivSubset(arr, k):
	arr = list(map(lambda arr_i: int(arr_i), arr))
	arr = list(map(lambda arr_i: arr_i % k, arr))
	ardic = dic(map(lambda arr_i: ))
	print(arr)

s = input().strip().split()
n, k = int(s[0]), int(s[1])
arr = list(input().strip().split())
print(nondivSubset(arr, k))

