import sys
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = [["(",n-1,1]]
        lens = 2 * n - 1
        while lens > 0:
        	lens -= 1
        	newResult = []
        	for base in result:
        		if base[1] > 0:
        			newResult.append([base[0] + '(', base[1]-1, base[2]+1])
        		if base[2] > 0:
        			newResult.append([base[0] + ')', base[1], base[2]-1])
        		result = newResult

        return [x[0] for x in result]

        

n = int(input())
print(Solution().generateParenthesis(n))



# ()

# (())
# ()()

# (()())
# ((()))
# ()()()
# (())()
# ()(())

# (())(())

# 12

# 1212 -> 121212
# 	 -> 112122
# 1122 -> 112212
# 	 -> 121122
# 	 -> 111222

# 111222
# 112122
# 112212
# 121122
# 121212

