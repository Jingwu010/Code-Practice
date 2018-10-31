class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        stack = list()
        maxH = 0
        for i, height in enumerate(heights):
            if not stack or height >= stack[-1][0]:
                stack.append((height,i))
                maxH = max(maxH, height)
                continue
            # if height < stack[-1]
            lstidx = 0
            while stack and stack[-1][0] > height:
                maxH = max(maxH, (i-stack[-1][1])*stack[-1][0])
                lstidx = stack[-1][1]
                stack.pop()
            stack.append((height,lstidx))
        # print(stack)
        for i, v in enumerate(reversed(stack)):
            maxH = max(maxH, (len(heights)-v[1])*v[0])
        # maxH = max(maxH, len(heights)*stack[0][0])
        return maxH

# print(Solution().largestRectangleArea([2,1,5,6,2,3]))
# print(Solution().largestRectangleArea([7,5,9,10,9,5,4]))
print(Solution().largestRectangleArea([2]))