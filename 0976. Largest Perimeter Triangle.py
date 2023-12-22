from typing import List
"""
Method 1:
Sort nums in descending order and loop through it.

Time complexity: O(nlog(n))
Space complexity: O(n) during sorting
"""

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0


if __name__ == "__main__":
    nums = [1,2,1,10]
    result = Solution().largestPerimeter(nums)
    print(result)