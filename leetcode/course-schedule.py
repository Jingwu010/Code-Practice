class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        class Node:
            def __init__(self, index):
                self.index = index
                self.inDegree = 0
                self.outEdges = []
            def __repr__(self):
                return str(self.inDegree) + str(self.outEdges)

        nodes = [Node(i) for i in range(numCourses)]
        for prerequ in prerequisites:
            source = prerequ[1]
            sink = prerequ[0]
            nodes[source].outEdges.append(sink)
            nodes[sink].inDegree += 1
            
        flag = True
        while flag:
            flag = False
            okNode = Node(-1)
            for node in nodes:
                if node.inDegree == 0:
                    okNode = node
                    flag = True
                    break

            for outEdge in okNode.outEdges:
                nodes[outEdge].inDegree -= 1

            okNode.inDegree = -1

        return sum([node.inDegree > 0 for node in nodes]) <= 0

# calculate in-degree version
# 
# another simple way is to iterate through all edges in the graph
# and follow the edge direction, you should never come BACK
# to one node which you have already started

print(Solution().canFinish(3, [[1,0],[2,0],[2,1],[0,2]]))