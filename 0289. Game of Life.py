"""
Method 1:
Use 2 and 3 to represents the elements in the board that need to be modified to live or dead.
After iterating the board, we know the elements to be modified. Then, iterate the board again
and replace 2s and 3s with correct values.

Time complexity: O(MN), M is the number of rows and N is the number of columns
Space complexity: O(1)
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_sum(board, r, c):
            total = 0
            direction = [-1, 0, 1]
            dictionary = {
                0: 0,
                1: 1,
                2: 1,
                3: 0
            }
            for i in direction:
                for j in direction:
                    if r+i >= 0 and c+j >=0:
                        try:
                            total += dictionary[board[r+i][c+j]]
                        except:
                            pass
            return total - board[r][c]

        c = len(board[0])
        r = len(board)
        dictionary = {
                0: 0,
                1: 1,
                2: 0,
                3: 1
            }
        for i in range(r):
            for j in range(c):
                lives = get_sum(board, i, j)
                if board[i][j]:
                    if lives<2 or lives>3:
                        board[i][j] = 2
                else:
                    if lives == 3:
                        board[i][j] = 3
        
        for i in range(r):
            for j in range(c):
                board[i][j] = dictionary[board[i][j]]
