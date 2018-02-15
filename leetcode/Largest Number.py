import functools
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compareNums(num1, num2):
        	idx = 0
        	maxsComp = max(len(num1), len(num2)) * 2
        	while True:
        		if int(num1[idx % len(num1)]) > int(num2[idx % len(num2)]):
        			return -1
        		elif int(num1[idx % len(num1)]) < int(num2[idx % len(num2)]): 
        			return 1
        		idx += 1
        		if idx > maxsComp:
        			return -1
        	return 1

        def checkZero(num):
        	for c in num:
        		if c != '0':
        			return False
        	return True

        nums = [str(x) for x in nums]
        nums = sorted(nums, key=functools.cmp_to_key(compareNums))
        # print(nums)
        result = ""
        for num in nums:
        	result += num
        return "0" if checkZero(result) else result

print(Solution().largestNumber([3, 30, 34, 5, 9]))
print(Solution().largestNumber([1,1,1,1,10]))
print(Solution().largestNumber([2,3,4,1,0]))
print(Solution().largestNumber([10,10,11,9,10]))
print(Solution().largestNumber([128,12]))
print(Solution().largestNumber([0,9,8,7,6,5,4,3,2,1]))
print(Solution().largestNumber([100,90,89,88]))
print(Solution().largestNumber([0,0]))
print(Solution().largestNumber([0,0,1]))
print(Solution().largestNumber([2362,2362,2313,2,2281,216]))
print(Solution().largestNumber([2000,2060,213,216,2281,2,2313,2362,2362]))
print(Solution().largestNumber([4704,6306,9385,7536,3462,4798,5422,5529,8070,6241,9094,7846,663,6221,216,6758,8353,3650,3836,8183,3516,5909,6744,1548,5712,2281,3664,7100,6698,7321,4980,8937,3163,5784,3298,9890,1090,7605,1380,1147,1495,3699,9448,5208,9456,3846,3567,6856,2000,3575,7205,2697,5972,7471,1763,1143,1417,6038,2313,6554,9026,8107,9827,7982,9685,3905,8939,1048,282,7423,6327,2970,4453,5460,3399,9533,914,3932,192,3084,6806,273,4283,2060,5682,2,2362,4812,7032,810,2465,6511,213,2362,3021,2745,3636,6265,1518,8398]))


