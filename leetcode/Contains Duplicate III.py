class Solution:

    # def containsNearbyAlmostDuplicate(self, nums, k, t):
    #     # TLE
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :type t: int
    #     :rtype: bool
    #     """

    #     # i != j
    #     # | nums[i] - nums[j] | <= t
    #     # | i - j| <= k
    #     if len(nums) < 2:
    #         return False
    #     # the upper bound of the iteration
    #     for i in range(len(nums)):
    #         # the upper bound of the iteration
    #         for j in range(i+1, min((i+k+1), len(nums))):
    #             if abs(nums[i] - nums[j]) <= t:
    #                 return True
    #     return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        # i != j
        # | nums[i] - nums[j] | <= t
        # | i - j| <= k
        # 

        # The idea here is maintain a window of length (k+1), nums[i] ... nums[i+k]
        # where all nums[i] where i in the window frame are sorted into different buckets
        # with bucket size t
        # The possible solution is two numbers are in the same bucket or in its neighbour buckets
        
        # Never expect user input correct values
        if k < 0 or t < 0: return False

        buckets = {}
        size = t + 1

        for i, num in enumerate(nums):
            if i > k:
                del buckets[nums[i-k-1] // size]
            # t != 0
            print(buckets)
            bucket = num // size

            
            if bucket in buckets:
                return True
            if bucket-1 in buckets and abs(buckets[bucket-1] - num) < size:
                return True
            if bucket+1 in buckets and abs(buckets[bucket+1] - num) < size:
                return True

            # There will be at most 1 value in 1 bucket. 
            # If you have others in (m-1)th bucket, 
            # it must have already returned True when you find two values in the same (m-1)th bucket.
            buckets[bucket] = num
        return False


# print(Solution().containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))
# print(Solution().containsNearbyAlmostDuplicate([1,0,1,1],1,2))
# print(Solution().containsNearbyAlmostDuplicate([1,2,3,1],3,0))
# print(Solution().containsNearbyAlmostDuplicate([1,3,5,7,9],0,2))
# print(Solution().containsNearbyAlmostDuplicate([1,3,5,7,1],3,1))
print(Solution().containsNearbyAlmostDuplicate([],1,1))
# print(Solution().containsNearbyAlmostDuplicate([1,2],0,0))
# print(Solution().containsNearbyAlmostDuplicate([1,2],2,0))
# print(Solution().containsNearbyAlmostDuplicate([-11,3],2,9))