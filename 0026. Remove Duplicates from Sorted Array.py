"""
Method 1:
The same method as in cpp.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp = nums[0]
        result = 1
        i = 1
        while i < len(nums):
            if nums[i] == tmp:
                nums.pop(i)
                i -= 1
            else:
                tmp = nums[i]
                result += 1
            i += 1
        return result
