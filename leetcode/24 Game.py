class Solution:
    precision = 0.000001
    dp = {}

    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # print(nums)
        flag = False

        if len(nums) == 1:
            # print(nums)
            # Lost precision due to float operations
            return abs(nums[0] - 24) < self.precision

        nums.sort()
        if tuple(nums) in self.dp:
            return self.dp[tuple(nums)]

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                remaining = nums[:i] + nums[i+1:j] + nums[j+1:]
                # a + b
                flag = flag or self.judgePoint24([nums[i]+nums[j]] + remaining)
                # a - b
                flag = flag or self.judgePoint24([nums[i]-nums[j]] + remaining)
                # b - a
                flag = flag or self.judgePoint24([nums[j]-nums[i]] + remaining)
                # a * b
                flag = flag or self.judgePoint24([nums[i]*nums[j]] + remaining)
                # a / b
                if nums[j] != 0:
                    flag = flag or self.judgePoint24([nums[i]/nums[j]] + remaining)
                # b / a
                if nums[i] != 0:
                    flag = flag or self.judgePoint24([nums[j]/nums[i]] + remaining)

        self.dp[tuple(nums)] = flag
        return self.dp[tuple(nums)]

# print(Solution().judgePoint24([3,3,8,8]))
print(Solution().judgePoint24([1,3,4,6]))
