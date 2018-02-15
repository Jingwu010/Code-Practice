class Solution:
    def firstMissingPositive(self, nums):
        """
        The idea is for any given list[], the most possible positive integers is from 1 ... l (l is the length of list)
        Then for each value, we put it back to its original place using hash index, 
        for example, 5 should goes to nums[4], 9 should goes to nums[8]
        Then using hash value to calculate the occurance of each num
        :type nums: List[int]
        :rtype: int
        """

        # make sure n is bigger than l (1 ... l)
        nums.append(0)
        n = len(nums)

        # set out boundary nums to 0 
        for i in range(n):
        	if nums[i] < 0  or nums[i] > n - 1:
        		nums[i] = 0

        # hash index each value in the list
       	for i in range(n):
       		nums[nums[i] % n] += n

       	# calculate their occurance based on hash value
       	for i in range(n):
       		if nums[i] // n <= 0:
       			return i
       	return n
