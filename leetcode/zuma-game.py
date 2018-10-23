class Solution:
    def findMinStep(self, board, hand):
        """
        :type board: str    len(board) <= 20
        :type hand: str     len(hand) <= 5
        :rtype: int
        """
        
        # Do we get balls after removing them from board? No
        
        def removeElem(string, elem, times):
            i = 0
            start = None
            end = None
            while times > 0:
                if string[i] == elem:
                    if start is None: start = i
                    end = i
                    times -= 1
                i += 1
            if start is not None:
                return string[:start] + string[end+1:]
            else:
                return string

        def dfs(board, hand):
            if board == '#': return 0
            steps = 10
            i = 0
            for j in range(len(board)):
                ball = board[i]
                if board[i] == board[j]:
                    continue

                needs = max(3-(j-i), 0)
                # print(board, hand, ball, needs, hand.count(ball) >= needs)
                if hand.count(ball) >= needs:
                    steps = min(dfs(board[:i]+board[j:], removeElem(hand, ball, needs))+needs, steps)
                i = j
            # print(board, hand, steps)
            return steps

        hand = ''.join(sorted(hand))
        steps = dfs(board+'#', hand)
        return steps if steps != 10 else -1
        # return sets[(tuple(board), tuple(hand))] if sets[(tuple(board), tuple(hand))] != 10 else -1

print(Solution().findMinStep('RRBRR','RRBB')) #2
print(Solution().findMinStep('WRRBBW','RB')) #-1
print(Solution().findMinStep('RBYYBBRRB','YRBGB')) #3
print(Solution().findMinStep('RRBRRBB','BBR')) #-1
print(Solution().findMinStep('YRRYYR','YRR')) #-1
print(Solution().findMinStep('GYGGYYRRYGGYR','GYGYY')) #-1

