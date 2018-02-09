class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        def bfs(beginWord, endWord, wordList):
        	if beginWord == endWord:
        		return 0

        	queue = [(beginWord,1)]
        	while queue:
        		# print(queue)
        		newQueue = []
        		for wordTuple in queue:
	        		word, step = wordTuple
	        		if word == endWord:
	        			return step
	        		for i in range(len(word)):
	        			for c in 'abcdefghijklmnopqrstuvwxyz':
	        				next_word = word[:i] + c + word[i+1:]
	        				if next_word in wordList:
	        					newQueue.append((next_word, step+1))
	        					wordList.remove(next_word)
	        	queue = newQueue

        	return 0

        if endWord in wordList:
        	return bfs(beginWord, endWord, set(wordList))
        else:
        	return 0
        	
print(Solution().ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))
print(Solution().ladderLength("hit","hog",["hot","dot","dog","lot","log","cog"]))
print(Solution().ladderLength("aaa","bac",["aac","caa","aab","cab","bab","bac"]))
print(Solution().ladderLength("hot","dog",["hot","cog","dog","tot","hog","hop","pot","dot"]
))
print(Solution().ladderLength("hot","dog",["hot","dog"]))




