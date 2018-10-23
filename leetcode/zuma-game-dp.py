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
            start = -1
            end = -1
            while times > 0:
                if string[i] == elem:
                    if start == -1: start = i
                    end = i
                    times -= 1
                i += 1
            return string[:start] + string[end+1:]

        def removeConsecutives(string):
            start = 0
            equals = 0
            while start < len(string):
                if start+equals < len(string) and string[start] == string[start+equals]:
                    equals += 1
                else:
                    if equals >= 3:
                        return string[:start] + removeConsecutives(string[start+equals:])
                    start += equals
                    equals = 0
            return string

        def dfs(board, hand):
            while True:
                newBoard = removeConsecutives(board)
                if newBoard == board:
                    break
                board = newBoard

            if (tuple(board), tuple(hand)) in sets:
                return sets[(tuple(board), tuple(hand))]

            if len(board) <= 0:
                return 0
            if len(hand) <= 0:
                return 10

            steps = 10
            i = 0
            while True:
                ball = board[i]
                flag = False
                if i+1 < len(board):
                    flag = board[i+1] == board[i]
                # if there exist 2 consecutive balls
                if flag and hand.count(ball) > 0:
                    steps = min(dfs(board[:i]+board[i+2:], removeElem(hand, ball, 1))+1, steps)
                elif not flag and hand.count(ball) > 1:
                    steps = min(dfs(board[:i]+board[i+1:], removeElem(hand, ball, 2))+2, steps)
                i += (1 + flag)
                if i >= len(board):
                    break
            sets[(tuple(board), tuple(hand))] = steps
            return steps

        # print(removeConsecutives('YRYRYYRYYR'))
        sets = {}
        hand = ''.join(sorted(hand))
        dfs(board, hand)
        return sets[(tuple(board), tuple(hand))] if sets[(tuple(board), tuple(hand))] != 10 else -1

# print(Solution().findMinStep('RRBRR','RRBB')) #2
# print(Solution().findMinStep('WRRBBW','RB')) #-1
# print(Solution().findMinStep('RBYYBBRRB','YRBGB')) #3
# print(Solution().findMinStep('RRBRRBB','BBR')) #2
# print(Solution().findMinStep('YRRYYR','YRR')) #2

