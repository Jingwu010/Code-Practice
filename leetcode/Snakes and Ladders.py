class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        
        # 2 <= board.length = board[0].length <= 20
        # board[i][j] is between 1 and N*N or is equal to -1.
        # The board square with number 1 has no snake or ladder.
        # The board square with number N*N has no snake or ladder.
        # 

        def get_num(n, num):
            x_dirs = [-1, 1]
            end = 0
            while num > end:
                end += n
            y = end // n
            x_delta = x_dirs[y % 2]
            x = (n - 1) * (y % 2) - x_delta * (end - num)
            return n - y, x

        def bfs(num, steps, n, board, depth):
            queue = [(False, num, depth)]
            while queue:
                # print('exploring', queue[0])
                jump, cur_num, cur_depth = queue.pop(0)
                if cur_num > n * n:
                    continue
                i, j = get_num(n, cur_num)
                # if the node has been explored
                if steps[i][j][jump] != -1:
                    continue
                steps[i][j][jump] = cur_depth

                # if there is an short path to another node
                if board[i][j] != -1 and jump:
                    # print('jump to ', get_num(n, board[i][j]), board[i][j])
                    queue.append((False, board[i][j], cur_depth))

                # roll the dice and explore all possible moves upon that node
                else:
                    for i in range(1, 7):
                        queue.append((True, cur_num+i, cur_depth+1))

                queue.sort(key=lambda a: a[2])

        if board:
            n = len(board)
        steps = [[[-1 for k in range(2)] for j in range(n)] for i in range(n)]
        bfs(1, steps, n, board, 0)

        i, j = get_num(n, n*n)
        # print(steps[i][j])
        if sum([-1 == elem for elem in steps[i][j]]) == 2:
            return -1
        elif sum([-1 == elem for elem in steps[i][j]]) == 1:
            return steps[i][j][0] if steps[i][j][0] != -1 else steps[i][j][1]
        else:
            return min(steps[i][j])

# print(Solution().snakesAndLadders([
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,35,-1,-1,13,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,15,-1,-1,-1,-1]]))

print(Solution().snakesAndLadders([
[-1,36,35,34,33,32],
[26,27,28,29,30,31],
[25,24,23,22,21,20],
[14,15,16,17,18,19],
[13,12,11,10,9,8],
[-1,3,4,5,6,7]]))

# print(Solution().snakesAndLadders([
# [-1,-1,-1,-1],
# [-1,-1,-1,-1],
# [-1,-1,-1,-1],
# [-1,3,11,-1]]))

# print(Solution().snakesAndLadders([
# [-1,-1,-1,-1],
# [-1,-1,16,-1],
# [-1,-1,-1,-1],
# [-1,11,-1,-1]]))

# print(Solution().snakesAndLadders([
# [-1,-1,-1,-1,-1,-1],
# [-1,35,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [26,-1,-1,-1,-1,-1],
# [-1,35,-1,-1,-1,-1],
# [-1,12,-1,-1,-1,-1]]))

# print(Solution().snakesAndLadders([
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,36,-1],
# [-1,8,-1,-1,-1,-1]]))

# print(Solution().snakesAndLadders([[1,1,-1],[1,1,1],[-1,1,1]]))
