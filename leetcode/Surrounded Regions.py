class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        def pprint():
            for i in range(n):
                for j in range(m):
                    print(board[i][j], end=' ')
                print()

        def dfs(i, j, value):
            if i >= n or i < 0:
                return
            if j >= m or j < 0:
                return

            if visited[i][j] == 1:
                return
            visited[i][j] = 1

            if board[i][j] == 'X':
                return

            # if the 'O' resides on the border 
            if i == n-1 or i == 0:
                value[0] = board[i][j]
            if j == m-1 or j == 0:
                value[0] = board[i][j]

            # dfs its adjacent cells
            dfs(i+1, j, value)
            dfs(i, j+1, value)
            dfs(i-1, j, value)
            dfs(i, j-1, value)

            # in order to keep all the recursive assignment update to the same value
            board[i][j] = value[0]

        try:
            n = len(board)
            m = len(board[0])
            pprint()
            print()
            visited = [[0 for j in range(m)] for i in range(n)]
            for i in range(n):
                for j in range(m):
                    dfs(i, j, ['X'])
            
            pprint()
            return
        except:
            return
        
# Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
# Solution().solve([["X","X","X","X","X"],["X","O","O","O","X"],["X","O","X","X","X"],["O","O","X","O","X"],["X","X","X","O","X"]])
# Solution().solve([["O","O","O","O","O"],["O","O","X","X","O"],["O","X","O","X","O"],["O","X","O","X","O"],["O","O","O","O","O"]])
# Solution().solve([["X","X","X","O","X"],["X","X","O","O","X"],["X","X","X","X","X"],["X","O","O","X","O"],["X","O","X","X","X"]])
Solution().solve([["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]])

