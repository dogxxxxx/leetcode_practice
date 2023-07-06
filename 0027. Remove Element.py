"""
Method 1:
Loop through the list from the end. If the number equals to val, pop it.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pops = 0
        init_len = len(nums)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                pops += 1
                nums.pop(i)
        return init_len - pops
