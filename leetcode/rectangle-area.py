class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        # AB = CD?
        
        def getIntersection(interval1, interval2):
            # Take two intervals and return the intersection length
            if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
                return 0
            return abs(max(interval1[0], interval2[0])-min(interval1[1], interval2[1]))

        return (C-A)*(D-B)+(G-E)*(H-F)-getIntersection((A,C), (E,G))*getIntersection((B,D),(F,H))

print(Solution().computeArea(0,0,7,5,0,0,5,7))

