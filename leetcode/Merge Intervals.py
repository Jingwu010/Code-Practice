# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x: x.start)
        print(intervals)
        result = [intervals[0]]
        for interval in intervals:
        	prev = result[-1]
        	if interval.start <= prev.end:
        		prev.end = max(interval.end, prev.end)
        	else:
        		result.append(interval)
        return result

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[2,3],[1,2],[3,4],[6,18]]))