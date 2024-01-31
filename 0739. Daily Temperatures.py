from typing import List
"""
Method 1:
Use a stack to store unsolved elements

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for ind, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                index, _ = stack.pop()
                result[index] = ind - index
            stack.append((ind, val))
        return result
    

if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    result = Solution().dailyTemperatures(temperatures)
    print(result)
