
class Solution:
    def countBits(self, num):
        """
        :type i: int
        :rtype: List[int]
        """
        bound = 2
        idx = 0
        if num == 0: return [0]
        if num == 1: return [0, 1]
        result = [0, 1]
        for i in range(2, num+1):
        	if i == bound:
        		result.append(1)
        		bound *= 2
        		idx = 1
        		continue
        	result.append(1 + result[idx])
        	idx += 1
        return result

print(Solution().countBits(0))
print(Solution().countBits(1))
print(Solution().countBits(2))
print(Solution().countBits(5))
print(Solution().countBits(32))

    
# 0 1 2  3   4   5   6   7   8    9    10   11   12  13    14    15    16
# 0 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101  1110  1111 10000
# 0 1 1  2   1   2   2   3   1    2     2   3    2
           # ^
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1]

