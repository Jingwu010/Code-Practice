class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        
        mod = 10 ** 9 + 7
        grid = [[[0 for k in range(N+1)] for j in range(n)] for i in range(m)]
        flag = [[[0 for k in range(N+1)] for j in range(n)] for i in range(m)]

        def dfs(idxI, idxJ, step):
            if step == 0:
                return

            increI = [1, 0, -1, 0]
            increJ = [0, 1, 0, -1]

            # loop through 4 directions
            for k in range(4):
                newI = idxI + increI[k]
                newJ = idxJ + increJ[k]

                # if the ball is out of boundary
                if newI >= m or newI < 0:
                    grid[idxI][idxJ][step] += 1
                    continue
                if newJ >= n or newJ < 0:
                    grid[idxI][idxJ][step] += 1
                    continue

                # if the next state has not been recorded
                if flag[newI][newJ][step-1] == 0:
                    # dfs explores next state 
                    dfs(newI, newJ, step-1)

                # The sum of possible ways of all next states
                grid[idxI][idxJ][step] += (grid[newI][newJ][step-1] % mod)
            
            # mark the current state as recorded
            flag[idxI][idxJ][step] = 1

        dfs(i, j, N)
        return grid[i][j][N] % mod

# print(Solution().findPaths(1,3,3,0,1))
# print(Solution().findPaths(2,2,2,0,0))
# print(Solution().findPaths(3,2,3,1,1))