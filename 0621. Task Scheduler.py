from typing import List
from collections import Counter
"""
Method 1:
This question is to fill the idles with tasks

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        total = len(tasks)
        max_count = sum(value == max_freq for value in freq.values())
        result = max((max_freq - 1) * (n + 1) + max_count, total)
        return result
    

if __name__ == "__main__":
    tasks = ["A","B","C","D","A","B","V"]
    n = 3
    result = Solution().leastInterval(tasks, n)
    print(result)
