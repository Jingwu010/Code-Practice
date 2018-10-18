import math
class Solution:
    # motivation for a binary search is the total problem complexity 
    # could up to [1, m * n] = 9 * 10 ^8
    # Linear time solution wont work.
    # Need to come up with a log n solution
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        
        def smaller(num):
            # return how many number in the multiplication table that
            # are smaller than 'num'
            # for each row looks like [i*1, i*2, ... i*k]
            # print(num, [min(num // i, n) for i in range(1, m+1)])
            return sum(min(num // i, n) for i in range(1, m+1))

        left = 1
        right = m * n
        while left < right:
            middle = (left + right) // 2
            # print(left, right, middle, smaller(middle))
            # if k-th value is bigger than m
            # move the left to middle + 1
            if smaller(middle) < k:
                left = middle + 1
            else:
                right = middle
        return left

# print(Solution().findKthNumber(2, 3, 6))
print(Solution().findKthNumber(23412,9762,12345567))