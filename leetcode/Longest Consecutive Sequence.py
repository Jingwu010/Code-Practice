class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # nums[i] can be positive, negative and 0
        # []
        # duplicates

        numSet = set()
        for num in nums:
            numSet.add(num)

        loopSet = numSet.copy()
        ret = 0
        for num in loopSet:
            cs = 1
            if num not in numSet:
                continue
            print('exploring', num)
            dirs = [-1, 1]
            for dir in dirs:
                steps = 1
                while True:
                    newNumber = num+steps*dir
                    if newNumber not in numSet:
                        break
                    cs += 1
                    steps += 1
                    numSet.remove(newNumber)
            ret = max(ret, cs)
        return ret

print(Solution().longestConsecutive([1,1,1,1,2]))
print(Solution().longestConsecutive([1,3,5,111111]))
print(Solution().longestConsecutive([-1,1,3,-2,-4]))
print(Solution().longestConsecutive([]))