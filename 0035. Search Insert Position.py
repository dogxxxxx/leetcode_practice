from typing import List
"""
Method 1:
Binary Search

Time complexity: O(log(n))
Space complexity: O(1)
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                high = mid - 1                
        return low


if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,5,6]
    target = 2
    result = sol.searchInsert(nums, target)
    print(result)