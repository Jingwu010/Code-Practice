class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def searchSortedArr(arr, target):
        	# print(arr, target)
        	if len(arr) == 0:
        		return False
        	if len(arr) <= 2:
        		return target in arr

        	mid = len(arr)//2
        	if arr[mid] == target:
        		return True
        	if arr[mid] < target:
        		return searchSortedArr(arr[mid+1:], target)
        	else:
        		return searchSortedArr(arr[:mid], target)


        if not matrix:
        	return False
        x = len(matrix)
        y = len(matrix[0])
        i, j = x-1, y-1
        for step in range(min(x,y)):
        	if matrix[i][j] == target:
        		return True
        	elif matrix[i][j] < target:
        		return False
        	else:
        		if matrix[0][j] <= target: # matrix[:i][j]
        			if searchSortedArr([matrix[_i][j] for _i in range(i)], target):
        				return True
        		if matrix[i][0] <= target:
        			if searchSortedArr(matrix[i][:j], target):
        				return True
        	i -= 1
        	j -= 1
        return False

print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
print(Solution().searchMatrix([[1,2,3,4,100],[2,3,4,5,101],[3,4,5,6,102],[4,5,6,7,103]], 1))
print(Solution().searchMatrix([[1,2,3,4,100],[2,3,4,5,101],[3,4,5,6,102],[4,5,6,7,103]], 4))
print(Solution().searchMatrix([[1,2,3,4,100],[2,3,4,5,101],[3,4,5,6,102],[4,5,6,7,103]], 20))
print(Solution().searchMatrix([[1,2,3,4,100]], 1))
print(Solution().searchMatrix([[1],[2],[3],[4],[100]], 2))
print(Solution().searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 1))
# 20

# 1 2 3 4 100
# 2 3 4 5 101
# 3 4 5 6 102
# 4 5 6 7 103