from typing import List
"""
Method 1:
Keep reachable index at every step.
Count the step when the current index equals reachable.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        reachable = 0
        current_end = 0

        for i in range(len(nums) - 1):
            reachable = max(reachable, i + nums[i])
            if i == current_end:
                result += 1
                current_end = reachable
        return result


if __name__ == "__main__":
    nums = [0]
    result = Solution().jump(nums)
    print(result)
