
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        lens = len(s)
        table = [[0 for x in s] for j in s]
        for i in range(lens):
        	table[i][i] = 1
        	if i + 1 < lens:
        		table[i+1][i] = 1
        for k in range(1, lens):
        	for i in range(lens):
        		j = i + k
        		if j >= lens:
        			break
        		if s[i] == s[j] and table[i+1][j-1] == 1:
        			table[i][j] = 1
        # for i in range(lens):
        # 	for j in range(lens):
        # 		print(table[i][j], end="")
        # 	print()
        dp = [[] for i in s]
        dp[0] = [[s[0]]]
        for i in range(1, lens):
            for j in range(i+1):
                if table[j][i] == 1:
                    k = s[j:i+1]
                    # print(dp[i-1], i, j, k)
                    if j == 0:
                        dp[i].append([k])
                    else:
                        # print(j-1, "dp[j-1] = ", dp[j-1])
                        for ss in dp[j-1]:
                            # print("ss = ",ss, "k = ", k, )
                            dp[i].append(ss + [k])
            # print(i, dp[i])
            # print()
        # for i in range(lens):
        #     print(dp[i])
        # print()
        return dp[lens-1]

		
print(Solution().partition("aab"))
print()
print(Solution().partition("ababba"))
#   a a b
# a 1 1 0
# a   1 0
# b     1

#   0 1 2 3 4 5
#   a b a b b a
# a 1 0 1 0 0 0
# b   1 0 1 0 0
# a     1 0 0 1
# b       1 1 0
# b         1 0
# a           1