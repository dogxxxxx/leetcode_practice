from typing import List
"""
Method 1:
Use 2 indices to find out same colors and
add the time to remove duplicated colors.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l = 0
        r = 1
        result = 0
        while r < len(colors):
            max_time = neededTime[l]
            time_need = neededTime[l]
            while r < len(colors) and colors[l] == colors[r]:
                time_need += neededTime[r]
                if neededTime[r] > max_time:
                    max_time = neededTime[r]
                r += 1
            time_need -= max_time
            result += time_need
            l = r
            r += 1
        return result


if __name__ == "__main__":
    colors = "aabaa"
    neededTime = [1,2,3,4,1]
    result = Solution().minCost(colors, neededTime)
    print(result)