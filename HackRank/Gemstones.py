import sys

def gemstones(arr):
    # Complete this function
    num = 0
    stanStr = "abcdefghijklmnopqrstuvwxyz"
    for char in stanStr:
    	flag = True
    	for mystr in arr:
    		if flag is False:
    			break
    		if char not in mystr:
    			flag = False
    	if flag is True:
    		num += 1
    return num

n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
   arr_t = str(input().strip())
   arr.append(arr_t)
result = gemstones(arr)
print(result)
