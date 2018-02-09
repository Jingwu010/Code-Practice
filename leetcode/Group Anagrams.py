class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def hashString(string):
        	hashList = [0 for i in range(26)]
        	for c in string:
        		hashList[ord(c) - ord('a')] += 1
        	# hashes = sum([ord(c) - ord('a') for c in string])
        	return tuple(hashList)

        anaDic = {}
        for string in strs:
        	strhash = hashString(string)
        	if strhash in anaDic:
        		anaDic[strhash].append(string)
        	else:
        		anaDic[strhash] = [string]
        return list(anaDic.values())

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams(["e", "ee", "eee", "eea", "eae", "ae"]))
print(Solution().groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))