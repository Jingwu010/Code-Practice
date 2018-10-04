class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = [1]
        minimum = [1]
        for i, num in enumerate(nums):
            # used a maximum array to keep track of local maximum
            # which comes from previous maximum time current num
            # or, previous minimum times current num or the number itself
            maximum.append(max(maximum[i]*num, minimum[i]*num, num))
            # used a minimum array to keep track of local minimum
            # This array is used to handle minus signs 
            minimum.append(min(maximum[i]*num, minimum[i]*num, num))
            print('max = ', maximum[i+1])
            print('min = ', minimum[i+1])

        return max(maximum[1:])

print(Solution().maxProduct([-2,3,-1,-3]))
print(Solution().maxProduct([2,3,-2,4]))
print(Solution().maxProduct([-2,0,-1]))
print(Solution().maxProduct([-3,-2,-2,-3]))