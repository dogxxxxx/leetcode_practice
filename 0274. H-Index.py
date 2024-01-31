from typing import List
"""
Method 1:
Sort the citations in reverse order.
Then, it's about math.

Time complexity: O(nlog(n))
Space complexity: O(1)
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
            if i == len(citations) - 1:
                return i + 1
    

if __name__ == "__main__":
    citations = [5,5,5,5,5]
    result = Solution().hIndex(citations)
    print(result)
