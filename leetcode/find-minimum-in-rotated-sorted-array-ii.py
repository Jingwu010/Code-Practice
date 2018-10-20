class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # duplicates?
        # negative?
        # empty?
        # 
        
        if len(nums) <= 2:
            return min(nums)

        half = len(nums) // 2
        middle = nums[half]
        left = nums[half//2]
        right = nums[half+half//2]

        print(nums, left, middle, right)

        # all pivots are equal does not tell us more information
        if middle == left and middle == right:
            return min(self.findMin(nums[:half]), self.findMin(nums[half:]))
        if middle >= left and middle <= right:
            return min(self.findMin(nums[:half//2+1]), self.findMin(nums[half+half//2:]))
        if middle >= left and middle > right:
            return self.findMin(nums[half:])
        if middle < left and middle <= right:
            return self.findMin(nums[half//2:half+half//2+1])

# print(Solution().findMin([1,3,5]))
# print(Solution().findMin([4,5,6,7,8,9,0]))
# print(Solution().findMin([4,7,1,2,3]))
# print(Solution().findMin([3,5,7,7,0,1,2]))
# print(Solution().findMin([3,4,7,1,2]))
# print(Solution().findMin([-3,-2,-1,-7,-3]))
print(Solution().findMin([0,3,3,3,3,3,1]))