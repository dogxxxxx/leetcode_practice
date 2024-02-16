from typing import List
"""
Method 1:
Create row 0 and calculate the next row

Time complexity: O(N*2)
Space complexity: O(N)
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        start = [1]
        for _ in range(rowIndex):
            for i in range(len(start) - 1):
                start[i] = start[i] + start[i + 1]
            start.insert(0, 1)
        return start
    

if __name__ == "__main__":
    rowIndex = 1
    result = Solution().getRow(rowIndex)
    print(result)
