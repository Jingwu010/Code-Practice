import heapq
class Solution:
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        
        fzstsy
        
        1.sumneed:record the number of dress needed until i, the step must be larger than abs(sumneed). Because each machine at each step can get at most one dress from one direction.
        2.When the number of dress in current machine is larger than ave, it must be offloaded. Each step can only offload one dress.
        3.The maximum step is max(1,2).
        """
        
        # sums = sum(machines)
        # n = len(machines)
        # if sums % n != 0:
        #     return -1
        
        # avg = sums // n
        # chaos = 0
        # heap = []
        # for machine in machines:
        #     if machine > avg:
        #         chaos += machine - avg
        #         heapq.heappush(heap, machine - avg)

        # steps = 0
        # while chaos > 0:
        #     # time.sleep(1)
        #     # print(heap, chaos)
        #     t = len(heap)
        #     moves = heapq.heappop(heap)
        #     chaos -= moves*t
        #     heap = [x-moves for x in heap]
        #     steps += moves
        # return steps

        tot = sum(machines)
        L = len(machines)
        if tot%L!=0:
            return -1
        ave = tot//L
        sumneed = 0
        res = 0
        for m in machines:
            sumneed += m-ave
            res = max(res,abs(sumneed),m-ave)
        return res

print(Solution().findMinMoves([1,0,5]))
# print(Solution().findMinMoves([0,3,0]))
# print(Solution().findMinMoves([4,1,0,4,1]))