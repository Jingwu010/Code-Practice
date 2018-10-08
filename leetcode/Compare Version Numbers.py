class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        # If version1 > version2 return 1; 
        # if version1 < version2 return -1;
        # otherwise return 0.
        # 
        # "1.10" > "1.01"
        # "1.1.0" = "1.1"
        
        def alignCompare(version1, version2):
            v1 = int(version1[:version1.index('.')])
            v2 = int(version2[:version2.index('.')])
            if v1 == v2:
                if version1.index('.') == len(version1)-1 and version2.index('.') == len(version2)-1:
                    return 0
                version1 = '0.' if version1.index('.') == len(version1)-1 else version1[version1.index('.')+1:]
                version2 = '0.' if version2.index('.') == len(version2)-1 else version2[version2.index('.')+1:]
                return alignCompare(version1, version2)
            if v1 > v2:
                return 1
            else:
                return -1

        return alignCompare(version1+'.', version2+'.')

print(Solution().compareVersion("1.101", "1.011"))
# print(Solution().compareVersion("7.5.2.4", "7.5.3"))
# print(Solution().compareVersion("1", "1.0.1"))
# print(Solution().compareVersion("0.1", "1.1"))
# print(Solution().compareVersion("1.1.0", "1.1.0.0.1"))
print(Solution().compareVersion("1.0.0", "1"))