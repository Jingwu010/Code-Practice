# why i dfs?
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def strDif(str1, str2):
        	num = 0
        	for i in range(len(str1)):
        		if str1[i] != str2[i]:
        			num += 1
        	return num

        def dfs(tmp, goal, wordList, vis):
        	if strDif(tmp, goal) == 1:
        		return 1
        	
        	steps = []
        	for i in range(len(wordList)):
        		if vis[i]:
        			continue
        		if strDif(tmp, wordList[i]) == 1:
        			vis[i] = True
        			step = dfs(wordList[i], goal, wordList, vis)
        			# print(wordList[i], goal, "=", step)
        			if step != -1:
	        			steps.append(step + 1)
	        		vis[i] = False
        		elif strDif(tmp, wordList[i]) > 1:
        			continue
        			
        	if steps:
        		return min(steps)
        	else:
        		return -1

        vis = [False for x in range(len(wordList))]
        if endWord in wordList:
        	return dfs(beginWord, endWord, wordList, vis) + 1
        else:
        	return 0
        	
print(Solution().ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))
print(Solution().ladderLength("hit","hog",["hot","dot","dog","lot","log","cog"]))
print(Solution().ladderLength("aaa","bac",["aac","caa","aab","cab","bab","bac"]))
print(Solution().ladderLength("hot","dog",["hot","cog","dog","tot","hog","hop","pot","dot"]
))





