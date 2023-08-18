"""
Method 1:
"""

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def flatten(board):
            flattened = []
            n = len(board)
            for i in range(n - 1, -1, -1):
                if (n - i) % 2 == 0:
                    board[i]
                    flattened += board[i][::-1]
                else:
                    flattened += board[i]
            return flattened

        board = flatten(board)
        dq = deque([(1, 1)])
        seen = set()
        target = len(board)
        while dq:
            print(dq)
            loc, step = dq.popleft()
            
            for ind in range(loc, loc+6):
                if ind >= target - 1:
                    return step
                if board[ind] != -1 and board[ind] not in seen:
                    if board[ind] == target:
                        return step
                    
                    dq.append((board[ind], step + 1))
                    seen.add(board[ind])
            
            for ind in range(loc+5, loc-1, -1):
                if board[ind] == -1:
                    dq.append((ind + 1, step + 1))
                    break
        return -1
