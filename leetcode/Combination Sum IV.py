class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # nums[i] != nums[j]
        # nums[i] > 0
        
        # DFS should be considered with DP!
        def dfs(nums, target, dp):
            if dp[target] != -1:
                return dp[target]
            if target == 0:
                return 1
            ret = 0
            for num in nums:
                if num <= target:
                    ret += dfs(nums, target-num, dp)
            dp[target] = ret
            return ret

        dp = [-1] * (target+1)
        nums.sort(reverse=True)
        return dfs(nums, target, dp)

# print(Solution().combinationSum4([1, 2, 3], 4))
# print(Solution().combinationSum4([1, 4, 2, 5], 7))
print(Solution().combinationSum4([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 40))