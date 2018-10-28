import collections
class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int

        1 <= routes.length <= 500.
        1 <= routes[i].length <= 500.
        0 <= routes[i][j] < 10 ^ 6
        """
        # what buses stop at location x
        to_stop = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route: to_stop[j].add(i)

        queue = list([(S,0)])
        seen = set([S])
        while queue:
            stop, dis = queue.pop(0)
            if stop == T:
                return dis
            for route_i in to_stop[stop]:
                for v in routes[route_i]:
                    if v not in seen:
                        queue.append((v, dis+1))
                        seen.add(v)
                routes[route_i] = []
        return -1

print(Solution().numBusesToDestination([[1,3,5],[3,7,9],[5,7,11],[9,11,13],[11,13,15]],1,15))