from typing import List
"""
Method 1:
Store the amount of 1s in previous layer

Time complexity: O(m*n)
Space complexity: O(1)
"""

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        prev = 0
        for i in range(0, len(bank)):
            curr = bank[i].count("1")
            if curr == 0:
                continue
            else:
                result += curr * prev
                prev = curr
        return result
    

if __name__ == "__main__":
    bank = ["011001","000000","010100","001000"]
    result = Solution().numberOfBeams(bank)
    print(result)