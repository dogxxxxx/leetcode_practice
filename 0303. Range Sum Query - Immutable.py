from typing import List
"""
Method 1:
Modify the input nums to be prefix sum

Time complexity: O(N) for init, O(1) for sumRange
Space complexity: O(1), do not count input nums
Date: 2024/03/14
"""

class NumArray:
    def __init__(self, nums: List[int]):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        else:
            return self.nums[right] - self.nums[left - 1]
