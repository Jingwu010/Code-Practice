class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        def list2dic(li):
        	dic = {}
        	for key in li:
        		if key in dic:
        			dic[key] += 1
        		else: dic[key] = 1
        	return dic

        if not words: return []
        step = len(words[0])
        worddic = list2dic(words)
        ret = []
        for i in range(len(s)):
        	if i + step * len(words) > len(s): break
        	
        	index = i
        	remainning = worddic.copy()
        	flag = True
        	while flag:
        		word = s[index: index+step]

        		if word in remainning:
        			if remainning[word] == 1:
        				remainning.pop(word)
        			else: remainning[word] -= 1
        			index = index + step
        		else: flag = False

        		# print(remainning, i)

        		if not remainning: break

        		if index + step > len(s):
        			flag = False
        		
        	if flag:
        		ret.append(i)
        return ret


print(Solution().findSubstring("aaaa", ["aa"]))
print(Solution().findSubstring("aaabbab", ["aa", "ab", "bb"]))
print(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(Solution().findSubstring("barfoofoololbar", ["foo", "bar", "lol"]))
print(Solution().findSubstring("barfoofoololbar", []))
print(Solution().findSubstring("", ["a"]))
print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))

"""
aaabbab
[aa,ab,bb]
"""