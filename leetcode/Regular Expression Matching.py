class Solution:
    def isMatch(self, text, pattern):
        """
        . matches any characters
        * matches zore or more preceding character

        the idea is for a '*' we can view it as a skip or recursively call multiple times.
        then pairing pattern with text, untill there is one recursive call leads to a match
        using dp to improve the performance of recursion
        
        :type text: str
        :type pattern: str
        :rtype: bool
        """
        res = {}

        # dp(i, j) means pairring text[i:] with pattern[j:]
        def dp(i, j):
            if (i, j) in res:
                return res[i, j]

            if j == len(pattern):
                return i == len(text)

            # if the text is not empty
            # and the pattern matches with text
            first_match = bool (i < len(text)) and pattern[j] in {'.', text[i % len(text)]}


            if len(pattern) - j > 1 and pattern[j + 1] == '*':
                res[i, j] = (dp(i, j + 2) or first_match and dp(i + 1, j))
            else:
                res[i, j] = first_match and dp(i + 1, j + 1)
            return res[i, j]
        return dp(0, 0)

class Solution2:
    def isMatch(self, text, pattern):
        """
        . matches any characters
        * matches zore or more preceding character
        :type text: str
        :type pattern: str
        :rtype: bool
        """
        if not pattern:
            return not text

        first_match = bool (text) and pattern[0] in {'.', text[0]}

        if len(pattern) > 1 and pattern[1] == '*':
            if self.isMatch(text, pattern[2:]):
                return True

            else:
                return first_match and self.isMatch(text[1:], pattern)
                
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

class Solution3:
    def isMatch(self, text, pattern):
        """
        . matches any characters
        * matches zore or more preceding character
        :type text: str
        :type pattern: str
        :rtype: bool
        """
        def isStar(idx, str):
            if idx + 1 < len(str):
                if str[idx + 1] == '*':
                    return True
                else:
                    return False
            else:
                return False

        def isEqual(c1, c2):
            if c1 == c2:
                return True
            if c1 == '.' and c2 != '@':
                return True
            if c2 == '.' and c1 != '@':
                return True
            return False

        if len(text) == 0 and len(pattern) == 0:
            return True

        if len(text) > 0:
            char1 = text[0]
        else:
            char1 = '@'
        if len(pattern) > 0:
            char2 = pattern[0]
        else:
            char2 = '@'

        flag = False
        if isStar(0, pattern):
            if self.isMatch(text, pattern[2:]):
                flag = True

            if isEqual(char1, char2):
                for i in range(1, len(text) + 1):
                    if isEqual(text[i-1], char2):
                        # print("checking ", text[i:], pattern)
                        if self.isMatch(text[i:], pattern):
                            flag = True
                            if flag:
                                break
                
        else:
            if isEqual(char1, char2):
                if self.isMatch(text[1:], pattern[1:]):
                    flag = True
            else:
                flag = False
        return flag 


# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true

# print(Solution().isMatch("aab", "c*a*b"))
# print(Solution().isMatch("ab", ".*"))
# print(Solution().isMatch("aa", ".*"))
# print(Solution().isMatch("aa", "a*"))
# print(Solution().isMatch("aaa", "aa"))
# print(Solution().isMatch("aa", "aa"))
# print(Solution().isMatch("aa", "a"))
# print(Solution().isMatch("a*b*", "b*a*"))
# print(Solution().isMatch("a*b*", "c*d*"))
# print(Solution().isMatch("a*", "c*a"))
# print(Solution().isMatch("a", "c*d*a"))
# print(Solution().isMatch("aaa", "ab*a*c*a"))
# print(Solution().isMatch("aaba", "ab*a*c*a"))
# print(Solution().isMatch("abcca", "ab*a*c*a"))
# print(Solution().isMatch("a", ".*..a*"))
# print(Solution().isMatch("aaaab", "a*a*a*a*b"))
# print(Solution().isMatch("aaaaaaaaaab", "a*a*a*a*a*a*a*a*a*b"))



