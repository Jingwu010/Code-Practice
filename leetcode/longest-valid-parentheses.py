import time
import collections
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # stack version
        # stack = list()
        # s = ')'+s
        # for char in s:
        #     if char == '(':
        #         stack.append(['(',0])
        #     if char == ')':
        #         if stack and stack[-1][0] == '(':
        #             top = stack.pop()
        #             stack[-1][1] += top[1]+2
        #         else:
        #             stack.append([')',0])
        # return max(stack, key=lambda x:x[1])[1]
        # 
        # dp version
        s = ')'+s
        dp = [0] * len(s)
        for i, char in enumerate(s):
            if char == '(':
                continue
            if char == ')':
                if i > 0 and s[i-1] == '(':
                    dp[i] = dp[i-2]+2 if i >= 2 else 0+2
                if i > 0 and s[i-1] == ')':
                    if i > 1 and s[i-dp[i-1]-1] == '(':
                        dp[i] = dp[i-1]+2+dp[i-dp[i-1]-2]
        return max(dp)


print(Solution().longestValidParentheses("(()))())("))
