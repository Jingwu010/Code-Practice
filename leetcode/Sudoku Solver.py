class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        blocks = [(0,0), (0,3), (0,6),\
        		  (3,0), (3,3), (3,6),\
        		  (6,0), (6,3), (6,6)]

        # return valid nums for a given position in soduku
        def retValid(i, j):
        	numSet = set(range(1,10))
        	for _i in range(9):
        		if board[_i][j] in numSet:
        			numSet.remove(board[_i][j])
        	for _j in range(9):
        		if board[i][_j] in numSet:
        			numSet.remove(board[i][_j])
        	li = (i // 3) * 3
        	lj = (j // 3) * 3
        	for _i in range(3):
        		for _j in range(3):
        			if board[li+_i][lj+_j] in numSet:
        				numSet.remove(board[li+_i][lj+_j])
        	return numSet

        def dfs(dirc, key, board):
        	if dirc == 0:
        		i = key
        		for _j in range(9):
        			if board[i][_j] != '.':
        				continue
        			for v in retValid(i, _j):
        				board[i][_j] = v
        				updateDirections(i, _j, directions, add = 1)
        				dfs(i, j, dir, board)
        				updateDirections(i, _j, directions, add = -1)
        				board[i][_j] = '.'


        def calDirections():
        	directions = [[0 for j in range(9)] for i in range(3)]
        	for i in range(9):
        		for j in range(9):
        			updateDirections(i, j, directions, add = 1)
        	return directions

        def updateDirections(i, j, directions, add = 1):
        	if board[i][j] != '.':
        		k = blocks.index(((i//3)*3, (j//3)*3))
        		directions[0][i] = (directions[0][i] + add * 1) % 9
        		directions[1][j] = (directions[0][i] + add * 1) % 9
        		directions[2][k] = (directions[0][i] + add * 1) % 9

        def chooseDirections(directions):
        	maxs = max(max(Ai) for Ai in A)
        	for dirc in range(3):
        		for key in range(9):
        			if directions[dirc][key] == maxs:
        				return dirc, key
        	return None
