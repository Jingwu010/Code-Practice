class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str] -> Set
        :rtype: bool
        """
        if not s: return False
        wordDict = set(wordDict)
        table = [[0 for c in s] for c in s]
        for k in range(len(s)):
	        for i in range(len(s)):
        		j = i + k
        		if j >= len(s): break
        		if s[i:j+1] in wordDict:
        			table[i][j] = 1
        			continue
        		for bp in range(k):
        			if table[i][i+bp] == 1 and table[i+1+bp][j] == 1:
        				table[i][j] = 1
        				break
        # for i in range(len(s)):
        # 	print(table[i])
        # print(table[0][len(s)-1])
        return table[0][len(s)-1] == 1

print(Solution().wordBreak("leetcode", ["leet","code"]))
print(Solution().wordBreak("leetcode", ["le","l","eet","de","etcod","c"]))
print(Solution().wordBreak("leetcode", ["le","l","eet","e","etcod","c"]))
print(Solution().wordBreak("llllllll", ["l","ll"]))
print(Solution().wordBreak("", []))