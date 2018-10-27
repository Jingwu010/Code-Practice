class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        def helper(i, j, minCost):
            if i == len(word1) or j == len(word2):
                return len(word1)-i + len(word2)-j
                
            if (i,j) in minCost:
                return minCost[(i,j)]

            if word1[i] == word2[j]:
                minCost[(i,j)] = helper(i+1, j+1,minCost)
                return minCost[(i,j)]

            minCost[(i,j)] = min(helper(i,j+1,minCost)+1, #insert at word1
                                 helper(i+1,j,minCost)+1, #remove at word1
                                 helper(i+1,j+1,minCost)+1)#replace at word1
            return minCost[(i,j)]
        
        return helper(0, 0, {})

# print(Solution().minDistance('ineetion', 'execution'))
# print(Solution().minDistance('horse', 'ros'))
print(Solution().minDistance('intention', 'execution'))