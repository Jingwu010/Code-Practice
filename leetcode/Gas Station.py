import time
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        if sum(gas) < sum(cost):
            return -1

        nlen = len(gas)
        i = 0
        j = 0

        # scan the whole list once
        while i < nlen:
            remaining = 0

            # when the remaining is greater than 0
            # which means we can start from here
            for j in range(nlen):
                idx = (i + j) % nlen
                remaining = remaining + gas[idx] - cost[idx]

                # if the remaining till this point is not enough
                # that means any point (i) ahead of this (j) will not have enough sum
                # then we start from next point i += (j + 1)
                if remaining < 0:
                    i += (j + 1)
                    break
            if j == nlen - 1:
                return i
            
        return -1

print(Solution().canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))

print(Solution().canCompleteCircuit([2,3,4],[3,4,3]))

print(Solution().canCompleteCircuit([3,3,4],[3,4,3]))

print(Solution().canCompleteCircuit([1,1,1,2],[2,1,1,1]))

print(Solution().canCompleteCircuit([1,1,1,2],[2,1,1,1]))