class Solution:
    # def canJump(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     def dfs(idx, nums, vis):
    #     	vis[idx] = True
    #     	flag = False
    #     	if idx == len(nums) - 1:
    #     		return True
    #     	if idx + nums[idx] < len(nums) and not vis[idx + nums[idx] ]:
    #     		if dfs(idx+nums[idx], nums, vis):
    #     			flag = True
    #     	if idx - nums[idx] >= 0 and not vis[idx - nums[idx]]:
    #     		if dfs(idx-nums[idx], nums, vis):
    #     			flag = True
    #     	return flag
         
    #     vis = [False for i in nums]
    #     return dfs(0, nums, vis)

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        idx = 0
        maxsLen = [0 for i in nums]
        maxsLen[0] = nums[0]
        for i in range(1, len(nums)):
        	if maxsLen[i-1] < i:
        		return False
        	maxsLen[i] = max(maxsLen[i-1], i + nums[i])
        return True

print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))
print(Solution().canJump([3,2,2,0,4]))
print(Solution().canJump([1,1,1,0,4]))

