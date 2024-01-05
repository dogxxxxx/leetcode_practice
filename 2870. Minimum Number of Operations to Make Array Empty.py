from typing import List
from collections import Counter
"""
Method 1:
Create a dictionary to store counts of each number.

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        if 1 in counts.values():
            return -1
        result = 0
        for val in counts.values():
            result +=  -(-val//3)
        return result
    

if __name__ == "__main__":
    nums = [2,3,3,2,2,4,2,3,4]
    result = Solution().minOperations(nums)
    print(result)