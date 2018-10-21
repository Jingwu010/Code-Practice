class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """

        def rearrange(lst):
            lst.sort()
            return ''.join(map(str, lst))

        def retrieveNextBigger(lst, num):
            lst.sort()
            i = 0
            while i < len(lst):
                if lst[i] > num:
                    break
                i += 1
            return lst.pop(i)

        
        def compareBits(string, lst):
            if len(string) == 1:
                return -1
            last = string[-1]
            secondlast = string[-2]
            newlst = lst.copy()
            if int(last) > int(secondlast):
                newlst.append(int(last))
                newSmaller = retrieveNextBigger(newlst, int(secondlast))
                newlst.append(int(secondlast))
                return string[:-2] + str(newSmaller) + rearrange(newlst)
            else:
                newlst.append(int(last))
                return compareBits(string[:-1], newlst)

        # 32-bit integer 
        ret = int(compareBits(str(n), []))
        return ret if ret < 2**31 else -1

# print(Solution().nextGreaterElement(231))
# print(Solution().nextGreaterElement(1132))
# print(Solution().nextGreaterElement(11122))
print(Solution().nextGreaterElement(2147483647))