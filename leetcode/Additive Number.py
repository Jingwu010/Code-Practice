class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)

        if n < 3:
            return False

        # The size range for both a, b 
        # should not bigger than n // 2
        for i in range(1, n//2+1):
            for j in range(1, n//2+1):
                # The ending index for all integers encountered so far
                idx = i+j
                a = int(num[:i])
                b = int(num[i:i+j])

                # Deal with leading zeros, only for initial cases
                if len(str(a)) != i or len(str(b)) != j:
                    continue
                    
                while True:
                    c = a+b
                    if not num[idx:].startswith(str(c)):
                        break
                    idx = idx+len(str(c))
                    a, b = b, c
                    if idx == n:
                        return True
        return False

print(Solution().isAdditiveNumber('112358'))
print(Solution().isAdditiveNumber('199100199'))
print(Solution().isAdditiveNumber('00000'))
print(Solution().isAdditiveNumber('224668'))
print(Solution().isAdditiveNumber('1111223'))
print(Solution().isAdditiveNumber('121325'))
print(Solution().isAdditiveNumber('00000011'))
print(Solution().isAdditiveNumber('0235813'))