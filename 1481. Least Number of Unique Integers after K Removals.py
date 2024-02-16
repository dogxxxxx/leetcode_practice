from typing import List
from collections import Counter
"""
Method 1:
Count the amounts of each number
Sort the count

Time complexity: O(N * log(N))
Space complexity: O(N)
"""

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        vals = Counter(arr).values()
        vals = sorted(list(vals))
        i = 0
        while k >= 0 and i < len(vals):
            k -= vals[i]
            i += 1
        return len(vals) - i + 1 - (k>=0)  
                

if __name__ == "__main__":
    arr = [1]
    k = 1
    result = Solution().findLeastNumOfUniqueInts(arr, k)
    print(result)
