class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """


        # build parenthese tree by taking the constraint
        def dfs(valid, pos, template, stack, uniqueSet):
            # print(valid, '\t', pos, '\t', stack)
            if not stack:
                # print('ADD ==\t', valid+template[pos:])
                uniqueSet.add(valid+template[pos:])
                return

            # Take the first constraint out
            parenthese, idx = stack[0]

            # Distinguish the left( and right) parenthese case
            if parenthese == ')':
                # right ) is able to replace one ) on its left
                for i in range(pos, idx+1):
                    if template[i] == parenthese:
                        # replace, dfs
                        dfs(valid, i+1, template, stack[1:], uniqueSet)
                    # not replace, continue
                    valid += template[i]
            else:
                # concatnate template from pos to idx, cause left ( will look at its right
                valid += template[pos: idx]
                # left ( is able to replace one ( on its right
                for i in range(max(pos,idx), len(template)):
                    if template[i] == parenthese:
                        # replace, dfs
                        dfs(valid, i+1, template, stack[1:], uniqueSet)
                    # not replace, continue
                    valid += template[i]

        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append((c, i))
                continue
            
            if c == ')' and len(stack) > 0 and stack[-1][0] == '(':
                stack.pop()
            elif c == ')': 
                stack.append((c, i))

        uniqueSet = set()
        # print(stack)
        dfs('', 0, s, stack, uniqueSet)

        return list(uniqueSet)

# print(Solution().removeInvalidParentheses('(a)())()'))
# print(Solution().removeInvalidParentheses('())())())'))
# print(Solution().removeInvalidParentheses('(()(()(()'))


