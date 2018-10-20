class Solution:
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        
        # 1 <= positions.length <= 1000.
        # 1 <= positions[i][0] <= 10^8.
        # 1 <= positions[i][1] <= 10^6.
        # 
        
        queue = []
        ret = []
        maxH = 0
        for position in positions:
            maxs = 0
            left = ()
            right = ()
            # the right position to insert new interval
            smaller = len(queue)

            # loop through overlaping intervals to find maximum height
            for i, interval in enumerate(queue):
                l = position[0]
                r = position[0] + position[1] - 1
                if l <= interval[1] and r >= interval[0]:
                    if not left: left = (i, interval)
                    maxs = max(interval[2], maxs)
                    right = (i, interval)
                if r < interval[0] and smaller == len(queue):
                    smaller = i

            # the maximum height to build upon
            h = maxs + position[1]

            # print(left, right)
            # manipulate the queue
            middle = [(position[0], position[0]+position[1]-1, h)]
            if left and right:
                leftSplit = [(left[1][0], position[0]-1, left[1][2])] if left[1][0] <= position[0]-1 else []
                rightSplit = [(position[0]+position[1], right[1][1], right[1][2])] if position[0]+position[1] <= right[1][1] else []
                queue = queue[:left[0]] + leftSplit + middle + rightSplit + queue[right[0]+1:]
            else:
                if queue:
                    queue = queue[:smaller] + middle + queue[smaller:]
                else:
                    queue = middle
            # print(queue)
            maxH = max(maxH,h)
            ret.append(maxH)

        return ret

print(Solution().fallingSquares([[1, 2], [2, 3], [6, 1]]))
print(Solution().fallingSquares([[1,3],[2,5],[4,1],[6,7],[9,1],[4,4],[3,7],[1,2],[3,1],[5,6]]))
print(Solution().fallingSquares([[100, 100], [200, 100], [300, 100], [1, 150], [200, 150], [200,1]]))
print(Solution().fallingSquares([[7,1],[3,3],[7,5]]))
print(Solution().fallingSquares([[2,1],[2,2],[3,2],[4,2],[5,2],[1,3],[4,2]]))
print(Solution().fallingSquares([[3,1],[5,1],[7,1],[4,1]]))


