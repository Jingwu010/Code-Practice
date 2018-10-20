class Solution:
    def findSchedules(self, work_hours, day_hours, pattern):
        """
        :type work_hours: int   [1...56]
        :type day_hours: int    [1...8]
        :type pattern: string   len=7
        :rtype: List[string]    Lexicographically

        # At least one correct schedule
        """ 
        
        def combination(idxs, target, limit, works, ret):
            # idxs: Available free indexes in pattern
            # target: remaining work load to fill up
            # works: current working hour pattern
            days = len(idxs)
            # print(target, works)
            if days == 0:
                if target == 0:
                    ret.append(works)
                return

            if target < 0:
                return

            loc = idxs[0]

            # print(target-(days-1)*limit)
            # the minimum work per day is max(target-(days-1)*limit,0), all len-1 days work full hours
            # the maximum work per day is min(limit,target)+1, reaching the target or limit
            for i in range(max(target-(days-1)*limit,0), min(limit,target)+1):
                # print(i)
                combination(idxs[1:], target-i, limit, works[:loc]+str(i)+works[loc+1:], ret)

        idxs = []
        remaining = work_hours
        for i, c in enumerate(pattern):
            if ord(c) == 63:
                idxs.append(i)
            else:
                remaining -= int(c)
        ret = []
        combination(idxs, remaining, day_hours, pattern, ret)
        return ret

# print(Solution().findSchedules(3,1,'???????'))
print(Solution().findSchedules(25,4,'??434??'))


