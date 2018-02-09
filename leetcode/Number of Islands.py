class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        grid = [[int(c) for c in string] for string in grid]

        def explore(grid, idx, vis):
        	x, y = idx
        	dirx = [1, 0, -1, 0]
        	diry = [0, 1, 0, -1]
        	if grid[x][y] == 1 and not vis[x][y]:
        		vis[x][y] = True
        		for i in range(len(dirx)):
        			dx = x + dirx[i]
        			dy = y + diry[i]
        			if dx < 0 or dx >= len(grid):
        				continue
        			if dy < 0 or dy >= len(grid[0]):
        				continue
        			if vis[dx][dy]: continue
        			explore(grid, (dx, dy), vis)
        	return 1

        vis = [[False for c in string] for string in grid]
        result = 0
        for i in range(len(grid)):
        	for j in range(len(grid[i])):
        		if grid[i][j] == 1 and not vis[i][j]:
        			result += explore(grid, (i, j), vis)
        return result

print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
))
print(Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
))
print(Solution().numIslands([["1","0","1","1"],["0","1","0","1"],["1", "0", "1","1"]]))
print(Solution().numIslands([["1","1"],["0","1"]]))
# 1011
# 0101
# 1011

