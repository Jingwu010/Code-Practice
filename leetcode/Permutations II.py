class Solution:
    def permuteUnique(self, nums):
        """
        [1,2] --> [[1,2],[2,1]]
        [1,1,2] --> [[1,1,2],[1,2,1],[2,1,1]]
        [1,2,3] --> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, permutelist):
            # check if the sublist is in the set
            # if ture, then the permutation is not unique, break
            # else, the permutation sublist is unique, continue
            if tuple(permutelist) in duplicateSet:
                return
            duplicateSet.add(tuple(permutelist))
            if not nums:
                ret.append(permutelist)
                return 
            if len(permutelist) == 0:
                dfs(nums[1:], [nums[0]])
                return 
            for i in range(len(permutelist)+1):
                dfs(nums[1:], permutelist[:i]+[nums[0]]+permutelist[i:])

        duplicateSet = set()
        ret = []
        dfs(nums, [])
        return ret

# print(len(Solution().permuteUnique([1,2,3,4])))
# print(Solution().permuteUnique([1,2,3]))
# print(Solution().permuteUnique([1,2]))
# print(Solution().permuteUnique([1]))
# print(Solution().permuteUnique([]))
print(Solution().permuteUnique([1,1,2]))
print(Solution().permuteUnique([1,1,1,1,1,1,1,1,1,1,2]))
        