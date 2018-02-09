from time import sleep

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
        	return []
        nrow = len(matrix)
        ncol = len(matrix[0])
        vis = [[False for j in range(ncol)] for i in range(nrow)]
        dirx = [0, 1, 0, -1]
        diry = [1, 0, -1, 0]
        idxx, idxy = 0, 0
        result = []
        while len(result) != nrow * ncol:
	        for i in range(4):
	        	incx = dirx[i]
	        	incy = diry[i]
	        	while True:
	        		if not vis[idxx][idxy]:
		        		result.append(matrix[idxx][idxy])
		        		vis[idxx][idxy] = True
	        		if idxx + incx < 0 or idxx + incx >= nrow:
	        			break
	        		if idxy + incy < 0 or idxy + incy >= ncol:
	        			break
	        		if vis[idxx + incx][idxy + incy]:
	        			break
	        		idxx += incx
	        		idxy += incy
        return result

print(Solution().spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))
print(Solution().spiralOrder([[]
]))
print(Solution().spiralOrder([
]))