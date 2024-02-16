from typing import List
"""
Method 1:
Sort nums first and check from the end

Time complexity: O(N * log(N))
Space complexity: O(1)
"""

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        nums.sort()
        current_sum = sum(nums[:-1])
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < current_sum:
                return current_sum + nums[i]
            else:
                current_sum -= nums[i - 1]
        return -1
    

if __name__ == "__main__":
    nums = [5,5,50]
    result = Solution().largestPerimeter(nums)
    print(result)
