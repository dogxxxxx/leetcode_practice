"""
Method 1:
Keep how many times a number is duplicated. If larger than 2, remove it from the list.
This causes changes of length of the list.
Thus, create another variable to keep how many elements are removed to keep the index right.
It's quite stupid! There must be other methods to keep less things but too tired now to think about it.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates = 1
        tmp = nums[0]
        pop_times = 0
        for i in range(1, len(nums)):
            if tmp == nums[i - pop_times]:
                duplicates += 1
                if duplicates > 2:
                    nums.pop(i - pop_times)
                    pop_times += 1
            else:
                tmp = nums[i - pop_times]
                duplicates = 1
        return len(nums)
