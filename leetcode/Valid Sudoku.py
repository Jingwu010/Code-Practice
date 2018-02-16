class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        class sudokuObj:
        	def __init__(self):
        		self.h = False
        		self.v = False
        		self.b = False

        def checkHorizontal(i, j, flag):
        	if flag[i][j].h:
        		return True
        	numSet = set()
        	for _j in range(9):
        		if board[i][_j] == '.':
        			continue
        		if board[i][_j] in numSet:
        			return False
        		numSet.add(board[i][_j])
        	for _j in range(9):
        		flag[i][_j].h = True
        	return True

        def checkVertical(i, j, flag):
        	if flag[i][j].v:
        		return True
        	numSet = set()
        	for _i in range(9):
        		if board[_i][j] == '.':
        			continue
        		if board[_i][j] in numSet:
        			return False
        		numSet.add(board[_i][j])
        	for _i in range(9):
        		flag[_i][j].v = True
        	return True

        def checkBlock(i, j, flag):
        	if flag[i][j].b:
        		return True
        	li = (i // 3) * 3
        	lj = (j // 3) * 3
        	numSet = set()
        	for _i in range(3):
        		for _j in range(3):
        			if board[li + _i][lj + _j] == '.':
        				continue
        			if board[li + _i][lj + _j] in numSet:
        				return False
        			numSet.add(board[li + _i][lj + _j])
        	for _i in range(3):
        		for _j in range(3):
        			flag[li + _i][lj + _j].b = True
        	return True

        flag = [[sudokuObj() for y in board[0]] for x in board]
        
        for i in range(9):
        	for j in range(9):
        		if not (checkHorizontal(i, j, flag) and \
        				checkVertical(i, j, flag) and \
        				checkBlock(i, j, flag)):
        			return False

        return True
