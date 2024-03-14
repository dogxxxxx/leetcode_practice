from typing import List
"""
Method 1:
Use 2 pointers and calculate sum of elements between these pointers.
If sum >= target, move left pointer one unit to the right.
Otherwise, move right pointer one unit to the right until right pointer points
to the end of nums.

Time complexity: O(N)
Space complexity: O(1)
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
    
"""
Method 2:
Use sliding window to calculate current sum

Time complexity: O(N)
Space complexity: O(1)
Date: 2024/03/14
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p1 = 0
        current_sum = 0
        result = float('inf')
        for i in range(len(nums)):
            current_sum += nums[i]
            while current_sum >= target:
                result = min(result, i - p1 + 1)
                current_sum -= nums[p1]
                p1 += 1
        
        return 0 if result == float('inf') else result


if __name__ == "__main__":
    target = 7
    nums = [2,3,1,2,4,3]
    result = Solution().minSubArrayLen(target, nums)
    print(result)
