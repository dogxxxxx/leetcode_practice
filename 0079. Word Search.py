from typing import List
"""
Method 1:
backtrack, set the breakpoint to return True or False

Time complexity: O(M*N*K), where M is len(board), N is len(board[0]), and K is len(word)
Space complexity: O(K)
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, wordID):
            if wordID == len(word):
                return True
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
                return False
            
            current_char = board[i][j]
            if current_char != word[wordID]:
                return False
            
            board[i][j] = ''
            wordID += 1
            if backtrack(i + 1, j, wordID) or backtrack(i - 1, j, wordID) or backtrack(i, j + 1, wordID) or backtrack(i, j - 1, wordID):
                return True
            board[i][j] = current_char
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True


if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    result = Solution().exist(board, word)
    print(result)
