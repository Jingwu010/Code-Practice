class Solution:
	def strTransformation(self, string):
		'''
		TODO
		aacceeggiikkmmooqqssuuwwyy --> abcdefghijklmnopqrstuvwxyz
		aaaceeggiikkmmooqqssuuwwyy --> -1
		aaaaaaaacceeggiikkmmooqqssuuwwyyzzz --> abcdefghijklmnopqrstuvwxyz
		azacceeggiikkmmooqqssuuwwyy --> abcdefghijklmnopqrstuvwxyz
		thereisnoanswer --> -1
		'''
		idx = 0
		while idx < len(string):
			pedding, skips = 0, 0
			while -1 <= ord(string[idx + pedding + skips]) - ord('a') - pedding  <= 0:
				# print(string[idx + pedding], pedding)
				pedding += 1
				if pedding > 25:
					return "abcdefghijklmnopqrstuvwxyz"
				if idx + pedding >= len(string):
					return -1
			idx += 1 if pedding == 0 else pedding
		return -1

print(Solution().strTransformation("aaaceeggiikkmmooqqssuuwwyy"))
print(Solution().strTransformation("aacceeggiikkmmooqqssuuwwyy"))
print(Solution().strTransformation("thereisnoanswer"))
print(Solution().strTransformation("abcdefgahijklmnopqrstuvwxyz"))