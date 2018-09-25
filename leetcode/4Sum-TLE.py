class Solution:
    def fourSum(self, nums, target):
        """
        [-1,1,0,0,-2,2], 0 --> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        [-1,0,1,2,3,4,4], 7 --> [[-1,0,4,4],[-1,1,3,4],[0,1,2,4]]
        [0,0,1,2,3,4,4], 6 --> [[0,0,2,4],[0,1,2,3]]
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(sumList, nums):
        	tmp = sum(sumList)
        	if tmp == target and len(sumList) == 4:
        		if tuple(sumList) not in fourSet:
        			fourSet.add(tuple(sumList))
        			ret.append(sumList)
        	for i, num in enumerate(nums):
        		dfs(sumList+[num], nums[i+1:])

        nums.sort()
        fourSet = set()
        ret = []
        dfs([], nums)
        return ret

print(Solution().fourSum([-1,0,0,1,-2,2], 0))
print(Solution().fourSum([-1,0,1,2,3,4,4], 7))
print(Solution().fourSum([0,0,1,2,3,4,4], 6))
print(Solution().fourSum([1,1,1,1,0,0,0,-1,-1,-1], 0))
print(Solution().fourSum([1,-2,-5,-4,-3,3,3,5], -11))



        