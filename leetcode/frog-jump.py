class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]     
            2 <= len(stones) < 1100
            0 <= stone[i] < 2**31
            stone[0] = 0
        :rtype: bool
        """
        #  first jump must be 1 unit
        
        stones.sort()

        stset = set(stones)
        # Dictionary is used to record step size that used from
        # any stone before which successfuuly arrived at
        # stone i, initially, stone 0 with step size 0
        ret = {}
        for stone in stones:
            ret[stone] = set()
        ret[0].add(0)
        for stone in stones:
            # print(stone, ret[stone])
            for step in ret[stone]:
                if step-1 > 0 and step-1+stone in stset:
                    ret[step-1+stone].add(step-1)
                if step > 0 and step+stone in stset:
                    ret[step+stone].add(step)
                if step+stone+1 in stset:
                    ret[step+stone+1].add(step+1)
            if len(ret[stones[-1]]) != 0:
                return True
        return False

# print(Solution().canCross([0,1,3,5,6,8,12,17]))
# print(Solution().canCross([0,1,2,3,4,8,9,11]))