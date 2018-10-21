class Solution:
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        
        # n <= 100
        
        def dfs(boxes, occ, dp):
            # print(occ, '\t', boxes)
            if not boxes:
                return 0

            if tuple(boxes) in dp:
                return dp[tuple(boxes)]

            score = 0
            for k, v in occ.items():
                if v == 1:
                    idx = boxes.index(k)
                    newOcc = occ.copy()
                    newOcc[k] = 0
                    score = dfs(boxes[:idx]+boxes[idx+1:], newOcc, dp) + 1

            i = 0
            while i < len(boxes):
                j = i
                while j < len(boxes) and boxes[j] == boxes[i]:
                    j += 1
                nlen = j-i
                newOcc = occ.copy()
                newOcc[boxes[i]] = occ[boxes[i]]-nlen
                score = max(score, dfs(boxes[:i]+boxes[j:], newOcc, dp) + nlen*nlen) 
                i = j
            dp[tuple(boxes)] = score
            return score


        occ = {}
        for num in boxes:
            occ[num] = occ.get(num, 0)+1

        maxs = dfs(boxes, occ, {})
        return maxs

print(Solution().removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]))