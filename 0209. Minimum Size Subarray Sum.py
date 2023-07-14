"""
Method 1:
Use 2 pointers and calculate sum of elements between these pointers.
If sum >= target, move left pointer one unit to the right.
Otherwise, move right pointer one unit to the right until right pointer points
to the end of nums.

Time complexity:
Space complexity:
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p1 = 0
        p2 = 0
        tmp_sum = nums[0]
        result = len(nums) + 1
        while p2 < len(nums):
            if tmp_sum < target:
                p2 += 1
                if p2 == len(nums):
                    break
                tmp_sum += nums[p2]
            else:
                result = min(result, p2-p1+1)
                tmp_sum -= nums[p1]
                p1 += 1
        if result == len(nums) + 1:
            return 0
        return result
