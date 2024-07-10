from typing import List
"""
Method 1:
Iterate the logs

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        for step in logs:
            if step == "./":
                continue
            elif step == "../":
                result -= 1 if result > 0 else 0
            else:
                result += 1
        return result
    

if __name__ == "__main__":
    logs = ["d1/","d2/","../","d21/","./"]
    res = Solution().minOperations(logs)
    print(res)