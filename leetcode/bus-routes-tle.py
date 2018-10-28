import heapq
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
        maxNodes = 2501
        maxDist = 501

        indexes = [-1] * maxNodes
        graph = [[False]*maxNodes for _ in range(maxNodes)]
        distinct = 0
        for route in routes:
            for i in range(len(route)):
                for j in range(i, len(route)):
                    num1 = route[i]
                    num2 = route[j]
                    if num1 not in indexes:
                        indexes[distinct] = num1
                        distinct += 1
                    if num2 not in indexes:
                        indexes[distinct] = num2
                        distinct += 1
                    graph[indexes.index(num1)][indexes.index(num2)] = True
                    graph[indexes.index(num2)][indexes.index(num1)] = True

        # print(indexes)

        def dijkstra(graph, source, target):
            dist = [maxDist] * maxNodes
            dist[indexes.index(source)] = 0
            queue = list()
            for j in range(maxNodes):
                if graph[indexes.index(source)][j] and dist[j] > 1:
                    dist[j] = 1
                    queue.append(j)

            while queue:
                print(queue)
                min_i = -1
                min_dist = maxDist
                for i in queue:
                    if dist[i] < min_dist:
                        min_dist = dist[i]
                        min_i = i
                print(min_i, min_dist)
                queue.remove(min_i)

                for j in range(maxNodes):
                    if graph[min_i][j] and dist[j] > min_dist+1:
                        dist[j] = min_dist+1
                        queue.append(j)
            return dist[indexes.index(target)]

        return dijkstra(graph, S, T)

print(Solution().numBusesToDestination([[1, 2, 7], [3, 6, 7]],1,3))