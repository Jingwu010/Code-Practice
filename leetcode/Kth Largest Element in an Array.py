import time
class Solution:

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(nums, l, r):
        	pivot = nums[r]
        	idx = l
        	for i in range(l, r):
        		if nums[i] < pivot:
        			nums[i], nums[idx] = nums[idx], nums[i]
        			idx += 1
        	nums[idx], nums[r] = nums[r], nums[idx]
        	return idx


        def quickSelect(nums, l, r, k):
        	if k <= r and k >= l:
        		idx = partition(nums, l, r)
        		# print("idx", idx, nums[idx])
        		if idx == k:
        			return nums[idx]
        		elif idx > k:
        			return quickSelect(nums, l, idx-1, k)
        		else:
        			return quickSelect(nums, idx+1, r, k)
        	else: return None

        lens = len(nums)
        return quickSelect(nums, 0, lens-1, lens-k)

print(Solution().findKthLargest([3,2,1,5,6,4], 2))
print(Solution().findKthLargest([3,2,1,5,6,4], 1))
print(Solution().findKthLargest([1,1,1,1,1,1], 6))
print(Solution().findKthLargest([1,1,1,1,1,1], 1))