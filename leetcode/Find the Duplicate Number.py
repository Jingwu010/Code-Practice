import time
class Solution:

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def binaryCompare(arr, key):
        	smaller, larger = 0, 0
        	for num in arr:
        		if num > key:
        			larger += 1
        		if num < key:
        			smaller += 1
        	return smaller, larger
        

        if len(nums) % 2 == 1:
        	nums.append(len(nums))
        maxs = len(nums) - 1
        mins = 1
        lens = len(nums) - 1

        while maxs >= mins:
        	mid = (maxs+mins) // 2
        	smaller, larger = binaryCompare(nums, mid)
        	# time.sleep(1)
        	# print("smaller", smaller, "\n | larger", larger, "\n mid = ",mid, "mins=",mins, "maxs=",maxs)
        	# print()
        	if smaller <= mid - 1 and larger <= lens - mid:
        		return mid
        	elif smaller > mid - 1:
        		maxs = mid - 1
        	elif larger > lens - mid:
        		mins = mid + 1
        return False

print(Solution().findDuplicate([2,5,9,6,9,3,8,9,7,1]))
print(Solution().findDuplicate([1,1,1,2,3]))
print(Solution().findDuplicate([1,1,1,2,3,6]))
print(Solution().findDuplicate([1,1]))
print(Solution().findDuplicate([1,1,2]))
print(Solution().findDuplicate([1,2,2]))
print(Solution().findDuplicate([1,2,3,4,5,6,1]))
print(Solution().findDuplicate([1,2,3,4,5,6,2]))
print(Solution().findDuplicate([1,2,3,4,5,6,3]))
print(Solution().findDuplicate([1,2,3,4,5,6,4]))
print(Solution().findDuplicate([1,2,3,4,5,6,5]))
print(Solution().findDuplicate([1,2,3,4,5,6,6]))